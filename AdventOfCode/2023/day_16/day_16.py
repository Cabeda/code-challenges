# --- Day 16: The Floor Will Be Lava ---

# With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.

# Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.

# Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

# The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

# You note the layout of the contraption (your puzzle input). For example:

# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....

# The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

#     If the beam encounters empty space (.), it continues in the same direction.
#     If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
#     If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
#     If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.

# Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

# In the above example, here is how the beam of light bounces around the contraption:

# >|<<<\....
# |v-.\^....
# .v...|->>>
# .v...v^.|.
# .v...v^...
# .v...v^..\
# .v../2\\..
# <->-/vv|..
# .|<<<2-|.\
# .v//.|.v..

# Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

# ######....
# .#...#....
# .#...#####
# .#...##...
# .#...##...
# .#...##...
# .#..####..
# ########..
# .#######..
# .#...#.#..

# Ultimately, in this example, 46 tiles become energized.

# The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?

# --- Part Two ---

# As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

# So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.

# In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

# .|<2<\....
# |v-v\^....
# .v.v.|->>>
# .v.v.v^.|.
# .v.v.v^...
# .v.v.v^..\
# .v.v/2\\..
# <-2-/vv|..
# .|<<<2-|.\
# .v//.|.v..

# Using this configuration, 51 tiles are energized:

# .#####....
# .#.#.#....
# .#.#.#####
# .#.#.##...
# .#.#.##...
# .#.#.##...
# .#.#####..
# ########..
# .#######..
# .#...#.#..

# Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?

import sys
from dataclasses import dataclass


@dataclass
class Move:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Move(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Challenge_16:
    def parse_file(self, file_name: str = "input_test.txt"):
        lines = []
        with open(file_name, "r") as file:
            for line in file:
                lines.append(list(line.strip()))

        return lines

    def print_grid(self, grid: list[list[str]], current_coord: Move = Move(-1, 0)):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if current_coord.x == x and current_coord.y == y:
                    print("X", end="")
                else:
                    print(grid[y][x], end="")
            print()
        print("\n")

    def parse_line(
        self,
        grid: list[list[str]],
        prevCoordinate: Move = Move(-1, 0),
        move: Move = Move(1, 0),
        seen: set[str] = set(),
    ) -> set[str]:
        current_coord = Move(move.x + prevCoordinate.x, move.y + prevCoordinate.y)

        # self.print_grid(grid, current_coord)

        if str(prevCoordinate) + "|" + str(current_coord) in seen:
            return seen
        else:
            seen.add(str(prevCoordinate) + "|" + str(current_coord))

        if (
            current_coord.x < 0
            or current_coord.x >= len(grid)
            or current_coord.y < 0
            or current_coord.y >= len(grid[0])
        ):
            return seen

        char = grid[current_coord.y][current_coord.x]
        match char:
            case ".":
                seen.union(self.parse_line(grid, current_coord, move, seen))
            case "|":
                if prevCoordinate != current_coord + Move(0, 1):
                    seen.union(self.parse_line(grid, current_coord, Move(0, 1), seen))
                if prevCoordinate != current_coord + Move(0, -1):
                    seen.union(self.parse_line(grid, current_coord, Move(0, -1), seen))
            case "-":
                if prevCoordinate != current_coord + Move(1, 0):
                    seen.union(self.parse_line(grid, current_coord, Move(1, 0), seen))
                if prevCoordinate != current_coord + Move(-1, 0):
                    seen.union(self.parse_line(grid, current_coord, Move(-1, 0), seen))
            case "/":
                match move:
                    case Move(1, 0):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(0, -1), seen)
                        )
                    case Move(0, 1):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(-1, 0), seen)
                        )
                    case Move(-1, 0):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(0, 1), seen)
                        )
                    case Move(0, -1):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(1, 0), seen)
                        )
            case "\\":
                match move:
                    case Move(1, 0):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(0, 1), seen)
                        )
                    case Move(0, 1):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(1, 0), seen)
                        )
                    case Move(-1, 0):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(0, -1), seen)
                        )
                    case Move(0, -1):
                        seen.union(
                            self.parse_line(grid, current_coord, Move(-1, 0), seen)
                        )

        return seen


def get_length(seen: set[str]):
    return len(set([l.split("|")[0] for l in seen])) - 1


challenge = Challenge_16()

lines = challenge.parse_file("day_16/input.txt")

sys.setrecursionlimit(15000)
seen = challenge.parse_line(lines)
print(get_length(seen))


# Part 2

max_energized: set[int] = set()

for y in range(len(lines)):
    total_y_0 = challenge.parse_line(lines, Move(-1, y), Move(1, 0), set())
    total_y_1 = challenge.parse_line(lines, Move(len(lines[0]), y), Move(-1, 0), set())

    # print(Move(-1, y), Move(1, 0), get_length(total_y_0))
    # print(Move(len(lines[0]), y), Move(-1, 0), get_length(total_y_1))
    max_energized.add(get_length(total_y_0))
    max_energized.add(get_length(total_y_1))

print("\n")
for x in range(len(lines[0])):

    total_x_0 = challenge.parse_line(lines, Move(x, -1), Move(0, 1), set())
    total_x_1 = challenge.parse_line(lines, Move(x, len(lines)), Move(0, -1), set())

    # print(Move(x, -1), Move(0, 1), get_length(total_x_0))
    # print(Move(x, len(lines) + 1), Move(0, -1), get_length(total_x_1))
    max_energized.add(get_length(total_x_0))
    max_energized.add(get_length(total_x_1))

print(max(max_energized))
