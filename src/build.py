# Builds both pages: index.html (Part 1, Design Brief) and scenario-map/index.html (Part 2, Scenario Map).
import pathlib, runpy

HERE = pathlib.Path(__file__).parent
for page in ("design-brief", "scenario-map"):
    runpy.run_path(str(HERE / page / "build.py"), run_name="__main__")
