# --- Day 17: Clumsy Crucible ---

# The lava starts flowing rapidly once the Lava Production Facility is operational. As you leave, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.

# As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: half of Gear Island is empty, but the half below you is a giant factory city!

# You land near the gradually-filling pool of lava at the base of your new lavafall. Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large crucibles on wheels.

# The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.

# To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory. To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.

# Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

# For example:

# 2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533

# Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. (Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

# Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

# One way to minimize heat loss is this path:

# 2>>34^>>>1323
# 32v>>>35v5623
# 32552456v>>54
# 3446585845v52
# 4546657867v>6
# 14385987984v4
# 44578769877v6
# 36378779796v>
# 465496798688v
# 456467998645v
# 12246868655<v
# 25465488877v5
# 43226746555v>

# This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

# Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?

# To begin, get your puzzle input.

from dataclasses import dataclass


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def __eq__(self, __value) -> bool:
        return self.x == __value.x and self.y == __value.y

    def __add__(self, __value):
        return Pos(self.x + __value.x, self.y + __value.y)

    def get_distance(self, __value):
        return abs(self.x - __value.x) + abs(self.y - __value.y)


@dataclass(frozen=True)
class Crucible:
    position: Pos
    heat: int
    straight: Pos
    prev_moves: set[Pos]


class Challenge_17:
    min_loss = -1

    def parse_file(self, file_name: str = "input_test.txt"):
        lines = []
        with open(file_name, "r") as file:
            for line in file:
                lines.append(list(line.strip()))

        return lines

    def find_path(self, grid: list, crucible: Crucible, end: Pos) -> int | None:
        # Add a memoization table
        memo: dict = {}

        def dfs(crucible):
            # Use the position and direction as the key
            key = (crucible.position, crucible.straight)
            if key in memo and crucible.heat >= memo[key]:
                return None
            heat_losses: set[int] = set({self.min_loss})

            if crucible.heat > self.min_loss and self.min_loss != -1:
                return None

            if crucible.position == end:
                if crucible.heat < self.min_loss or self.min_loss == -1:
                    print("New min loss: ", crucible.heat)
                    self.min_loss = crucible.heat
                return crucible.heat

            grid_heat = int(grid[crucible.position.x][crucible.position.y])

            # Get all possible moves
            moves = set(
                {
                    Pos(0, 1),
                    Pos(1, 0),
                    Pos(0, -1),
                    Pos(-1, 0),
                }
            )

            moves_with_costs = []
            for move in moves:
                new_pos = crucible.position + move
                if new_pos not in crucible.prev_moves:
                    # The cost is the distance from the start to the new position (the "g" cost)
                    # plus the heuristic distance from the new position to the end (the "h" cost)
                    g_cost = crucible.position.get_distance(
                        Pos(0,0)
                    )
                    h_cost = new_pos.get_distance(end)
                    f_cost = g_cost + h_cost
                    moves_with_costs.append((f_cost, move))

            while moves_with_costs:
                _, move = moves_with_costs.pop(0)
                new_pos = crucible.position + move
                new_straight = crucible.straight + move
                is_turn = new_straight.x != 0 and new_straight.y != 0

                if is_turn:
                    new_straight = Pos(0, 0)

                # Can't do more than 3 straights
                if new_straight.x > 3 or new_straight.y > 3:
                    continue

                # Can't do this move as it's out of bounds
                if (
                    new_pos.x < 0
                    or new_pos.y < 0
                    or new_pos.x >= len(grid)
                    or new_pos.y >= len(grid[0])
                ):
                    continue

                heat = self.find_path(
                    grid,
                    Crucible(
                        new_pos,
                        crucible.heat + grid_heat,
                        new_straight,
                        crucible.prev_moves | {crucible.position},
                    ),
                    end,
                )
                if heat:
                    heat_losses.add(heat)
            memo[key] = crucible.heat
            return min(heat_losses)

        return dfs(crucible)


challenge = Challenge_17()

lines = challenge.parse_file("day_17/input_test.txt")

result = challenge.find_path(
    lines,
    Crucible(
        Pos(0, 0),
        0,
        Pos(0, 0),
        set(),
    ),
    Pos(
        len(lines) - 1,
        len(
            lines[0],
        )
        - 1,
    ),
)

print(result)
