
import matplotlib.pyplot as plt
import numpy as np

world = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

fig, ax = plt.subplots()

ax.imshow(world, cmap="Greens", vmin=0, vmax=1)

ax.set_xticks(np.arange(-0.5, 5, 1))
ax.set_yticks(np.arange(-0.5, 5, 1))

ax.grid(color="black", linewidth=1)

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()
