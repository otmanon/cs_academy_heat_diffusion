# Lesson 1: The Heat Equation — Drifting Toward the Average

In Lesson 0 we stored temperature as a grid of numbers. Now we ask the central
question of the whole course:

> Given the grid right now, how should each number change a moment later?

The answer is one short sentence, and it's worth memorizing:

> **Every point drifts toward the average of its neighbors.**

Everything else — the fancy equation, the code, the animation — is just this
sentence made precise.

---

## 1. The intuition: hot leaks into cold

Picture three points in a row on our grid. The middle one is at 100, and its two
neighbors are cold at 0:

```
0        100        0
```

Left alone, what happens? Heat flows *out* of the hot middle into the cold
sides. The middle cools, the sides warm, and the sharp spike smooths into a
gentle bump. Wait long enough and all three settle at the same value.

Notice **which way each point moved**: the middle (100) was *above* its
neighbors' average (0), so it went **down**. The sides (0) were *below* their
neighbor's influence, so they went **up**. In every case a point moved *toward*
the temperature around it. That's the whole idea.

---

## 2. Making "toward the average" precise

How *fast* does a point move? It depends on how far it is from its surroundings.
Define the mismatch between a point and its neighbors as:

$$
\text{mismatch} = (\text{sum of neighbor temperatures}) - (\text{number of neighbors}) \times T_{\text{here}}
$$

On our 2D grid a point has four neighbors — up, down, left, right — so:

$$
\text{mismatch at }(i,j) = T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1} - 4\,T_{i,j}
$$

- If a point is **hotter** than its neighbors, this number is **negative** → the
  point will cool down.
- If it's **colder**, the number is **positive** → the point will warm up.
- If it already equals the neighbor average, the number is **zero** → nothing
  changes. (This is why a perfectly even grid stays put forever.)

This quantity has a name — it's the **Laplacian** of the temperature, usually
written $\nabla^2 T$. Don't let the symbol scare you: on a grid it is *literally*
"neighbors minus four times me."

---

## 3. The heat equation

Heat changes over time in proportion to that mismatch. In the language of
calculus that statement is **the heat equation**:

$$
\frac{\partial T}{\partial t} = \alpha \, \nabla^2 T
$$

Read it out loud in plain English:

> *The rate at which a point's temperature changes ($\partial T / \partial t$)
> is proportional to how far it is from the average of its neighbors
> ($\nabla^2 T$).*

The constant $\alpha$ (**alpha**) is the material's **thermal diffusivity** — how
eagerly it passes heat along. Copper has a big $\alpha$ and evens out fast; wood
has a tiny one and holds hot spots for a long time. It's just a dial for *how
quickly* the drifting happens.

---

## 4. Where we're headed

We now have the rule in math form, but a computer can't do $\partial T /
\partial t$ directly — it doesn't know calculus, only arithmetic. In the next
lesson we turn the smooth heat equation into a concrete recipe of `+`, `-`, and
`×` on grid entries: the **finite-difference** method.

**Next up → Lesson 2: Finite Differences.**
