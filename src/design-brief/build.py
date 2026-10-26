import datetime, html, pathlib, re, sys

HERE = pathlib.Path(__file__).parent  # src/design-brief/; writes ../../index.html
sys.path.insert(0, str(HERE.parent / "shared"))
import sitekit

PEOPLE = {
    "Arjun": "arjun", "Nisha": "nisha", "Individual Contributors": "ic",
    "Delivery Head": "dh", "Admin / Resource Ops": "admin",
    "Leadership": "lead", "Finance": "fin",
}

def esc(s):
    return html.escape(s, quote=False)

def chips(users):
    out, keys, tiers = [], [], set()
    for u in users.split(", "):
        name, tier = u.rsplit(" – ", 1)
        k = PEOPLE[name]
        keys.append(k); tiers.add(tier.lower())
        out.append(f'<span class="chip tier-{tier.lower()}">{esc(name)} – {tier}</span>')
    return "".join(out), " ".join(keys), " ".join(sorted(tiers))

def problem_body(text):
    # split "X, because Y, when Z." into labelled spans, keeping the text verbatim
    i = text.index(", because ")
    j = text.rindex(", when ")
    a, b, c = text[:i + 1], text[i + 2:j + 1], text[j + 2:]
    return (f'<span class="seg seg-what" data-l="Problem">{esc(a)}</span> '
            f'<span class="seg seg-why" data-l="Cause">{esc(b)}</span> '
            f'<span class="seg seg-when" data-l="Context">{esc(c)}</span>')

def outcome_body(text):
    i = text.rindex(", by ")
    a, b = text[:i + 1], text[i + 2:]
    a = re.sub(r"(approximately\s)?(±?\d[\d–.]*\s?%|\d+\s(?:day|days|minutes|hours|weeks))",
               lambda m: f"<strong>{m.group(0)}</strong>", esc(a))
    return (f'<span class="seg seg-target" data-l="Target">{a}</span> '
            f'<span class="seg seg-how" data-l="How">{esc(b)}</span>')

def card(kind, cid, title, users, text, link):
    c, keys, tiers = chips(users)
    body = problem_body(text) if kind == "p" else outcome_body(text)
    ltitle = LOOKUP[link]
    arrow = "Addressed by" if kind == "p" else "Solves"
    return f'''<details class="card" id="{cid}" open data-people="{keys}" data-tiers="{tiers}">
<summary><span class="cid">{cid}</span><span class="ctitle">{esc(title)}</span><span class="chev" aria-hidden="true"></span></summary>
<div class="cbody"><div class="chips">{c}</div><p class="stmt">{body}</p>
<a class="link" href="#{link}" data-target="{link}"><span class="lk">{arrow}</span> <span class="cid">{link}</span> {esc(ltitle)}</a></div>
</details>'''

UP = [
 ("UP1","No cross-team visibility of availability","Arjun – Primary, Nisha – Primary","Managers can't tell who is free or already assigned outside their own team, because availability lives in separate spreadsheets and people's heads with no shared system, when they want to find available people across the organization to staff a project."),
 ("UP2","Unknowingly double-booking people","Arjun – Primary, Nisha – Primary","Managers end up assigning people who are already committed elsewhere, because nothing checks for overlapping allocations or alerts anyone in real time, when they want to allocate a person to a project with confidence that there's no conflict."),
 ("UP3","Misreading how much effort someone can give","Nisha – Primary, Individual Contributors – Secondary","PMs and contributors interpret \"50%\" or \"part-time\" differently, which leads to wrong expectations, because there's no standard unit for effort or capacity, when they want to agree on how many hours a person will give to a project."),
 ("UP4","Working from outdated or conflicting plans","Arjun – Primary, Nisha – Primary","Managers make decisions from stale or conflicting versions of the plan, because spreadsheets don't support several people editing at once and depend on manual updates, when they want to view and update one current allocation plan."),
 ("UP5","Relying on familiar people instead of the right skills","Nisha – Primary, Arjun – Primary","Managers keep going back to the same 2 or 3 people and overlook others who could do the work, because there's no searchable, up-to-date skills directory, when they want to find people with the right skills and proficiency for a project."),
 ("UP6","No view of future availability","Nisha – Primary, Delivery Head – Secondary","Managers find people already booked just as a new project is about to start, because there's no forecast of free capacity by role or skill, when they want to plan staffing for upcoming projects and commit start dates to clients."),
 ("UP7","Time lost chasing allocation updates","Arjun – Primary","Managers spend hours on Slack and in meetings chasing people for updates, because allocation status isn't visible in one place, when they want to monitor team workload and spot overload early."),
 ("UP8","Hidden overload for individuals","Individual Contributors – Secondary","Contributors end up stretched across projects with unclear expectations, because they can't see their total commitments or easily flag overload, when they want to manage their own workload and raise concerns in time."),
]
BP = [
 ("BP1","Missed client deadlines damaging client relationships","Delivery Head – Secondary, Leadership – Tertiary","The company faces SLA penalties, escalations and lower client renewals, because project delivery slips when committed people turn out to be unavailable, when it wants to retain clients and grow existing accounts."),
 ("BP2","Revenue loss from unbilled capacity","Finance – Tertiary, Leadership – Tertiary","The company carries salary costs for capacity that never turns into billable work, which erodes margins, because staffing decisions are made without an organization-wide picture of who can be billed, when it wants to maximize revenue per employee."),
 ("BP3","Inaccurate revenue and capacity forecasting","Finance – Tertiary, Leadership – Tertiary","The company can't reliably predict quarterly revenue or decide whether to take on new work, because there's no dependable data on future capacity and committed allocations, when it wants to plan finances and growth each quarter."),
 ("BP4","Lost or delayed new business","Delivery Head – Secondary","The company loses deals or overpromises start dates it can't staff, because sales and delivery can't confirm upcoming capacity by skill, when it wants to win new client work quickly and reliably."),
 ("BP5","Cost of attrition and burnout","Leadership – Tertiary","The company loses high-demand specialists and pays the cost of hiring and ramping up replacements, because workload isn't spread evenly across the workforce, when it wants to retain talent and protect delivery continuity."),
 ("BP6","Growing cost of managing resources as the company grows","Leadership – Tertiary, Admin / Resource Ops – Secondary","The company spends more and more on coordinating people every time it adds new projects, which reduces profit, because resource planning is done manually and doesn't scale, when it wants to take on more projects without increasing management costs."),
 ("BP7","Poor strategic workforce decisions","Leadership – Tertiary","The company hires late or for the wrong skills, keeps excess bench, or misprices projects, because leadership lacks reliable data on skill supply, demand and utilization trends, when it wants to make informed decisions about hiring, pricing and capacity investment."),
]
UO = [
 ("UO1","Instant cross-team visibility","Arjun – Primary, Nisha – Primary","Reduce the time to find an available person across the organization from approximately 1 day of asking around to under 10 minutes, by giving everyone one shared, real-time view of people's availability and allocations."),
 ("UO2","Conflict-free allocations","Arjun – Primary, Nisha – Primary","Flag 100% of allocation conflicts before an allocation is confirmed, by detecting overlapping commitments in real time and warning managers at the moment of assignment."),
 ("UO3","Shared understanding of effort","Nisha – Primary, Individual Contributors – Secondary","Record 100% of allocations in hours per week, with no free-text effort terms, by standardizing effort as hours against a 40-hour week and showing each person's remaining capacity."),
 ("UO4","One trusted, current plan","Arjun – Primary, Nisha – Primary","Retire 100% of spreadsheet trackers for active projects and update 95% of allocations within 24 hours of a change, by keeping one shared plan that several managers can edit, with live updates and a visible record of changes."),
 ("UO5","Skill-based staffing","Nisha – Primary, Arjun – Primary","Increase the share of the workforce allocated to at least one project from approximately 65% to 85%, and reduce reliance on the same \"go-to\" people by approximately 40%, by making people's skills and proficiency levels searchable when staffing a project."),
 ("UO6","Proactive forward planning","Nisha – Primary, Delivery Head – Secondary","Increase the share of projects staffed at least 4 weeks before they start from approximately 20% to 60%, by forecasting free capacity by role and skill for the coming weeks and months."),
 ("UO7","Less time chasing updates","Arjun – Primary","Reduce the time managers spend tracking allocation status by 50%, approximately 4 hours saved per manager per week, by making team workload and utilization visible at a glance in one place."),
 ("UO8","Visible and manageable personal workload","Individual Contributors – Secondary","Reduce the number of people allocated above 100% for 2 or more consecutive weeks to near zero, and make sure 90% of contributors can see their total commitments, by giving each person visibility of their own allocations and a simple way to flag overload."),
]
BO = [
 ("BO1","On-time client delivery","Delivery Head – Secondary, Leadership – Tertiary","Increase on-time project delivery from approximately 70% to 90%, and reduce client escalations by approximately 50%, by preventing overcommitment of people across projects."),
 ("BO2","Higher billable utilization","Finance – Tertiary, Leadership – Tertiary","Increase billable utilization from approximately 65% to 80%, and reduce non-billable bench cost by approximately 30%, by making unbilled capacity visible when work is staffed."),
 ("BO3","Reliable revenue forecasting","Finance – Tertiary, Leadership – Tertiary","Improve the accuracy of quarterly revenue forecasts to within ±10% of actuals, by basing forecasts on live allocation and capacity data."),
 ("BO4","Faster and reliable client commitments","Delivery Head – Secondary","Reduce the time to confirm staffing for a new client request from approximately 5 days to under 2 days, and meet 90% of committed start dates, by giving delivery reliable insight into upcoming capacity by skill."),
 ("BO5","Lower attrition cost","Leadership – Tertiary","Reduce voluntary attrition among high-demand specialists by approximately 20% within a year, by spreading work evenly and catching sustained overload early."),
 ("BO6","Lower cost of managing resources per project","Leadership – Tertiary, Admin / Resource Ops – Secondary","Reduce the resource coordination effort per project by approximately 40%, so that management costs don't rise as the company takes on more projects, by making resource planning a shared, self-serve process."),
 ("BO7","Data-driven workforce strategy","Leadership – Tertiary","Base 100% of quarterly hiring and pricing decisions on actual skill demand and utilization data, by making organization-wide trends in capacity and skill gaps available to leadership."),
]
LOOKUP = {r[0]: r[1] for r in UP + BP + UO + BO}
pair = lambda cid: cid.replace("UP", "UO").replace("BP", "BO") if cid[1] == "P" else cid.replace("UO", "UP").replace("BO", "BP")
cards = lambda rows, kind: "\n".join(card(kind, r[0], r[1], r[2], r[3], pair(r[0])) for r in rows)

TL = [
 ("1. Design Definition", 1, [
  ("Define Design Briefs (document problems and outcomes clearly)","Sun, 25 Oct 2026","Done","Started 21 Oct. All sections are done except Learnings, which will be added later."),
  ("Internal Review of Design Briefs","Mon, 26 Oct 2026","Not started","Internal alignment before the client presentation."),
  ("Client Review Meeting for Design Briefs","Mon, 26 Oct 2026","Not started","The Head of Delivery Operations (Approver) should attend."),
  ("Implement Client Feedback on Design Briefs","Tue, 27 Oct 2026","Not started","Document changes and rationale.")]),
 ("2. Scenario Planning & Refinement", 2, [
  ("Define All Possible Scenarios & Propose Prioritized Scenarios","Mon, 26 Oct 2026","Done","Main, edge, special, error and external scenarios, with CRUD and MVP tags."),
  ("Client Presentation & Review Meeting for Scenarios","Tue, 27 Oct 2026","Not started","Key client decision-makers should attend."),
  ("Implement Client Feedback on Scenarios","Tue, 27 Oct 2026","Not started","Document changes and rationale."),
  ("Internal Review of Implemented Scenario Feedback","Tue, 27 Oct 2026","Not started","Make sure the feedback was incorporated accurately."),
  ("Client Confirmatory Review Meeting","Tue, 27 Oct 2026","Not started","A quick review to confirm the changes."),
  ("Implement Final Adjustments to Scenarios","Tue, 27 Oct 2026","Not started","Consolidated scenarios are finalized.")]),
 ("3. Workflow Design", 3, [
  ("Design Workflows (ideal paths, edge cases, measurement criteria)","Thu, 29 Oct 2026","Not started","3-day phase (28 to 30 Oct)."),
  ("Internal Review of Workflows","Thu, 29 Oct 2026","Not started",""),
  ("Client Review Meeting for Workflows","Fri, 30 Oct 2026","Not started","Key client decision-makers should attend."),
  ("Implement Client Feedback & Share Updated Workflows","Fri, 30 Oct 2026","Not started","Document changes and rationale.")]),
 ("4. Ideation & Lo-Fi", 4, [
  ("Create Low-Fidelity Hand-Drawn Sketches (variety of ideas, converge 2–3)","Sun, 1 Nov 2026","Not started","3-day phase (31 Oct to 2 Nov)."),
  ("Internal Review of Lo-Fi Sketches","Sun, 1 Nov 2026","Not started",""),
  ("Client Review Meeting for Lo-Fi Sketches","Mon, 2 Nov 2026","Not started","Key client decision-makers should attend."),
  ("Implement Client Feedback on Lo-Fi Sketches","Mon, 2 Nov 2026","Not started","Refine and document the changes.")]),
 ("5. Wireframing & IxD", 5, [
  ("Create Digital Wireframes (functionality and content design)","Thu, 12 Nov 2026","Not started","2-week phase (3 to 16 Nov). Desktop-first."),
  ("Internal Review of Digital Wireframes","Fri, 13 Nov 2026","Not started",""),
  ("Client Review Meeting for Digital Wireframes","Sat, 14 Nov 2026","Not started","Key client decision-makers should attend."),
  ("Implement Client Feedback on Digital Wireframes","Sun, 15 Nov 2026","Not started","Document changes and rationale."),
  ("Final Interaction Design (IxD) Sign-off","Mon, 16 Nov 2026","Not started","Assignment deadline. Official approval from the Approver.")]),
]
rows = []
for cat, n, tasks in TL:
    for k, (task, date, status, note) in enumerate(tasks):
        st = {"Done": "done", "In progress": "prog"}.get(status, "todo")
        catcell = f'<td class="tcat" rowspan="{len(tasks)}"><span class="pdot p{n}"></span>{esc(cat)}</td>' if k == 0 else ""
        rows.append(f'<tr data-phase="{n}"{" class=first" if k == 0 else ""}>{catcell}<td>{esc(task)}</td><td class="tdate">{date}</td><td><span class="status {st}">{status}</span></td><td class="tnote">{esc(note)}</td></tr>')
timeline_rows = "\n".join(rows)

# Gantt: day 0 = 21 Oct, day 26 = 16 Nov (27 days)
SPAN = 27
GANTT = [(1,"Design Definition",0,6,"21–27 Oct"),(2,"Scenario Planning & Refinement",5,6,"26–27 Oct"),
         (3,"Workflow Design",7,9,"28–30 Oct"),(4,"Ideation & Lo-Fi",10,12,"31 Oct–2 Nov"),(5,"Wireframing & IxD",13,26,"3–16 Nov")]
gantt = "\n".join(
    f'<button class="grow" type="button" data-phase="{n}" aria-pressed="false"><span class="glabel"><span class="pdot p{n}"></span>{n}. {esc(name)}<span class="gdate">{d}</span></span>'
    f'<span class="gtrack"><span class="gbar p{n}" style="left:{s/SPAN*100:.3f}%;width:{(e-s+1)/SPAN*100:.3f}%"></span></span></button>'
    for n, name, s, e, d in GANTT)
# "Today" marker follows the build date, clamped to the timeline
START = datetime.date(2026, 10, 21)
today_d = min(max(datetime.date.today(), START), START + datetime.timedelta(days=SPAN - 1))
today = ((today_d - START).days + 0.5) / SPAN * 100
today_label = f"{today_d.day} {today_d:%b}"
ticks = "".join(f'<span style="left:{d/SPAN*100:.3f}%">{l}</span>' for d, l in [(0,"21 Oct"),(7,"28 Oct"),(14,"4 Nov"),(21,"11 Nov"),(26,"16 Nov")])

page = (HERE / "template.html").read_text()
for k, v in {
    **sitekit.common("brief"),
    "PAGER": sitekit.pager("brief", "map", "Users and key tasks, 11 experiences, 157 prioritized scenarios and 4 consolidated scenarios."),
    "TODAYLABEL": today_label, "UP": cards(UP, "p"), "BP": cards(BP, "p"), "UO": cards(UO, "o"), "BO": cards(BO, "o"),
    "TLROWS": timeline_rows, "GANTT": gantt, "TODAY": f"{today:.3f}", "TICKS": ticks,
}.items():
    page = page.replace("{{" + k + "}}", v)
sitekit.write("brief", page)
