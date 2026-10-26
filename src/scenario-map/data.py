# Verbatim content from the FINAL project-chat messages (Step 1, Step 2, Step 4 tables, consolidated scenarios).

USERS = [
 ("Primary", "Arjun", "Engineering Manager", "A", [
  "Check who in his team and across other teams is free, partly free or fully booked",
  "Allocate engineers to projects in hours per week, and edit, extend or remove allocations",
  "Resolve conflicts when someone is overbooked",
  "Monitor team workload and utilization, and spot overload or underuse early",
  "Rebalance work when priorities or people change"]),
 ("Primary", "Nisha", "Project Manager", "N", [
  "Find people by skill, proficiency, role and availability for a project",
  "Request or allocate people to her project for a defined period",
  "Forecast free capacity by role and skill for upcoming projects",
  "Track her project's staffing and fill gaps when someone leaves or goes on leave",
  "Agree effort in hours per week with managers and contributors"]),
 ("Secondary", "Individual Contributors", "designers, developers, QA and DevOps", "IC", [
  "View their own allocations and total weekly commitments",
  "Keep their skills, proficiency levels and availability up to date",
  "Flag overload or raise concerns about their allocations",
  "Check upcoming leave, which is synced from the timesheet system"]),
 ("Secondary", "Delivery Head / Account Manager", "", "DH", [
  "Raise staffing requests for new or expanding client engagements",
  "Check whether people with the right skills are available before committing start dates",
  "Track the status of their requests until staffing is confirmed"]),
 ("Secondary", "Admin / Resource Ops", "", "AD", [
  "Add, edit and deactivate people, roles and projects",
  "Manage permissions for each user type",
  "Maintain the skills list and effort standards",
  "Monitor the timesheet leave sync and Slack integrations"]),
 ("Tertiary", "Leadership", "CTO / COO, read-only", "L", [
  "View organization-wide utilization, bench strength and capacity trends",
  "Identify skill gaps and delivery risk for strategic decisions"]),
 ("Tertiary", "Finance", "read-only", "F", [
  "View billable vs non-billable utilization",
  "Use capacity and allocation data for revenue forecasting and project costing"]),
]

EXPERIENCES = [
 ("E1", "Viewing availability", "Arjun, Nisha, Delivery Head", "See who is free, partly free or fully booked across the organization", "Faster staffing, with less time lost asking around (UO1)"),
 ("E2", "Finding people by skill", "Nisha, Arjun, Delivery Head", "Find people with the right skill and proficiency for a project", "Better use of underused talent and higher billable utilization (UO5, BO2)"),
 ("E3", "Allocating people to projects", "Arjun, Nisha", "Assign, edit, extend or remove a person's allocation in hours per week", "One trusted plan instead of scattered spreadsheets (UO3, UO4)"),
 ("E4", "Managing conflicts", "Arjun, Nisha, Individual Contributors", "Catch and resolve overbooking before it is confirmed", "Fewer delivery slips and client escalations (UO2, BO1)"),
 ("E5", "Forecasting capacity", "Nisha, Delivery Head, Leadership", "See free capacity by role and skill for upcoming weeks and months", "Projects staffed ahead of time, and reliable start dates (UO6, BO4)"),
 ("E6", "Monitoring team workload", "Arjun, Nisha", "Track utilization and spot overload or underuse early", "Less time chasing updates, and less burnout (UO7, BO5)"),
 ("E7", "Managing my profile and allocations", "Individual Contributors", "Keep skills current, see total commitments and flag overload", "Accurate skills data, and lower attrition risk (UO8, BO5)"),
 ("E8", "Raising staffing requests", "Delivery Head, Nisha", "Request people for a new or expanding engagement and track the request", "Faster, reliable client commitments (BO4)"),
 ("E9", "Setting up and administering the platform", "Admin / Resource Ops", "Manage people, roles, permissions, projects, the skills list and integrations", "Clean, consistent data, with lower coordination cost per project (BO6)"),
 ("E10", "Viewing organization-wide utilization", "Leadership, Finance", "See utilization, bench and capacity trends across the organization, read-only", "Accurate revenue forecasting and data-driven hiring and pricing (BO3, BO7)"),
 ("E11", "Onboarding and first-time setup", "Arjun, Nisha, Individual Contributors, Delivery Head, Admin, Leadership, Finance", "Log in for the first time, complete a profile and understand hours-based effort and their role's permissions", "Faster adoption and complete data from day one, which helps retire spreadsheets (UO4, BO6)"),
]

PRIORITY_DEFS = [
 ("P1", "MVP", "The core loop of seeing availability, finding people, allocating them, catching conflicts, keeping profiles current and the basic admin setup."),
 ("P2", "Expansion", "This adds forecasting, staffing requests, workload alerts and org-wide utilization, which together should deliver most (80–90%) of the user and business outcomes."),
 ("P3", "Add-on", "These are conveniences on top of existing scenarios."),
]

MAP = """
| S1 | Viewing availability | Arjun | Checks who in his team and other teams is free next week | Best case | Main | Read | P1 |
| S2 | Viewing availability | Nisha | Views one person's availability across all their projects for the next month | Best case | Main | Read | P1 |
| S3 | Viewing availability | Nisha | Sees partial availability, e.g. 12 of 40 hrs free | Best case | Main | Read | P1 |
| S4 | Viewing availability | Arjun | Sees leave and public holidays reflected in availability | Best case | Main | Read | P1 |
| S5 | Viewing availability | Individual Contributor | Views own availability for the next 4 weeks | Best case | Main | Read | P1 |
| S6 | Viewing availability | Delivery Head | Filters availability by date range and location | Feature | Main | Read | P2 |
| S7 | Viewing availability | Delivery Head | Filters by role, team, skill and billable status | Feature | Main | Read | P2 |
| S8 | Viewing availability | Arjun | Views team availability in a week or month calendar view | Feature | Main | Read | P2 |
| S9 | Viewing availability | Arjun | Nobody with the needed role is free in the selected period | Edge | Atypical | Read | P1 |
| S10 | Viewing availability | Nisha | Person shows as free but is doing unrecorded internal work | Edge | Atypical | Read | P3 |
| S11 | Viewing availability | Arjun | Views a part-time employee on a 20-hr contract | Edge | Atypical | Read | P1 |
| S12 | Viewing availability | Nisha | Leave sync from the timesheet system fails, so availability may be stale | Edge | External | Read | P2 |
| S13 | Viewing availability | Arjun | People in another region have different holidays | Edge | External | Read | P2 |
| S14 | Viewing availability | Nisha | The org-wide view loads slowly or only partly | Edge | External | Read | P3 |
| S15 | Finding people by skill | Nisha | Searches for "React, Senior, 20 hrs/week free from 1 Dec" | Best case | Main | Read | P1 |
| S16 | Finding people by skill | Arjun | Opens a person's full profile: skills, proficiency, past projects | Best case | Main | Read | P1 |
| S17 | Finding people by skill | Arjun | Compares 2–3 candidates side by side | Feature | Main | Read | P3 |
| S18 | Finding people by skill | Nisha | Filters by several skills at once | Feature | Main | Read | P2 |
| S19 | Finding people by skill | Nisha | Sorts results by best match or most availability | Feature | Main | Read | P2 |
| S20 | Finding people by skill | Nisha | Shortlists candidates for a project | Feature | Main | Create | P2 |
| S21 | Finding people by skill | Nisha | Removes someone from the shortlist | Feature | Main | Delete | P2 |
| S22 | Finding people by skill | Delivery Head | Saves a search to reuse for a recurring client need | Feature | Main | Create | P3 |
| S23 | Finding people by skill | Delivery Head | Deletes a saved search | Feature | Main | Delete | P3 |
| S24 | Finding people by skill | Nisha | Search returns no results for a rare skill | Edge | Atypical | Read | P1 |
| S25 | Finding people by skill | Nisha | Finds a match whose skill profile is over 6 months old | Edge | Atypical | Read | P2 |
| S26 | Finding people by skill | Nisha | Searches with a typo or synonym, e.g. "JS" vs "JavaScript" | Edge | Atypical | Read | P2 |
| S27 | Finding people by skill | Nisha | A skill match is on leave during the project | Edge | Atypical | Read | P2 |
| S28 | Finding people by skill | Arjun | A common skill returns too many results | Edge | Atypical | Read | P3 |
| S29 | Allocating people to projects | Arjun | Allocates an engineer at 20 hrs/week for 6 weeks | Best case | Main | Create | P1 |
| S30 | Allocating people to projects | Nisha | Extends an allocation by 2 weeks when the project slips | Best case | Main | Update | P1 |
| S31 | Allocating people to projects | Arjun | Reduces someone's hours from 30 to 15 per week | Best case | Main | Update | P1 |
| S32 | Allocating people to projects | Nisha | Removes a person when the project ends early | Best case | Main | Delete | P1 |
| S33 | Allocating people to projects | Individual Contributor | Is notified of a new allocation | Best case | Main | Read | P1 |
| S34 | Allocating people to projects | Arjun | Allocates several people to one project at once | Feature | Main | Create | P2 |
| S35 | Allocating people to projects | Nisha | Allocates with varying hours, e.g. ramping up from 10 to 30 hrs/week | Feature | Main | Create | P2 |
| S36 | Allocating people to projects | Arjun | Makes a tentative allocation, then confirms it | Feature | Main | Update | P2 |
| S37 | Allocating people to projects | Arjun | Reassigns an allocation to another person | Feature | Main | Update | P2 |
| S38 | Allocating people to projects | Nisha | Views an allocation's change history | Feature | Main | Read | P3 |
| S39 | Allocating people to projects | Arjun | Undoes an allocation he just removed | Feature | Main | Update | P3 |
| S40 | Allocating people to projects | Nisha | Two managers edit the same allocation at the same time | Edge | Atypical | Update | P2 |
| S41 | Allocating people to projects | Nisha | Allocates to a project with no end date set | Edge | Atypical | Create | P2 |
| S42 | Allocating people to projects | Nisha | Allocating someone from another manager's team needs that manager's approval | Edge | Atypical | Create | P2 |
| S43 | Allocating people to projects | Arjun | Enters 0 hrs or more than 40 hrs by mistake | Edge | Atypical | Create | P1 |
| S44 | Allocating people to projects | Arjun | Internet drops while saving an allocation | Edge | External | Create | P2 |
| S45 | Allocating people to projects | Nisha | The client puts the project on hold, so allocations are paused | Edge | External | Update | P2 |
| S46 | Allocating people to projects | Nisha | Her project overruns its deadline, but some of its people are booked on another project starting tomorrow, so the overlap is flagged | Edge | Atypical | Read | P1 |
| S47 | Allocating people to projects | Arjun | Resolves the overrun overlap by splitting hours, swapping someone in or moving the new project's start | Edge | Atypical | Update | P1 |
| S48 | Allocating people to projects | Nisha | Extends allocations for an overrunning project and sees who can and can't stay on | Best case | Main | Update | P1 |
| S49 | Allocating people to projects | Arjun | Allocates someone serving notice and sees a "Notice period, last working day" tag with the date | Edge | Atypical | Read | P2 |
| S50 | Allocating people to projects | Nisha | Tries to allocate someone past their last working day, and is warned and offered a replacement or handover | Edge | Atypical | Create | P2 |
| S51 | Managing conflicts | Arjun | Gets a warning that an allocation pushes someone to 50 hrs/week, and adjusts hours | Best case | Main | Update | P1 |
| S52 | Managing conflicts | Arjun | Views all open conflicts in one list | Best case | Main | Read | P1 |
| S53 | Managing conflicts | Arjun | Splits hours between two projects to resolve a conflict | Best case | Main | Update | P1 |
| S54 | Managing conflicts | Nisha | Shifts allocation dates to avoid an overlap | Best case | Main | Update | P1 |
| S55 | Managing conflicts | Nisha | Resolves a conflict by suggesting another available person | Best case | Main | Update | P2 |
| S56 | Managing conflicts | Arjun | Removes one of the conflicting allocations | Best case | Main | Delete | P1 |
| S57 | Managing conflicts | Arjun | The other manager involved is notified of the conflict | Best case | Main | Read | P1 |
| S58 | Managing conflicts | Individual Contributor | Is notified on Slack that they've been double-booked | Best case | Main | Read | P2 |
| S59 | Managing conflicts | Arjun | Overrides a conflict with a reason, e.g. a 1-week crunch | Feature | Atypical | Create | P2 |
| S60 | Managing conflicts | Delivery Head | Two high-priority client projects clash, so the conflict is escalated | Edge | Atypical | Update | P2 |
| S61 | Managing conflicts | Individual Contributor | Disagrees with how a conflict was resolved | Edge | Atypical | Create | P3 |
| S62 | Managing conflicts | Nisha | A newly synced leave conflicts with a confirmed allocation | Edge | External | Update | P2 |
| S63 | Managing conflicts | Arjun | A change to the public holiday calendar creates new conflicts | Edge | External | Update | P3 |
| S64 | Forecasting capacity | Nisha | Views free capacity by role and skill for the next 3 months | Best case | Main | Read | P2 |
| S65 | Forecasting capacity | Delivery Head | Checks whether 2 QA engineers are free from a client's start date | Best case | Main | Read | P2 |
| S66 | Forecasting capacity | Delivery Head | Sees when a specific person rolls off their project | Best case | Main | Read | P2 |
| S67 | Forecasting capacity | Nisha | Deletes a tentative booking when the project doesn't happen | Best case | Main | Delete | P2 |
| S68 | Forecasting capacity | Leadership | Views forecasted skill shortages and demand vs supply by skill | Feature | Main | Read | P2 |
| S69 | Forecasting capacity | Nisha | Adds a tentative (soft) booking to see its impact on capacity | Feature | Main | Create | P2 |
| S70 | Forecasting capacity | Nisha | A forecast 6+ months out has very little data | Edge | Atypical | Read | P3 |
| S71 | Forecasting capacity | Delivery Head | Many overlapping tentative bookings make the forecast unreliable | Edge | Atypical | Read | P3 |
| S72 | Forecasting capacity | Delivery Head | The forecast changes suddenly after a large project is cancelled | Edge | External | Read | P2 |
| S73 | Forecasting capacity | Leadership | Unplanned resignations reduce future capacity | Edge | External | Read | P2 |
| S74 | Forecasting capacity | Finance | Views how many people are free next week, next month, next quarter or for custom dates, to plan projects | Best case | Main | Read | P2 |
| S75 | Forecasting capacity | Finance | Breaks free headcount down by role and skill, excluding people whose notice period ends | Feature | Main | Read | P2 |
| S76 | Forecasting capacity | Delivery Head | Enters a new project's needs (e.g. 3 UX Designers, 5 Developers, 3 QA) and sees the ideal start date when the full team is free | Best case | Main | Read | P2 |
| S77 | Forecasting capacity | Nisha | Compares 2–3 suggested start dates and how many needed people are free for each | Feature | Main | Read | P3 |
| S78 | Forecasting capacity | Delivery Head | Saves a suggested start date as a tentative booking for the needed people | Feature | Main | Create | P3 |
| S79 | Forecasting capacity | Leadership | No date within 6 months covers the full team, so the platform shows which roles are short and by how many | Edge | Atypical | Read | P2 |
| S80 | Monitoring team workload | Arjun | Checks weekly team utilization and spots someone at 120% | Best case | Main | Read | P1 |
| S81 | Monitoring team workload | Arjun | Spots underused people, e.g. below 50% | Best case | Main | Read | P1 |
| S82 | Monitoring team workload | Arjun | Rebalances work from an overloaded engineer to an underused one | Best case | Main | Update | P1 |
| S83 | Monitoring team workload | Arjun | Responds to an overload flag from a contributor | Best case | Main | Update | P2 |
| S84 | Monitoring team workload | Nisha | Views workload for her project team only | Best case | Main | Read | P1 |
| S85 | Monitoring team workload | Nisha | Gets an alert when someone stays above 100% for 2 or more weeks | Feature | Main | Read | P2 |
| S86 | Monitoring team workload | Arjun | Drills down from the team view to one person's weekly breakdown | Feature | Main | Read | P2 |
| S87 | Monitoring team workload | Arjun | Sets the utilization threshold for alerts | Feature | Main | Update | P3 |
| S88 | Monitoring team workload | Arjun | Dismisses or snoozes an alert | Feature | Main | Update | P3 |
| S89 | Monitoring team workload | Arjun | The whole team is overloaded, so there's nobody to rebalance to | Edge | Atypical | Read | P2 |
| S90 | Monitoring team workload | Arjun | Takes over a team from another manager | Edge | Atypical | Update | P2 |
| S91 | Monitoring team workload | Arjun | A team member goes on sudden sick leave and their work needs cover | Edge | External | Update | P2 |
| S92 | Managing my profile and allocations | Individual Contributor | Views total weekly commitments across all projects | Best case | Main | Read | P1 |
| S93 | Managing my profile and allocations | Individual Contributor | Views upcoming allocations with project details and managers | Best case | Main | Read | P1 |
| S94 | Managing my profile and allocations | Individual Contributor | Adds a new skill and proficiency level after a certification | Best case | Main | Create | P1 |
| S95 | Managing my profile and allocations | Individual Contributor | Updates the proficiency level of an existing skill | Best case | Main | Update | P1 |
| S96 | Managing my profile and allocations | Individual Contributor | Removes an outdated skill | Best case | Main | Delete | P1 |
| S97 | Managing my profile and allocations | Individual Contributor | Updates availability, e.g. moving to reduced hours | Best case | Main | Update | P1 |
| S98 | Managing my profile and allocations | Individual Contributor | Spots a wrong or missing allocation and requests a correction | Best case | Main | Create | P2 |
| S99 | Managing my profile and allocations | Individual Contributor | Flags overload with a short note to their manager | Feature | Main | Create | P2 |
| S100 | Managing my profile and allocations | Individual Contributor | Withdraws an overload flag once it's resolved | Feature | Main | Delete | P3 |
| S101 | Managing my profile and allocations | Individual Contributor | Sets notification preferences (Slack or in-app) | Feature | Main | Update | P3 |
| S102 | Managing my profile and allocations | Individual Contributor | Their manager doesn't respond to an overload flag | Edge | Atypical | Read | P3 |
| S103 | Managing my profile and allocations | Individual Contributor | Works for two managers and sees allocations from both | Edge | Atypical | Read | P1 |
| S104 | Raising staffing requests | Delivery Head | Raises a request for 3 developers for a new client from 1 Dec | Best case | Main | Create | P2 |
| S105 | Raising staffing requests | Delivery Head | Adds skills, hours, dates and priority to a request | Best case | Main | Create | P2 |
| S106 | Raising staffing requests | Delivery Head | Checks feasibility before submitting a request | Best case | Main | Read | P2 |
| S107 | Raising staffing requests | Delivery Head | Tracks request status (open, partly filled, confirmed) | Best case | Main | Read | P2 |
| S108 | Raising staffing requests | Delivery Head | Is notified when a request is filled | Best case | Main | Read | P2 |
| S109 | Raising staffing requests | Nisha | Receives and accepts a request | Best case | Main | Update | P2 |
| S110 | Raising staffing requests | Nisha | Fulfils a request by allocating matching people | Best case | Main | Update | P2 |
| S111 | Raising staffing requests | Arjun | Declines a request or proposes another person or date | Best case | Main | Update | P2 |
| S112 | Raising staffing requests | Delivery Head | Edits the request when the client changes scope | Best case | Main | Update | P2 |
| S113 | Raising staffing requests | Delivery Head | Withdraws the request when the deal is lost | Best case | Main | Delete | P2 |
| S114 | Raising staffing requests | Delivery Head | Duplicates a past request | Feature | Main | Create | P3 |
| S115 | Raising staffing requests | Delivery Head | The request can't be fully staffed by the start date | Edge | Atypical | Read | P2 |
| S116 | Raising staffing requests | Delivery Head | Duplicate requests are raised for the same client | Edge | Atypical | Create | P3 |
| S117 | Raising staffing requests | Delivery Head | Raises an urgent request starting in 2 days | Edge | Atypical | Create | P2 |
| S118 | Raising staffing requests | Delivery Head | The client delays the start date after staffing is confirmed | Edge | External | Update | P2 |
| S119 | Setting up and administering the platform | Admin | Adds a new joiner with role, team and permissions | Best case | Main | Create | P1 |
| S120 | Setting up and administering the platform | Admin | Edits a person's role, team or manager | Best case | Main | Update | P1 |
| S121 | Setting up and administering the platform | Admin | Assigns or changes permissions for each role | Best case | Main | Update | P1 |
| S122 | Setting up and administering the platform | Admin | Creates a new project with dates and manager | Best case | Main | Create | P1 |
| S123 | Setting up and administering the platform | Admin | Archives a completed project | Best case | Main | Delete | P1 |
| S124 | Setting up and administering the platform | Admin | Adds a new skill to the list | Best case | Main | Create | P1 |
| S125 | Setting up and administering the platform | Admin | Edits the skills list, e.g. merges "ReactJS" and "React" | Best case | Main | Update | P2 |
| S126 | Setting up and administering the platform | Admin | Removes an unused skill | Best case | Main | Delete | P2 |
| S127 | Setting up and administering the platform | Admin | Sets standard working hours (40/week) and part-time contracts | Best case | Main | Update | P1 |
| S128 | Setting up and administering the platform | Admin | Marks a person as serving notice and records their last working day | Best case | Main | Update | P2 |
| S129 | Setting up and administering the platform | Admin | Imports people and allocations in bulk from existing spreadsheets | Feature | Main | Create | P1 |
| S130 | Setting up and administering the platform | Admin | Views an audit log of changes | Feature | Main | Read | P2 |
| S131 | Setting up and administering the platform | Admin | Deactivates a person who has left, with future allocations still open | Edge | Atypical | Delete | P1 |
| S132 | Setting up and administering the platform | Admin | The bulk import file has errors or duplicates | Edge | Atypical | Create | P1 |
| S133 | Setting up and administering the platform | Admin | Tries to delete a skill that is used in people's profiles | Edge | Atypical | Delete | P2 |
| S134 | Setting up and administering the platform | Admin | Accidentally removes their own admin rights | Edge | Atypical | Update | P3 |
| S135 | Setting up and administering the platform | Admin | The Slack or timesheet integration disconnects | Edge | External | Update | P2 |
| S136 | Viewing organization-wide utilization | Leadership | Views monthly utilization, bench strength and capacity trends | Best case | Main | Read | P2 |
| S137 | Viewing organization-wide utilization | Leadership | Views the most over-used and under-used skills | Best case | Main | Read | P2 |
| S138 | Viewing organization-wide utilization | Finance | Views billable vs non-billable utilization by team for the quarter | Best case | Main | Read | P2 |
| S139 | Viewing organization-wide utilization | Finance | Views bench cost from idle hours | Best case | Main | Read | P2 |
| S140 | Viewing organization-wide utilization | Leadership | Compares utilization across two quarters | Feature | Main | Read | P3 |
| S141 | Viewing organization-wide utilization | Leadership | Filters by team, role, project and client | Feature | Main | Read | P2 |
| S142 | Viewing organization-wide utilization | Finance | Exports utilization data for revenue forecasting | Feature | Main | Read | P2 |
| S143 | Viewing organization-wide utilization | Finance | Schedules a monthly utilization report | Feature | Main | Create | P3 |
| S144 | Viewing organization-wide utilization | Leadership | Checks utilization on mobile in the read-only view | Feature | Main | Read | P3 |
| S145 | Viewing organization-wide utilization | Finance | Data is incomplete because some managers haven't updated allocations | Edge | Atypical | Read | P2 |
| S146 | Viewing organization-wide utilization | Leadership | Tries to edit data and is told the view is read-only | Edge | Atypical | Read | P3 |
| S147 | Viewing organization-wide utilization | Finance | Looks for data from before the platform launched | Edge | Atypical | Read | P3 |
| S148 | Onboarding and first-time setup | Admin | Sends invites to new users | Best case | Main | Create | P1 |
| S149 | Onboarding and first-time setup | Admin | Connects the timesheet system and Slack during first setup | Best case | Main | Create | P2 |
| S150 | Onboarding and first-time setup | Individual Contributor | Logs in for the first time and completes their skill profile | Best case | Main | Create | P1 |
| S151 | Onboarding and first-time setup | Individual Contributor | Confirms auto-synced leave and working hours | Best case | Main | Read | P2 |
| S152 | Onboarding and first-time setup | Arjun | Gets a role-specific walkthrough of hours-based effort and conflict alerts | Best case | Main | Read | P2 |
| S153 | Onboarding and first-time setup | Leadership, Finance | First login lands on the read-only org utilization view | Best case | Main | Read | P2 |
| S154 | Onboarding and first-time setup | Nisha | Skips onboarding and returns to it later | Feature | Main | Update | P3 |
| S155 | Onboarding and first-time setup | Individual Contributor | Leaves their profile half-complete and gets a reminder later | Edge | Atypical | Update | P3 |
| S156 | Onboarding and first-time setup | Nisha | Is given the wrong role on first login | Edge | Atypical | Update | P2 |
| S157 | Onboarding and first-time setup | Individual Contributor | The invite link has expired, or single sign-on fails | Edge | External | Read | P2 |
"""

CS = [
 dict(id="CS1", title="Staffing a new project without double-booking", user="Arjun", tier="Primary",
  exps=["Viewing availability", "Finding people by skill", "Allocating people to projects", "Managing conflicts", "Monitoring team workload"],
  context="It's Monday morning. Arjun has to staff a new client project, \"Atlas\", which starts next Monday and needs 2 backend developers at 20 hrs/week for 6 weeks. His own project \"Orion\" is running a week past its deadline, and two of its developers are already booked on Atlas from tomorrow. Before the platform, he would check 3 spreadsheets and message other managers on Slack, which used to take about half a day.",
  goal="staff Atlas with the right people, without overbooking anyone or delaying Orion.",
  metrics=["Time to staff a project: from approximately 4 hours down to under 30 minutes",
           "Double-bookings confirmed: 0",
           "No one in the team above 100% utilization after allocation",
           "Number of Slack or meeting follow-ups needed to confirm availability: 0"],
  actions=["Arjun opens the availability view and checks who in his team and other teams is free next week. Leave, public holidays and part-time contracts are already reflected, and he can see partial availability such as \"12 of 40 hrs free\" (S1, S3, S4, S11).",
           "Nobody with the backend role is fully free in his own team (S9), so he searches across the organization for \"Node.js, Senior, 20 hrs/week free from next Monday\" (S15). When a rarer skill returns no results, the platform suggests related skills (S24).",
           "He opens the profiles of the two best matches to check their skills, proficiency and past projects (S16).",
           "He allocates both at 20 hrs/week for 6 weeks (S29). He mistypes 200 instead of 20, and the platform stops him with a clear error (S43).",
           "The platform flags that Orion's overrun overlaps with two developers booked on Atlas from tomorrow (S46). He extends their Orion allocations by a week and sees who can and can't stay on (S48).",
           "A warning shows that one developer would reach 50 hrs/week (S51). Arjun opens the conflicts list (S52) and resolves the overlap by splitting her hours: 10 on Orion and 20 on Atlas for that week (S47, S53). He removes the second developer's Orion booking for that week, and the other manager involved is notified (S56, S57).",
           "Each person is notified of their new allocation (S33) and sees their updated weekly total in their own view (S92).",
           "Arjun checks the team utilization view. Nobody is above 100%, and one underused engineer can pick up Orion's remaining work, so he rebalances it to them (S80, S82)."],
  emotion=[("Start", "stressed and unsure, expecting another afternoon of chasing people and fixing clashes."),
           ("Middle", "relieved when the overrun clash is caught before anyone is double-booked, and confident because the hours are clear and nothing is vague."),
           ("End", "in control. Atlas is staffed in minutes, Orion is still covered, and nobody on the team is overloaded.")],
  ids="S1, S3, S4, S9, S11, S15, S16, S24, S29, S33, S43, S46, S47, S48, S51, S52, S53, S56, S57, S80, S82, S92"),
 dict(id="CS2", title="Keeping a slipping project on track", user="Nisha", tier="Primary",
  exps=["Viewing availability", "Allocating people to projects", "Managing conflicts", "Monitoring team workload"],
  context="Nisha runs \"Orion\", a client project that has just slipped by 2 weeks because the client changed the scope. Some of her team are needed longer, some less, and one person isn't needed any more. She used to update 2 spreadsheets and ping 3 managers to make changes like these.",
  goal="re-plan the team for the new timeline without overloading anyone or leaving gaps.",
  metrics=["Time to re-plan after a slip: from approximately 1 day down to under 1 hour",
           "Allocation changes made without any back-and-forth with other managers: approximately 90%",
           "Overlaps left unresolved after re-planning: 0"],
  actions=["Nisha opens each team member's availability across all their projects for the next month (S2).",
           "She extends the allocations of the two developers she still needs by 2 weeks (S30).",
           "The designer's work is mostly done, so she reduces their hours from 30 to 15 per week (S31).",
           "QA is no longer needed after the new scope, so she removes the QA engineer from Orion (S32).",
           "One extension overlaps with a developer's next booking. She shifts the dates of his Orion allocation to avoid the overlap (S54).",
           "She checks the workload view for her project team only and confirms that nobody is above 100% (S84). Arjun sees that the QA engineer is now below 50% and available for other work (S81)."],
  emotion=[("Start", "anxious, because the slip could cause a chain of clashes and difficult conversations."),
           ("Middle", "reassured, because every change shows its effect on hours straight away."),
           ("End", "confident. The new plan is clear, the overlap is resolved and nobody is overloaded.")],
  ids="S2, S30, S31, S32, S54, S81, S84"),
 dict(id="CS3", title="Starting out and keeping my profile current", user="Individual Contributor", tier="Secondary",
  exps=["Onboarding and first-time setup", "Managing my profile and allocations", "Viewing availability"],
  context="Ravi, a backend developer, has just received his invite to the platform. He works for two managers and often isn't sure what he's committed to each week. He recently earned an AWS certification that nobody knows about.",
  goal="set up an accurate profile and always know his own commitments.",
  metrics=["Profile completed on first login: within approximately 10 minutes",
           "Skill profiles updated in the last 6 months: approximately 90% across the organization",
           "Times he has to ask a manager \"what am I on next week?\": 0"],
  actions=["Ravi logs in for the first time and completes his skill profile (S150).",
           "He adds AWS at an Intermediate level after his certification (S94), raises his Node.js level to Expert (S95) and removes jQuery, which he no longer uses (S96).",
           "He's moving to a 4-day week next month, so he updates his availability to 32 hrs/week (S97).",
           "He views his own availability for the next 4 weeks (S5) and his upcoming allocations, with project details and managers (S93).",
           "He sees the allocations from both of his managers together in one place (S103)."],
  emotion=[("Start", "sceptical, expecting yet another tool to fill in."),
           ("Middle", "pleasantly surprised that setup is quick and his new skill is now visible to managers."),
           ("End", "in control. He knows exactly what he's committed to, and his reduced hours will be respected.")],
  ids="S5, S93, S94, S95, S96, S97, S103, S150"),
 dict(id="CS4", title="Setting up the platform and retiring spreadsheets", user="Admin", tier="Secondary",
  exps=["Setting up and administering the platform", "Onboarding and first-time setup"],
  context="Meera, from Resource Ops, is launching the platform at Nimbus Labs. All the data is in managers' spreadsheets today, the skills list is messy and people keep joining and leaving.",
  goal="set up the platform with complete, clean data so that the spreadsheets can be retired.",
  metrics=["People and projects set up in the platform: 100% within the first week",
           "Spreadsheets still in use for resourcing: 0 within approximately 1 month",
           "Import errors fixed before go-live: 100%"],
  actions=["Meera imports people and allocations in bulk from the existing spreadsheets (S129). The platform flags duplicate rows and missing hours, and she fixes them before confirming (S132).",
           "She sets standard working hours at 40/week and records part-time contracts (S127).",
           "She assigns permissions for each role, such as managers, contributors and read-only for Leadership and Finance (S121).",
           "She adds missing skills to the skills list, e.g. \"Figma\" (S124).",
           "She creates the new project \"Atlas\" with its dates and manager (S122), and archives the completed project \"Vega\" (S123).",
           "She adds a new joiner with their role, team and permissions (S119), and moves another person to a new manager (S120).",
           "Someone who has left still has future allocations, so she deactivates them and their managers are alerted to reassign the work (S131).",
           "She sends invites to all users (S148)."],
  emotion=[("Start", "overwhelmed by messy data from several sources."),
           ("Middle", "relieved that errors are caught before go-live instead of afterwards."),
           ("End", "proud. There is now one clean source of truth for the whole organization.")],
  ids="S119, S120, S121, S122, S123, S124, S127, S129, S131, S132, S148"),
]
