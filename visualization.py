
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

from life import next_generation


# 1. Create a larger world
rows = 60
columns = 60

initial_density = 0.3

world = [
    [
        1 if random.random() < initial_density else 0
        for _ in range(columns)
    ]
    for _ in range(rows)
]


# 2. Place a glider near the center
world[9][10] = 1
world[10][8] = 1
world[10][10] = 1
world[11][9] = 1
world[11][10] = 1
world[11][11] = 1


# 3. Prepare the visualization
fig, ax = plt.subplots()

state = [world]

image = ax.imshow(
    state[0],
    cmap="Greens",
    vmin=0,
    vmax=1,
    interpolation="nearest"
)

ax.set_xticks(np.arange(-0.5, columns, 1))
ax.set_yticks(np.arange(-0.5, rows, 1))

ax.grid(color="gray", linewidth=0.5)

ax.set_xticklabels([])
ax.set_yticklabels([])

title = ax.set_title("Generation 0")


# 4. Update the world every frame
def update(frame):
    state[0] = next_generation(state[0])

    image.set_data(state[0])
    title.set_text(f"Generation {frame + 1}")

    return [image, title]


# 5. Start the animation
animation = FuncAnimation(
    fig,
    update,
    frames=200,
    interval=300,
    blit=False,
    repeat=True
)

plt.show()
