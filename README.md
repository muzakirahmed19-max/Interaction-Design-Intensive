# Interaction Design Intensive: Assignment A

Interactive submission site for a B2B team resource allocation platform for Nimbus Labs.

**Muzakir Ahmed** · MDes in User Experience and AI-2026 · O.P. Jindal Global University

## Pages
| Part | Page | Path |
|---|---|---|
| 1 | Design Brief (BG POSSTAL): Background, Goal, Problems, Outcomes, Scope, Stakeholders, Timeline, Artifacts, Learnings | `/` (`index.html`) |
| 2 | Scenario Map: users and key tasks, major experiences, prioritized scenario map, consolidated scenarios | `/scenario-map/` (`scenario-map/index.html`) |

Both pages share a site bar with Part 1 / Part 2 tabs, a "Next / Previous" card at the end, and one stylesheet. Links between pages are relative, so the site works on Vercel and on GitHub Pages.

Live: https://interaction-design-intensive.vercel.app and https://muzakirahmed19-max.github.io/Interaction-Design-Intensive/

## Source
```
src/
  build.py               builds both pages
  shared/                head.html, shared.css, logo.png, sitekit.py (site bar, pager, page wrapper)
  design-brief/          template.html + build.py (problem, outcome and timeline content)
  scenario-map/          template.html + data.py (verbatim content) + build.py
```
Run `python3 src/build.py` after any change, then commit the regenerated `index.html` and `scenario-map/index.html`. The pages are plain static HTML, so hosting needs no build step.

AI interactions transcript: https://claude.ai/artifact/NcxexpHQEXEVzk5BGcxWSw
