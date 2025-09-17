# PDA Exercises Collection (Python)

This repository contains 7 exercise scripts implemented in Python. The project
is prepared to be used in a collaborative GitHub workflow by a team of three
students. All documentation and comments are written in English.

## Assignment mapping
- **Student 1: Cristian Rodriguez** — Exercises **1, 2 and 3**.
- **Student 2: Jonathan Lanchero** — Exercises **4 and 5**.
- **Student 3: Yury Dorado** — Exercises **6 and 7**.

## Project structure
```
pda_project_full/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ main.py
└─ exercises/
   ├─ ejercicio1.py
   ├─ ejercicio2.py
   ├─ ejercicio3.py
   ├─ ejercicio4.py
   ├─ ejercicio5.py
   ├─ ejercicio6.py
   └─ ejercicio7.py
```

## Requirements (Python packages)
Install the Python requirements into a virtual environment before running:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**requirements.txt** includes `networkx`, `matplotlib`, and `graphviz` Python packages. Additionally,
Graphviz system binaries are required for `graphviz` to render diagrams. On Debian/Ubuntu you can install them with:
```bash
sudo apt-get update && sudo apt-get install -y graphviz
```

## How to run
Run the main entrypoint and select which exercise to execute:
```bash
python main.py --exercise 1       # runs exercise 1 visualization
python main.py --exercise 3       # runs exercise 3 visualization
python main.py --exercise 7       # renders graph for exercise 7 to PNG
python main.py --all              # runs all exercise demos (one by one)
```

Each exercise module exposes a function `run()` which is called by `main.py`.
All code is commented and contains docstrings in English.

## GitHub collaborative workflow (recommended)
1. Use `main` (or `main` branch) as the integration branch.
2. Each student creates a branch for their exercise(s), for example:
   - `cristian/ejercicio-1`
   - `jonathan/ejercicio-4`
   - `yury/ejercicio-7`
3. Push branch to GitHub and open a Pull Request targeting `main`.
4. After merging, delete the feature branch to keep the repository clean.

## Style
- Code follows PEP8 naming and formatting where practical.
- Functions are small and documented with docstrings.
- All textual documentation is in English.

If you want unit tests, CI config, or images embedded into the README, ask and I will add them.
