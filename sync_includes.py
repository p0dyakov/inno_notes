#!/usr/bin/env python3
"""Replace include-after-body content in all _site/*.html files."""
import glob, re, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
INCLUDE = os.path.join(ROOT, "_includes", "index.html")
SITE = os.path.join(ROOT, "_site")

with open(INCLUDE, "r") as f:
    new_content = f.read().strip()

# The include-after-body block starts with our <style> and ends with </script>
# right before </body>. We match from our first CSS custom property to the
# closing </script> that belongs to our block.
pattern = re.compile(
    r'(<style>\s*\n\s*:root\s*\{[^}]*--inn-bg:.*?</script>)',
    re.DOTALL
)

files = glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)
updated = 0
for path in files:
    with open(path, "r") as f:
        html = f.read()
    m = pattern.search(html)
    if not m:
        continue
    if m.group(1).strip() == new_content:
        continue
    html = html[:m.start(1)] + new_content + html[m.end(1):]
    with open(path, "w") as f:
        f.write(html)
    updated += 1

print(f"Updated {updated}/{len(files)} files")
