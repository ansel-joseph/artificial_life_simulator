
import random


# 1. Count the living neighbors of a cell
def count_neighbors(world, row, column):
    rows = len(world)
    columns = len(world[0])

    neighbors = 0

    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):

            if r == row and c == column:
                continue

            if 0 <= r < rows and 0 <= c < columns:
                neighbors += world[r][c]

    return neighbors


# 2. Calculate the next generation
def next_generation(world):
    rows = len(world)
    columns = len(world[0])

    new_world = []

    for r in range(rows):
        new_row = []

        for c in range(columns):
            neighbors = count_neighbors(world, r, c)
            cell = world[r][c]

            if cell == 1 and (neighbors == 2 or neighbors == 3):
                new_cell = 1
            elif cell == 0 and neighbors == 3:
                new_cell = 1
            else:
                new_cell = 0

            new_row.append(new_cell)

        new_world.append(new_row)

    return new_world


# 3. Run the simulation
def main():
    

    world = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

    print("Initial world:")
    for row in world:
        print(row)

    print("Living neighbors:", count_neighbors(world, 2, 2))

    for generation in range(10):
        print(f"\nGeneration {generation + 1}:")

        world = next_generation(world)

        for row in world:
            print(row)


if __name__ == "__main__":
    main()
