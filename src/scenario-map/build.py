import html, pathlib, re, sys
from collections import Counter

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "shared"))
import sitekit
from data import USERS, EXPERIENCES, PRIORITY_DEFS, MAP, CS

esc = lambda s: html.escape(s, quote=False)
attr = lambda s: html.escape(s, quote=True)

# Users as they're named in the tables -> filter key and tier
PEOPLE = {
    "Arjun": ("arjun", "Primary"), "Nisha": ("nisha", "Primary"),
    "Individual Contributor": ("ic", "Secondary"), "Individual Contributors": ("ic", "Secondary"),
    "Delivery Head": ("dh", "Secondary"), "Delivery Head / Account Manager": ("dh", "Secondary"),
    "Admin": ("admin", "Secondary"), "Admin / Resource Ops": ("admin", "Secondary"),
    "Leadership": ("lead", "Tertiary"), "Finance": ("fin", "Tertiary"),
}
FILTER_USERS = [("arjun", "Arjun"), ("nisha", "Nisha"), ("ic", "Individual Contributor"), ("dh", "Delivery Head"),
                ("admin", "Admin"), ("lead", "Leadership"), ("fin", "Finance")]

def chip(name, label=None):
    tier = PEOPLE[name][1]
    return f'<span class="chip tier-{tier.lower()}">{esc(label or name)}</span>'

# ---- Scenario map ----
rows = []
for line in MAP.strip().splitlines():
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    assert len(c) == 8, line
    rows.append(dict(id=c[0], exp=c[1], user=c[2], text=c[3], cat=c[4], type=c[5], crud=c[6], pri=c[7]))
assert [r["id"] for r in rows] == [f"S{i}" for i in range(1, 158)]
EXP_ID = {e[1]: e[0] for e in EXPERIENCES}
assert all(r["exp"] in EXP_ID for r in rows)
pc, tc, cc = Counter(r["pri"] for r in rows), Counter(r["type"] for r in rows), Counter(r["crud"] for r in rows)
assert (pc["P1"], pc["P2"], pc["P3"]) == (48, 80, 29), pc
assert (tc["Main"], tc["Atypical"], tc["External"]) == (106, 38, 13), tc

# Consolidated scenario coverage: every P1 exactly once
cs_of = {}
for cs in CS:
    ids = cs["ids"].split(", ")
    cs["idlist"] = ids
    for i in ids:
        assert i not in cs_of, i
        cs_of[i] = cs["id"]
    # every ID cited in the actions is in the consolidated list, and vice versa
    cited = set(re.findall(r"S\d+", " ".join(cs["actions"])))
    assert cited == set(ids), (cs["id"], cited ^ set(ids))
p1 = {r["id"] for r in rows if r["pri"] == "P1"}
assert set(cs_of) == p1, set(cs_of) ^ p1

def users_of(u):
    return [x for x in u.split(", ")]

def map_row(r):
    keys = " ".join(PEOPLE[u][0] for u in users_of(r["user"]))
    ucell = "".join(chip(u) for u in users_of(r["user"]))
    cs = cs_of.get(r["id"])
    cstag = f'<a class="cstag" href="#{cs}" data-jump="{cs}" title="Covered by consolidated scenario {cs[2:]}">{cs}</a>' if cs else ""
    search = attr(f'{r["id"]} {r["user"]} {r["text"]} {r["cat"]} {r["type"]} {r["crud"]} {r["pri"]}'.lower())
    return (f'<tr id="{r["id"]}" data-p="{r["pri"]}" data-t="{r["type"]}" data-c="{r["crud"]}" data-u="{keys}" data-s="{search}">'
            f'<td class="sid">{r["id"]}</td><td class="ucell">{ucell}</td><td class="stext">{esc(r["text"])}</td>'
            f'<td class="catcell">{r["cat"]}</td><td><span class="ttag t-{r["type"].lower()}">{r["type"]}</span></td>'
            f'<td class="ccell"><span class="crud c-{r["crud"].lower()}" title="{r["crud"]}">{r["crud"][0]}</span><span class="crudw">{r["crud"]}</span></td>'
            f'<td class="pcell"><span class="pri {r["pri"].lower()}">{r["pri"]}</span>{cstag}</td></tr>')

def minibar(counter, total):
    segs = "".join(f'<i class="{p.lower()}" style="flex:{counter[p]}"></i>' for p in ("P1", "P2", "P3") if counter[p])
    nums = " ".join(f'<span><b class="d {p.lower()}"></b>{p} {counter[p]}</span>' for p in ("P1", "P2", "P3"))
    return f'<span class="mini"><span class="mbar">{segs}</span><span class="mnums">{nums}</span></span>'

groups = []
for eid, name, *_ in EXPERIENCES:
    rs = [r for r in rows if r["exp"] == name]
    c = Counter(r["pri"] for r in rs)
    groups.append(f'''<details class="xgroup" id="map-{eid}" data-exp="{eid}">
  <summary><span class="eid">{eid}</span><span class="xname">{esc(name)}</span><span class="xcount" data-total="{len(rs)}">{len(rs)} scenarios</span>{minibar(c, len(rs))}<span class="chev" aria-hidden="true"></span></summary>
  <div class="tablewrap inner"><table class="smap">
    <thead><tr><th>ID</th><th>User</th><th>Scenario</th><th>Category</th><th>Type</th><th>CRUD</th><th>Priority</th></tr></thead>
    <tbody>
{chr(10).join(map_row(r) for r in rs)}
    </tbody></table></div>
</details>''')

# ---- Section 1: users ----
ucount = Counter()
for r in rows:
    for u in users_of(r["user"]):
        ucount[PEOPLE[u][0]] += 1
user_html = []
for tier in ("Primary", "Secondary", "Tertiary"):
    cards = []
    for t, name, role, ini, tasks in USERS:
        if t != tier: continue
        key = PEOPLE[name][0]
        role_html = f'<span class="urole">{esc(role)}</span>' if role else ""
        cards.append(f'''<article class="panel ucard">
  <header><span class="avatar av-{tier.lower()}" aria-hidden="true">{ini}</span><div><h4>{esc(name)}</h4>{role_html}</div></header>
  <p class="tlabel">Key tasks</p>
  <ul class="list">{"".join(f"<li>{esc(x)}</li>" for x in tasks)}</ul>
  <button class="ujump" type="button" data-user="{key}">See {ucount[key]} scenarios in the map <span aria-hidden="true">→</span></button>
</article>''')
    grid = "grid2" if tier == "Primary" else "grid3"
    user_html.append(f'<div class="tierhead"><span class="chip tier-{tier.lower()}">{tier}</span><h3>{tier} users</h3></div>\n<div class="{grid}">{"".join(cards)}</div>')

# ---- Section 2: experiences ----
exp_rows = []
for eid, name, users, goal, value in EXPERIENCES:
    n = sum(1 for r in rows if r["exp"] == name)
    uc = "".join(chip(u) for u in users.split(", "))
    if eid == "E11":
        uc = '<span class="allu">All users</span>' + uc
    value_html = re.sub(r"\(([^)]*)\)$", lambda m: f'<span class="oref">{m.group(1)}</span>', esc(value))
    exp_rows.append(f'<tr><td class="sid">{eid}</td><td class="xn"><strong>{esc(name)}</strong></td><td><div class="uchips">{uc}</div></td>'
                    f'<td>{esc(goal)}</td><td>{value_html}</td><td><a class="xjump" href="#map-{eid}" data-open="map-{eid}">{n}</a></td></tr>')

# ---- Section 3: summary + defs ----
def splitbar(items):
    tot = sum(n for _, n, _ in items)
    segs = "".join(f'<span class="seg2 {cls}" style="flex:{n}"><b>{n}</b></span>' for _, n, cls in items)
    leg = "".join(f'<span><i class="d {cls}"></i>{lab} <b>{n}</b></span>' for lab, n, cls in items)
    return f'<div class="sbar">{segs}</div><div class="sleg">{leg}</div>'

stats = f'''<div class="stats">
  <div class="panel stat big"><span class="tlabel">Unique scenarios</span><span class="num">{len(rows)}</span><span class="sub">across {len(EXPERIENCES)} experiences and 7 users</span></div>
  <div class="panel stat"><span class="tlabel">By priority</span>{splitbar([("P1 MVP", pc["P1"], "p1"), ("P2 Expansion", pc["P2"], "p2"), ("P3 Add-on", pc["P3"], "p3")])}</div>
  <div class="panel stat"><span class="tlabel">By type</span>{splitbar([("Main", tc["Main"], "t1"), ("Atypical / Edge", tc["Atypical"], "t2"), ("External", tc["External"], "t3")])}</div>
  <div class="panel stat"><span class="tlabel">By CRUD action</span>{splitbar([("Create", cc["Create"], "k1"), ("Read", cc["Read"], "k2"), ("Update", cc["Update"], "k3"), ("Delete", cc["Delete"], "k4")])}</div>
</div>'''
defs = "".join(f'<div class="panel pdef"><span class="pri {p.lower()}">{p}</span><div><h4>{p} = {lab}</h4><p>{esc(d)}</p></div></div>' for p, lab, d in PRIORITY_DEFS)

def fbtns(group, items):
    out = [f'<button class="fbtn" type="button" data-f="{group}" data-v="all" aria-pressed="true">All</button>']
    out += [f'<button class="fbtn" type="button" data-f="{group}" data-v="{v}" aria-pressed="false">{esc(l)}</button>' for v, l in items]
    return "".join(out)
filters = f'''<div class="toolbar" id="mapbar">
  <div class="tgroup" role="group" aria-label="Filter by priority"><span class="tlabel">Priority</span>{fbtns("p", [("P1","P1"),("P2","P2"),("P3","P3")])}</div>
  <div class="tgroup" role="group" aria-label="Filter by type"><span class="tlabel">Type</span>{fbtns("t", [("Main","Main"),("Atypical","Atypical"),("External","External")])}</div>
  <div class="tgroup" role="group" aria-label="Filter by CRUD"><span class="tlabel">CRUD</span>{fbtns("c", [("Create","Create"),("Read","Read"),("Update","Update"),("Delete","Delete")])}</div>
  <div class="tgroup" role="group" aria-label="Filter by user"><span class="tlabel">User</span>{fbtns("u", FILTER_USERS)}</div>
  <div class="tgroup grow1"><label class="tlabel" for="q">Search</label><input id="q" type="search" placeholder="e.g. overrun, notice, S46" autocomplete="off"></div>
  <div class="end"><span class="count" id="mapcount"></span><button class="fbtn" type="button" id="reset" hidden>Clear filters</button><button class="fbtn" type="button" id="toggleall">Expand all</button></div>
</div>'''

# ---- Section 4: consolidated scenarios ----
def link_ids(s):
    return re.sub(r"S\d+", lambda m: f'<a class="sref" href="#{m.group(0)}" data-row="{m.group(0)}">{m.group(0)}</a>', esc(s))

total_p1 = len(p1)
cov = "".join(f'<a class="cseg cs{i+1}" href="#{c["id"]}" style="flex:{len(c["idlist"])}"><b>{c["id"]}</b><span>{len(c["idlist"])}</span></a>' for i, c in enumerate(CS))
coverage = f'''<div class="panel coverage">
  <div class="covhead"><h3>Coverage check</h3><p><strong>{len(cs_of)} of {total_p1}</strong> MVP (P1) scenarios are covered, with no repeats.</p></div>
  <div class="covbar">{cov}</div>
  <p class="covsum">{" + ".join(f'{c["id"]} ({len(c["idlist"])})' for c in CS)} = {len(cs_of)}</p>
</div>'''

cs_html = []
for i, c in enumerate(CS):
    exps = "".join(f'<a class="xtag" href="#map-{EXP_ID[e]}" data-open="map-{EXP_ID[e]}"><b>{EXP_ID[e]}</b> {esc(e)}</a>' for e in c["exps"])
    ul_label = c["user"]
    emo = "".join(f'<li><span class="estage">{s}</span><p>{esc(t[0].upper() + t[1:])}</p></li>' for s, t in c["emotion"])
    ids = "".join(f'<a class="sref chipid" href="#{x}" data-row="{x}">{x}</a>' for x in c["idlist"])
    cs_html.append(f'''<article class="cscard cs{i+1}" id="{c["id"]}">
  <header class="cshead">
    <span class="csnum">{c["id"]}</span>
    <div class="cstitle"><span class="eyebrow">Consolidated Scenario {c["id"][2:]}</span><h3>{esc(c["title"])}</h3>
      <div class="csmeta"><span class="chip tier-{c["tier"].lower()}">({esc(ul_label)} – {c["tier"]})</span></div></div>
  </header>
  <div class="csbody">
    <div class="block"><h4 class="bk">Experiences covered</h4><div class="xtags">{exps}</div></div>
    <div class="cols">
      <div class="block"><h4 class="bk">Context</h4><p>{esc(c["context"])}</p></div>
      <div class="block goal"><h4 class="bk">Goal &amp; Metrics</h4><p><strong>Goal:</strong> {esc(c["goal"])}</p>
        <ul class="metrics">{"".join(f"<li>{esc(m)}</li>" for m in c["metrics"])}</ul></div>
    </div>
    <div class="block"><h4 class="bk">Action</h4><ol class="steps">{"".join(f"<li>{link_ids(a)}</li>" for a in c["actions"])}</ol></div>
    <div class="block"><h4 class="bk">User Emotion</h4><ol class="emotion">{emo}</ol></div>
    <div class="block"><h4 class="bk">Scenario IDs consolidated <span class="muted">(all P1 · {len(c["idlist"])} scenarios)</span></h4><div class="ids">{ids}</div></div>
  </div>
</article>''')

page = (HERE / "template.html").read_text()
for k, v in {
    **sitekit.common("map"),
    "PAGER": sitekit.pager("map", "brief", "Background, Goal, Problems, Outcomes, Scope, Stakeholders, Timeline, Artifacts and Learnings."),
    "BRIEFHREF": sitekit.href("map", "brief"), "USERS": "\n".join(user_html), "EXPROWS": "\n".join(exp_rows), "NEXP": str(len(EXPERIENCES)),
    "STATS": stats, "DEFS": defs, "FILTERS": filters, "GROUPS": "\n".join(groups),
    "COVERAGE": coverage, "CS": "\n".join(cs_html), "TOTAL": str(len(rows)),
}.items():
    page = page.replace("{{" + k + "}}", v)
sitekit.write("map", page)
