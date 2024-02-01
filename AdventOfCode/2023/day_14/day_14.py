# --- Day 13: Point of Incidence ---

# With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of Lava Island.

# There's just one problem: you don't see any lava.

# You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?

# As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.

# You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

# For example:

# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#

# To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

# In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:

# 123456789
#     ><
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#     ><
# 123456789

# In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

# The second pattern reflects across a horizontal line instead:

# 1 #...##..# 1
# 2 #....#..# 2
# 3 ..##..### 3
# 4v#####.##.v4
# 5^#####.##.^5
# 6 ..##..### 6
# 7 #....#..# 7

# This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.

# Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?


from collections import deque
from functools import cache


class Challenge_14:
    def parse_file(self, file_name: str = "input_test.txt"):
        with open(file_name, "r") as file:
            return tuple([line.strip() for line in file])

    @cache
    def move_north(self, grid: tuple):
        block = zip(*grid)
        new_block = []

        for line in block:
            line = list(line)
            spaces: deque = deque()
            for i in range(len(line)):
                if line[i] == ".":
                    spaces.append(i)
                elif line[i] == "O":
                    if spaces:
                        line[spaces.popleft()] = "O"
                        line[i] = "."
                        spaces.append(i)
                elif line[i] == "#":
                    spaces.clear()
            new_block.append(line)

        return tuple(zip(*new_block))

    @cache
    def cycle(self, grid: tuple) -> tuple:
        for _ in range(4):
            grid = self.move_north(grid)
            grid = tuple(["".join(row[::-1]) for row in zip(*grid)])

        return grid

    def calculate_score(self, grid: tuple):
        return sum(row.count("O") * (i + 1) for i, row in enumerate(reversed(grid)))


challenge = Challenge_14()

lines = challenge.parse_file("day_14/input_test.txt")

# Part I
new_block = challenge.move_north(tuple(lines))
score = challenge.calculate_score(new_block)
print(score)

# Part II

CYCLES = 1000000000

seen = {lines}
seen_list = [lines]

grid_cycle = lines
for i in range(CYCLES):
    grid_cycle = challenge.cycle(grid_cycle)

    # Considers that the cycle repeats itself and we can skip it
    if grid_cycle in seen:
        break
    seen.add(grid_cycle)
    seen_list.append(grid_cycle)

first_cycle_grid_index = seen_list.index(grid_cycle)
final_grid = seen_list[
    (CYCLES - first_cycle_grid_index) % (i + 1 - first_cycle_grid_index)
    + first_cycle_grid_index
]

score = challenge.calculate_score(final_grid)
print(score)
