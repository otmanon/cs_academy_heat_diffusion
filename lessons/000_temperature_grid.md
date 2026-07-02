# Lesson 0: The Temperature Grid — How Computers Store Heat

Before we can *simulate* heat spreading, we need to answer a simpler question:

> How does a computer even store "how hot everything is" in the first place?

A computer only knows how to store **numbers**. So the big idea of this lesson
is:

> **A temperature that varies across space is just a grid of numbers.**

That's it. Once you believe that, the rest of the course is just doing math on
that grid.

---

## 1. One number per point

Imagine a square frying pan. Every spot on that pan has its own temperature —
the middle might be scorching while the edges are still cool. To store this, we
lay an imaginary **grid** over the pan and record one temperature number at each
grid point.

If we use a 10×10 grid, that's 100 numbers — a little table where row `i` and
column `j` holds the temperature at that spot:

```
        cold ......... cold
 cold    20   20   20   20
 cold    20  100  100   20
 cold    20  100  100   20
 cold    20   20   20   20
```

A grid of numbers like this is exactly what NumPy calls a **2D array**.

---

## 2. Building the grid in code

In the notebook we create the grid with a single line:

```python
import numpy as np

grid_size = 10                                    # 10 points across, 10 down
T = np.zeros((grid_size, grid_size))              # every point starts at 0
```

`np.zeros((10, 10))` hands us a 10×10 table filled with zeros. `T[i, j]` is the
temperature at row `i`, column `j`.

To set a hot square in the middle, we just overwrite those entries:

```python
T[4:6, 4:6] = 373     # a 2×2 boiling-hot patch (373 kelvin = 100 °C)
```

> We measure temperature in **kelvin** (K) so we can act like proper scientists.
> 373 K is the boiling point of water; room temperature is about 293 K.

---

## 3. Seeing the grid

Numbers in a table are hard to read, so we draw the grid as an **image**: one
pixel per grid point, colored by temperature (bright = hot, dark = cold). The
notebook does this with `plt.imshow(T, cmap='hot')`, and you'll see a glowing
square floating in a cold field — like a hot spot on a pan.

---

## 4. Why this matters for the rest of the course

Here's the punchline that sets up everything to come.

The **grid never changes shape** — it's always the same 10×10 layout of points.
What *changes* over time is only **the numbers inside it**: the hot square will
fade and spread as heat leaks into its neighbors.

So simulating heat is nothing more than **repeatedly updating the numbers in the
grid**. That raises the key question of the whole course:

> Given the grid right now, what should each number become a moment later?

The answer is a beautifully simple rule — every point drifts toward the average
of its neighbors — and that's exactly where we go next.

**Next up → Lesson 1: The Heat Equation.**
