import pathlib
import re

TARGET = pathlib.Path(__file__).resolve().parent.parent / "pricing-api.html"
text = TARGET.read_text(encoding="utf-8")
pattern = r'<span class="func-fn">([^<]+)</span><span class="func-args">\(([^)]*)\)</span>'
replacement = (
    r'<span class="func-fn">\1</span><span class="func-paren">(</span>'
    r'<span class="func-params">\2</span><span class="func-paren">)</span>'
)
new, n = re.subn(pattern, replacement, text)
if n == 0:
    raise SystemExit("no matches")
TARGET.write_text(new, encoding="utf-8", newline="\n")
print(f"updated {n} signatures in {TARGET}")
