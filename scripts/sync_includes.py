#!/usr/bin/env python3
"""Replace include-after-body content in all _site/*.html files."""
import glob, re, os

ROOT = os.path.dirname(os.path.abspath(__file__))
INCLUDE = os.path.join(ROOT, "_includes", "index.html")
SITE = os.path.join(ROOT, "_site")

with open(INCLUDE, "r") as f:
    new_content = f.read().strip()

# The include starts with a websocket patch script followed by a <style> block.
# A previous buggy sync duplicated only that leading script, so we normalize
# the prefix separately and then replace the rest of the include block.
prefix, _, suffix = new_content.partition("<style>")
prefix = prefix.strip()
suffix = f"<style>{suffix}".strip()

prefix_pattern = re.compile(
    r'(?:<script>\s*// Patch WebSocket BEFORE quarto-preview\.js.*?</script>\s*)+(?=<style>\s*\n\s*:root\s*\{)',
    re.DOTALL,
)
suffix_pattern = re.compile(
    r'(<style>\s*\n\s*:root\s*\{[^}]*--inn-bg:.*?</script>)',
    re.DOTALL,
)

files = glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)
updated = 0
for path in files:
    with open(path, "r") as f:
        html = f.read()
    html_next = prefix_pattern.sub(f"{prefix}\n\n", html, count=1)
    m = suffix_pattern.search(html_next)
    if not m:
        continue
    if html_next == html and m.group(1).strip() == suffix:
        continue
    html_next = html_next[:m.start(1)] + suffix + html_next[m.end(1):]
    with open(path, "w") as f:
        f.write(html_next)
    updated += 1

print(f"Updated {updated}/{len(files)} files")
