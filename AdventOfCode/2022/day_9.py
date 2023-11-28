from enum import Enum
import time


class Op(Enum):
    Up = "U"
    Right = "R"
    Left = "L"
    Down = "D"


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_pos(self):
        return f"{self.x},{self.y}"

    def __str__(self):
        return f"{self.x},{self.y}"


def get_move(tail: Position, move: Position) -> Position:
    return Position(tail.x + move.x, tail.y + move.y)


def calculate_diff(head, tail) -> Position:
    return Position(x=head.x - tail.x, y=head.y - tail.y)


def calculate_move_tail(diff: Position) -> Position:

    match diff:
        case Position(x=2, y=0):
            return Position(1, 0)
        case Position(x=-2, y=0):
            return Position(-1, 0)
        case Position(x=0, y=2):
            return Position(0, 1)
        case Position(x=0, y=-2):
            return Position(0, -1)
        case Position(x=2, y=1):
            return Position(1, 1)
        case Position(x=2, y=-1):
            return Position(1, -1)
        case Position(x=-2, y=1):
            return Position(-1, 1)
        case Position(x=1, y=2):
            return Position(1, 1)
        case Position(x=1, y=-2):
            return Position(1, -1)
        case Position(x=2, y=2):
            return Position(1, 1)
        case Position(x=-2, y=-2):
            return Position(-1, -1)
        case Position(x=-2, y=-1):
            return Position(-1, -1)
        case Position(x=-1, y=-2):
            return Position(-1, -1)
        case Position(x=-1, y=2):
            return Position(-1, 1)
        case Position(x=1, y=1):
            return Position(0, 0)
        case Position(x=1, y=0):
            return Position(0, 0)
        case Position(x=0, y=1):
            return Position(0, 0)
        case Position(x=0, y=0):
            return Position(0, 0)
        case Position(x=1, y=1):
            return Position(0, 0)
        case Position(x=1, y=-1):
            return Position(0, 0)
        case Position(x=-1, y=-1):
            return Position(0, 0)
        case Position(x=-1, y=1):
            return Position(0, 0)
        case Position(x=0, y=-1):
            return Position(0, 0)
        case Position(x=-1, y=0):
            return Position(0, 0)
        case Position(x=2, y=-2):
            return Position(1, -1)
        case Position(x=-2, y=2):
            return Position(-1, 1)
        case _:
            raise Exception("Position missing")


def track_moved_position(pos: Position, move: Position) -> list[str]:
    posis = []
    newer_tail = Position(pos.x, pos.y)

    small = min([pos.x, move.x])
    big = max([pos.x, move.x])
    for x in range(small, big):
        newer_tail = Position(x, newer_tail.y)
        posis.append(newer_tail.get_pos())

    small = min([pos.y, move.y])
    big = max([pos.y, move.y])
    for y in range(small, big):
        newer_tail = Position(newer_tail.x, y)
        posis.append(newer_tail.get_pos())

    return posis


def print_rope(head: Position, knots: list[Position], tails: list[Position]):
    height = 100
    width = 200
    grid = []
    for i in range(0, height):
        grid.append([])
        for _ in range(0, width):
            grid[i].append(".")

    for i in range(0, len(tails)):
        grid[int(tails[i].x) + int(height / 2)][int(tails[i].y) + int(width / 2)] = str(
            "*"
        )

    for i in reversed(range(0, len(knots))):
        grid[int(knots[i].x) + int(height / 2)][int(knots[i].y) + int(width / 2)] = str(
            i + 1
        )

    grid[head.x + int(height / 2)][head.y + int(width / 2)] = "H"

    lines = ""
    for i in range(0, height):
        lines = f"{''.join(grid[i])}\n" + lines
    # CLEAR CONSOLE BEFORE PRINTING AGAIN
    print("\033c", end="")
    print(lines)
    time.sleep(0.01)


head = Position()
knots = [Position() for _ in range(0, 9)]
pos_tail = []
pos_tail_2 = []

count_op = 0

with open("input_9.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        [op, num] = line.split(" ")
        count_op += 1

        num_moves = int(num)

        for _ in range(0, num_moves):

            match op:
                case Op.Up.value:
                    # print("Up 1")
                    head.x += 1
                case Op.Down.value:
                    # print("Down 1")
                    head.x -= 1
                case Op.Left.value:
                    # print("Left 1")
                    head.y -= 1
                case Op.Right.value:
                    # print("Right 1")
                    head.y += 1
                case _:
                    raise Exception(f"Invalid type {line}")

            print_rope(head, knots, pos_tail_2)
            diff = calculate_diff(head, knots[0])
            move = calculate_move_tail(diff)
            new_knot = get_move(knots[0], move)
            knots[0] = new_knot
            print_rope(head, knots, pos_tail_2)

            for i in range(1, len(knots)):
                diff = calculate_diff(knots[i - 1], knots[i])
                move = calculate_move_tail(diff)
                new_knot = get_move(knots[i], move)
                knots[i] = new_knot
                print_rope(head, knots, pos_tail_2)

            # Get position of the last knot
            pos_tail.append(knots[-1].get_pos())
            pos_tail_2.append(knots[-1])

total_tail_pos = len(set(pos_tail))
print(f"The tail got to {total_tail_pos} positions")
