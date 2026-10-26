# Shared pieces for both pages: head, stylesheet, logo, site bar and pager.
import base64, pathlib

SHARED = pathlib.Path(__file__).parent
ROOT = SHARED.parent.parent  # repo root, where the site is served from

# Each page's address relative to the site root. Links between pages stay relative so they work
# on Vercel (/) and on GitHub Pages (/Interaction-Design-Intensive/).
PAGES = [
    ("brief", "", "Part 1", "Design Brief"),
    ("map", "scenario-map/", "Part 2", "Scenario Map"),
]

def href(frm, to):
    depth = dict((k, p) for k, p, *_ in PAGES)[frm].count("/")
    target = dict((k, p) for k, p, *_ in PAGES)[to]
    return ("../" * depth + target) or "./"

def sitebar(current):
    cur = ' aria-current="page"'
    tabs = "".join(
        f'<a href="{href(current, k)}"{cur if k == current else ""}><small>{part}</small>{name}</a>'
        for k, _, part, name in PAGES)
    return (f'<div class="sitebar"><div class="wrap"><span class="site-name"><b>Nimbus Labs</b> · Team Resource Allocation Platform</span>'
            f'<nav class="parts" aria-label="Assignment parts">{tabs}</nav></div></div>')

def pager(current, to, sub):
    i, j = [k for k, *_ in PAGES].index(current), [k for k, *_ in PAGES].index(to)
    _, _, part, name = PAGES[j]
    cls, dirlabel, arr = ("next", "Next", "→") if j > i else ("prev", "Previous", "←")
    return (f'<div class="wrap pager"><a class="{cls}" href="{href(current, to)}"><span class="dir">{dirlabel} · {part}</span>'
            f'<span class="ttl">{name}</span><span class="sub">{sub}</span><span class="arr" aria-hidden="true">{arr}</span></a></div>')

def common(current):
    return {
        "HEAD": (SHARED / "head.html").read_text().rstrip("\n"),
        "SHARED_CSS": (SHARED / "shared.css").read_text().rstrip("\n"),
        "LOGO": base64.b64encode((SHARED / "logo.png").read_bytes()).decode(),
        "SITEBAR": sitebar(current),
    }

def document(page):
    # Templates are written as a head fragment (title, links, style) followed by the body; wrap them in a full document
    head, body = page.split("</style>\n", 1)
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'{head}</style>\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n')

def write(key, page):
    assert "{{" not in page
    page = document(page)
    path = dict((k, p) for k, p, *_ in PAGES)[key]
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    print(f"wrote {out.relative_to(ROOT)} ({len(page):,} bytes)")
