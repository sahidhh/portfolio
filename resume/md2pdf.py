"""Render a resume .md to PDF with headless Chrome.

    py resume/md2pdf.py                       # DotNet variant -> resume/Sahidhullah_H_Resume.pdf (what the site links)
    py resume/md2pdf.py resume/Sahidhullah_H_Resume_AI-Python.md out.pdf

Needs: pip install markdown ; Chrome installed. Or skip this entirely and drop your own
PDF at resume/Sahidhullah_H_Resume.pdf — the site only cares about that filename.
"""
import os, subprocess, sys, tempfile
import markdown  # pip install markdown

HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "Sahidhullah_H_Resume_DotNet.md")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "Sahidhullah_H_Resume.pdf")
CHROME = next(p for p in (
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
) if os.path.exists(p))

CSS = """
@page { size: A4; margin: 14mm 16mm; }
body { font: 10.5pt/1.4 "Public Sans", "Segoe UI", Arial, sans-serif; color: #1b2431; }
h1 { font-size: 20pt; margin: 0 0 2pt; letter-spacing: -.01em; }
h1 + p { margin: 0 0 2pt; font-weight: 600; }
h2 { font-size: 10pt; letter-spacing: .06em; margin: 12pt 0 4pt; padding-bottom: 2pt; border-bottom: 1px solid #1b2431; }
h3, p, ul { margin: 0 0 4pt; }
ul { padding-left: 14pt; }
li { margin-bottom: 2pt; }
hr { display: none; }
em { color: #5f6b7a; }
a { color: inherit; text-decoration: none; }
"""
html = "<!doctype html><meta charset=utf-8><style>%s</style>%s" % (
    CSS, markdown.markdown(open(src, encoding="utf-8").read()))
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
    f.write(html); tmp = f.name
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--print-to-pdf=" + out, "file:///" + tmp.replace("\\", "/")], check=True, capture_output=True)
os.unlink(tmp)
print("wrote", out, os.path.getsize(out), "bytes")
