#!/usr/bin/env bash
# Cloudflare: DNS only (grey cloud) → GitHub Pages. HTTPS is issued by GitHub Pages, not CF proxy.
# Requires: curl, jq, CLOUDFLARE_API_TOKEN with Zone.DNS Edit.
set -euo pipefail

DOMAIN="${DOMAIN:-innonotes.ru}"
GITHUB_TARGET="${GITHUB_TARGET:-p0dyakov.github.io}"
GITHUB_A=(
	185.199.108.153
	185.199.109.153
	185.199.110.153
	185.199.111.153
)
API="https://api.cloudflare.com/client/v4"

if [[ -z "${CLOUDFLARE_API_TOKEN:-}" ]]; then
	echo "Set CLOUDFLARE_API_TOKEN (Zone.DNS Edit)." >&2
	exit 1
fi

cf_api() {
	local method="$1" path="$2"
	shift 2
	curl -sS -X "$method" "${API}${path}" \
		-H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
		-H "Content-Type: application/json" \
		"$@"
}

ensure_success() {
	local resp="$1"
	if [[ "$(echo "$resp" | jq -r '.success')" != "true" ]]; then
		echo "$resp" | jq . >&2
		exit 1
	fi
}

echo "Looking up zone ${DOMAIN}..."
ZONE_RESP="$(cf_api GET "/zones?name=${DOMAIN}&status=active")"
ensure_success "$ZONE_RESP"
ZONE_ID="$(echo "$ZONE_RESP" | jq -r '.result[0].id')"
if [[ -z "$ZONE_ID" || "$ZONE_ID" == "null" ]]; then
	echo "Zone not found for ${DOMAIN}" >&2
	exit 1
fi
echo "Zone ID: ${ZONE_ID}"

echo "Fetching DNS records..."
RECORDS="$(cf_api GET "/zones/${ZONE_ID}/dns_records?per_page=500")"
ensure_success "$RECORDS"

delete_matching_records() {
	local filter="$1"
	echo "$RECORDS" | jq -r "$filter | .id" | while read -r id; do
		[[ -z "$id" || "$id" == "null" ]] && continue
		local name type proxied
		name="$(echo "$RECORDS" | jq -r --arg id "$id" '.result[] | select(.id==$id) | .name')"
		type="$(echo "$RECORDS" | jq -r --arg id "$id" '.result[] | select(.id==$id) | .type')"
		proxied="$(echo "$RECORDS" | jq -r --arg id "$id" '.result[] | select(.id==$id) | .proxied')"
		echo "  Deleting ${type} ${name} (proxied=${proxied})..."
		DEL="$(cf_api DELETE "/zones/${ZONE_ID}/dns_records/${id}")"
		ensure_success "$DEL"
	done
}

# Remove apex CNAME/A/AAAA and www CNAME — we'll recreate DNS-only.
delete_matching_records ".result[] | select(.name==\"${DOMAIN}\" and (.type==\"CNAME\" or .type==\"A\" or .type==\"AAAA\"))"
delete_matching_records ".result[] | select(.name==\"www.${DOMAIN}\" and .type==\"CNAME\")"

upsert_a() {
	local ip="$1"
	local existing
	existing="$(echo "$RECORDS" | jq -r --arg n "$DOMAIN" --arg ip "$ip" \
		'.result[] | select(.type=="A" and .name==$n and .content==$ip) | .id' | head -1)"
	local payload
	payload="$(jq -n --arg name "$DOMAIN" --arg content "$ip" \
		'{type:"A", name:$name, content:$content, proxied:false, ttl:300}')"
	if [[ -n "$existing" && "$existing" != "null" ]]; then
		echo "  Updating A ${DOMAIN} -> ${ip} (DNS only)..."
		UPD="$(cf_api PUT "/zones/${ZONE_ID}/dns_records/${existing}" --data "$payload")"
		ensure_success "$UPD"
	else
		echo "  Creating A ${DOMAIN} -> ${ip} (DNS only)..."
		CRE="$(cf_api POST "/zones/${ZONE_ID}/dns_records" --data "$payload")"
		ensure_success "$CRE"
	fi
}

upsert_www_cname() {
	local fqdn="www.${DOMAIN}"
	local existing
	existing="$(echo "$RECORDS" | jq -r --arg n "$fqdn" '.result[] | select(.type=="CNAME" and .name==$n) | .id' | head -1)"
	local payload
	payload="$(jq -n --arg name "www" --arg content "$GITHUB_TARGET" \
		'{type:"CNAME", name:$name, content:$content, proxied:false, ttl:300}')"
	if [[ -n "$existing" && "$existing" != "null" ]]; then
		echo "  Updating CNAME ${fqdn} -> ${GITHUB_TARGET} (DNS only)..."
		UPD="$(cf_api PUT "/zones/${ZONE_ID}/dns_records/${existing}" --data "$payload")"
		ensure_success "$UPD"
	else
		echo "  Creating CNAME ${fqdn} -> ${GITHUB_TARGET} (DNS only)..."
		CRE="$(cf_api POST "/zones/${ZONE_ID}/dns_records" --data "$payload")"
		ensure_success "$CRE"
	fi
}

echo "Refreshing DNS records..."
RECORDS="$(cf_api GET "/zones/${ZONE_ID}/dns_records?per_page=500")"
ensure_success "$RECORDS"

echo "Configuring GitHub Pages DNS (grey cloud, no proxy)..."
for ip in "${GITHUB_A[@]}"; do
	upsert_a "$ip"
done
upsert_www_cname

echo ""
echo "Done. Cloudflare is DNS-only; HTTPS comes from GitHub Pages."
echo "GitHub Pages target: ${GITHUB_TARGET}"
echo "Verify (expect 185.199.x, not 104.21.x):"
echo "  dig +short ${DOMAIN}"
echo "  dig +short www.${DOMAIN}"
echo "  curl -sI https://${DOMAIN}/ | head -5"
