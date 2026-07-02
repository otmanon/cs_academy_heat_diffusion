# Syllabus

Work through these lessons in order. Each one builds directly on the one before,
and together they explain everything you need to build a working **heat
diffusion** simulator from scratch. The hands-on coding companion is
`notebooks/heat_diffusion.ipynb`.

0. [**The Temperature Grid**](000_temperature_grid.md) — how a computer stores a
   temperature that varies across space: a grid of numbers.
1. [**The Heat Equation**](001_heat_equation.md) — the one idea behind all of
   it: every point drifts toward the average of its neighbors.
2. [**Finite Differences**](002_finite_differences.md) — turning that smooth
   idea into arithmetic a computer can do, using the 5-point stencil.
3. [**Simulating Diffusion**](003_simulating_diffusion.md) — stepping through
   time, boundary conditions, and the stability rule that keeps it from blowing
   up.

<!--
Guidelines for writing a lesson:
- One concept per file; assume only what earlier lessons established.
- Explain in plain English first, then formalize.
- Point to the matching notebook exercise so students can apply the idea.
-->
