# GitHub repository and local setup

Repository: https://github.com/TechBOiz/Robotics_Arm_Project

The owner created this public repository on 2026-10-01. Project files are maintained on `main`. Code, CAD and electrical licensing remain undecided.

## Clone and check

```bash
git clone https://github.com/TechBOiz/Robotics_Arm_Project.git
cd Robotics_Arm_Project
python tools/check_project.py
python tools/size_static.py
```

Python 3.10+; no third-party packages are needed for these two utilities. Neither utility communicates with hardware.

## Contribute

Create a branch for each focused change, update affected requirements/BOM/decisions, and open a pull request. See `AGENTS.md` and the pull request template. Keep credentials and large generated artifacts out of Git.

## Planning data

`planning/milestones.json`, `planning/issues.json`, and `planning/labels.json` contain planning drafts. They are not live GitHub milestones, issues or labels yet. The complete readable backlog is in `planning/backlog.md`.

Stable local IDs (ISS-001 etc.) should remain in bodies when importing drafts to live issues. Create milestones/labels before associating issues. The repository connection used for initial upload does not expose milestone/label creation, so those definitions remain versioned files.
