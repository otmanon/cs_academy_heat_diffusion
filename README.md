# CS Academy: Heat Diffusion

Pour a cup of hot coffee and it slowly cools. Touch one end of a metal spoon
sitting in soup and the handle warms up. Heat always spreads from hot places to
cold ones until everything evens out. In this project you'll teach a computer to
*simulate* that spreading — the same math weather models, engine designers, and
special-effects studios use — starting from nothing but a grid of numbers.

By the end you'll have written a working **heat diffusion simulator** and watched
a glowing hot spot melt away across a virtual frying pan.

## Installation

### 1. Install Python (skip if you already have it)

If you're on a fresh laptop with no Python, install it from the official site:
https://www.python.org/downloads/ (any version >= 3.9).

Verify it's installed:

```bash
python3 --version
```

### 2. Install dependencies

We use [uv](https://docs.astral.sh/uv/). These two commands work identically on
macOS, Windows, and Linux — `uv sync` creates a virtual environment and installs
everything listed in `pyproject.toml`:

```bash
pip install uv
uv sync
```

(No manual "activate" step needed — `uv run` below always uses the right environment.)

### 3. Verify the install

Run this quick test — it imports the core libraries:

```bash
uv run python -c "import numpy, matplotlib; print('All dependencies installed correctly!')"
```

If it prints `All dependencies installed correctly!` with no errors, you're ready to go.

### 4. Launch the notebook

```bash
uv run jupyter notebook
```

Then open `notebooks/heat_diffusion.ipynb`.

> **No install? Use Google Colab.** Open `notebooks/heat_diffusion_colab.ipynb`
> — it runs in your browser with nothing to install. See the notebook's top cell
> for the "Open in Colab" link.

## Project Structure

Explanations of the concepts needed can be found in `lessons/`, in order of progression.

Core utility functions (if any) can be found in the `./src/` library.

Actual code students need to fill out can be found in `./notebooks/`.

Additional dependencies needed in the project can be found in `deps/` if needed.

| Directory     | What goes here                                                        |
| ------------- | -------------------------------------------------------------------- |
| `lessons/`    | Written explanations of the concepts, in order. Start with `lessons/README.md`. |
| `src/`        | Core utility functions — the project's reusable library.             |
| `notebooks/`  | Jupyter notebooks where students fill out and run code.              |
| `data/`       | Datasets and assets used by the project.                            |
| `deps/`       | Optional local / vendored dependencies (see `pyproject.toml`).       |
