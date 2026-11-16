"""Makes index.html, evidence.html and app.html fully self-contained (CSS + JS inlined)
so the site renders correctly even if the assets/ folder is missing on the host."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
for page in ["index.html", "evidence.html", "app.html"]:
    s = rd(page)
    s = re.sub(r'<link rel="stylesheet" href="(assets/[^"]+)">', lambda m: "<style>\n" + rd(m.group(1)) + "\n</style>", s)
    s = re.sub(r'<script src="(assets/[^"]+)"></script>', lambda m: "<script>\n" + rd(m.group(1)).replace("</script", "<\\/script") + "\n</script>", s)
    # fixed size on the logo so it can never blow up
    s = s.replace('<svg viewBox="0 0 32 32" aria-hidden="true">', '<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true">')
    open(os.path.join(ROOT, page), "w", encoding="utf-8").write(s)
    print(page, len(s) // 1024, "KB", "external css/js left:", len(re.findall(r'href="assets/|src="assets/', s)))
