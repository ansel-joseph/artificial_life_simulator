
import random

world = []

for row in range(5):
    new_row = []

    for column in range(5):
        cell = random.randint(0, 1)
        new_row.append(cell)

    world.append(new_row)

for row in world:
    print(row)
