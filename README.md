# Fractal-python-base

This small project renders a simple fractal to an SVG using a headless
replacement for the `turtle` API. The script writes `fractal.svg` to the
project directory.

**Get the repo**

```bash
# Clone this repository (or fork and clone your fork)
git clone https://github.com/Vaibhav-fusion/Fractal-python-base.git
cd Fractal-python-base
```

**Quickstart — run locally**

- Option A: helper script (recommended)

```bash
# run from the repository root
./run.sh
```

- Option B: manual (create/activate venv, then run)

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
# install project deps if any
pip install -r requirements.txt
python fractal.py
```

After running, the generated file `fractal.svg` will be in the project root.

Notes

- `fractal.py` uses only the Python standard library; there are no required
  third-party packages by default. Add any needed packages to `requirements.txt`.
- The helper script `run.sh` creates the virtual environment in `.venv`.
