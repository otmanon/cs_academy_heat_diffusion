# Lesson 2: Finite Differences — Arithmetic a Computer Can Do

In Lesson 1 we wrote the heat equation:

$$
\frac{\partial T}{\partial t} = \alpha \, \nabla^2 T
$$

It's a beautiful sentence, but a computer can't evaluate those calculus symbols.
A computer only adds, subtracts, multiplies, and divides the numbers in our
grid. This lesson replaces every symbol above with plain arithmetic. The trick
is called the **finite-difference method**.

---

## 1. Space between the points

Our grid isn't infinitely fine — the points sit a real distance apart. If the
whole pan is `width` meters across and split into `grid_size` points, the spacing
between two neighbors is:

```python
dx = width / grid_size     # meters between adjacent grid points
```

Keep `dx` in mind; it's the ruler we measure everything against.

---

## 2. The Laplacian becomes the 5-point stencil

We already met the discrete Laplacian in Lesson 1 as "neighbors minus four times
me." Made fully precise (and scaled by the spacing `dx`), it is:

$$
\nabla^2 T \;\approx\; \frac{T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1} - 4\,T_{i,j}}{dx^2}
$$

Because it touches a center point and its four immediate neighbors, this pattern
is called the **5-point stencil**. Picture it stamped over one grid point:

```
            [ T(i-1, j) ]
                 |
 [ T(i, j-1) ]--[ -4·T(i,j) ]--[ T(i, j+1) ]
                 |
            [ T(i+1, j) ]
```

To apply it, you slide this stamp over **every** point in the grid and compute
that combination. The result is a new grid telling you, at each spot, how far it
is from its neighbors.

---

## 3. Time becomes a small step forward

The left side, $\partial T / \partial t$, means "the rate of change in time." A
computer approximates it by taking one small **timestep** `dt` and asking how
much `T` changed over it:

$$
\frac{\partial T}{\partial t} \;\approx\; \frac{T^{\text{new}} - T^{\text{old}}}{dt}
$$

Set the two approximations equal and solve for the one thing we want — the new
temperature:

$$
\boxed{\,T^{\text{new}}_{i,j} = T_{i,j} + \alpha\,dt\;\frac{T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1} - 4\,T_{i,j}}{dx^2}\,}
$$

Read it as: **new = old + (how eager the material is) × (how long we wait) ×
(how far you are from your neighbors).** That boxed line is the entire simulator.

---

## 4. Doing it to the whole grid at once

You *could* write a double `for` loop over every `i` and `j`, but NumPy lets us
apply the stencil to the entire grid in one shot using **slicing**. The four
neighbor grids are just the temperature array shifted by one row or column:

```python
def update_temperature(T, alpha, dt, dx):
    Tnew = T.copy()
    # 5-point Laplacian on every interior point at once:
    laplacian = (
        T[2:,   1:-1]   # neighbor below
      + T[:-2,  1:-1]   # neighbor above
      + T[1:-1, 2:]     # neighbor right
      + T[1:-1, :-2]    # neighbor left
      - 4 * T[1:-1, 1:-1]
    ) / dx**2
    Tnew[1:-1, 1:-1] = T[1:-1, 1:-1] + alpha * dt * laplacian
    return Tnew
```

Each slice like `T[2:, 1:-1]` grabs "every interior point's lower neighbor" as a
whole block, so the whole grid updates in a single vectorized expression — no
loops, and it runs fast. **This function is exactly the notebook exercise you'll
fill in.**

> Notice the `1:-1` everywhere: we deliberately skip the outermost ring of
> points, because an edge point doesn't have a neighbor on all four sides. What
> to do about that edge is the subject of the next lesson.

---

## 5. Where we're headed

We can now compute one timestep. A real simulation runs *thousands* of them in a
row, and we have to decide what happens at the grid's edges and how big `dt` is
allowed to be before the whole thing explodes. That's the final lesson.

**Next up → Lesson 3: Simulating Diffusion.**
