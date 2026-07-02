# CS Academy Project

> Replace this section with a short description of your project — what it teaches
> and what a student will build by the end.

This repository is the **default project template** for CS Academy. It defines the
structure every project should follow. To submit your own project, fork this repo
(or create a new branch off `main`) and fill in the structure below with your
lessons, code, notebooks, and data. See [Submitting your project](#submitting-your-project).

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
uv run python -c "import numpy; print('All dependencies installed correctly!')"
```

If it prints `All dependencies installed correctly!` with no errors, you're ready to go.

## Project Structure

| Directory     | What goes here                                                        |
| ------------- | -------------------------------------------------------------------- |
| `lessons/`    | Written explanations of the concepts, in order of progression. Start with `lessons/README.md`. |
| `src/`        | Core utility functions — your project's reusable library.            |
| `notebooks/`  | Jupyter notebooks where students fill out and run code.              |
| `data/`       | Datasets and assets (meshes, images, etc.) used by the project.      |
| `deps/`       | Optional local / vendored dependencies (see `pyproject.toml`).       |

Add your project's dependencies in `pyproject.toml`.

## Submitting your project

1. **Fork** this repository, or create a **new branch** off `main`.
2. Keep the directory structure above; fill each folder with your own content.
3. Update this `README.md`, `pyproject.toml`, and `lessons/README.md` to describe
   your project.
4. Submit your fork or branch for review.

For a complete worked example, see the `skinning` branch — an "Introduction to
Skinning" project built on top of this exact template.
