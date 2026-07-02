# Lesson 3: Simulating Diffusion — Time, Edges, and Stability

In Lesson 2 we built `update_temperature`, which advances the grid by one small
timestep. A simulation is just that step run over and over. This lesson covers
the three things you need to turn one step into a believable animation:

1. **Looping** through time,
2. **Boundary conditions** — what to do at the edges,
3. **Stability** — the rule that stops the simulation from exploding.

---

## 1. Looping through time

If our timestep is `dt = 0.01` seconds and we want to simulate 1 second, we run
`1 / 0.01 = 100` steps. Each step feeds its output back in as the next step's
input:

```python
T = initial_temperature
for step in range(num_frames):
    T = update_temperature(T, alpha, dt, dx)
```

In the notebook, matplotlib's `FuncAnimation` calls the update once per frame and
redraws the image, so you literally watch the hot spot spread and fade.

---

## 2. Boundary conditions: what happens at the edge?

Remember from Lesson 2 that the 5-point stencil needs a neighbor on all four
sides — but the points on the outer ring of the grid don't have one. We have to
*decide* how the world behaves just past the edge. This choice is called a
**boundary condition**, and two are common:

- **Fixed (Dirichlet):** clamp the edges to a set temperature — like the pan's
  rim being held in an ice bath. `T[0, :] = 273`.
- **Insulated (Neumann):** let no heat escape — the edge simply copies its inner
  neighbor, so there's no gradient across the boundary and nothing leaks out:

```python
T[0, :]  = T[1, :]      # top row copies the row just inside it
T[-1, :] = T[-2, :]     # bottom row
T[:, 0]  = T[:, 1]      # left column
T[:, -1] = T[:, -2]     # right column
```

The notebook uses the **insulated** condition, so the total heat stays trapped
inside the pan and just spreads until the whole grid reaches one even
temperature.

---

## 3. Stability: don't let it explode

Here's a surprise that bites everyone the first time. If you make the timestep
`dt` too big, the simulation doesn't just get *inaccurate* — it violently blows
up, with temperatures flip-flopping to wild positive and negative values until
they overflow to infinity.

Intuitively: each step nudges a point toward its neighbors' average. If the nudge
is *too strong*, the point overshoots **past** the average to the other side,
then overshoots back even harder next step, and the oscillation feeds itself.

For our 2D scheme the safe range is captured by one inequality:

$$
\alpha \, \frac{dt}{dx^2} \;\le\; \frac{1}{4}
$$

In words: **the eagerness of the material times the timestep, divided by the
spacing squared, must stay at or below one quarter.** If your simulation ever
fills with `NaN`s or garish flickering, this is almost always the culprit — shrink
`dt` (or the diffusivity `alpha`) until the inequality holds.

You can test this yourself in the notebook: nudge `dt` up little by little and
watch the exact moment the smooth spreading turns into noise.

---

## 4. You've built a simulator

Step back and look at what you now have. Starting from nothing but a grid of
numbers, you can:

- store a temperature field (Lesson 0),
- express how heat moves as "drift toward the neighbor average" (Lesson 1),
- turn that into arithmetic with the 5-point stencil (Lesson 2),
- and march it through time with sane edges and a stable timestep (this lesson).

That's the same core algorithm behind climate models, heat-sink design, and the
smoke and fire you see in movies. Open `notebooks/heat_diffusion.ipynb`, fill in
`update_temperature`, and watch your hot spot melt away.

**That's the course — now go break it and see what happens.**
