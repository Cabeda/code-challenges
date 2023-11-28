from enum import Enum


class Op(Enum):
    NOOP = "noop"
    ADDX = "addx"


cycle = 0
register = 1
CRT_pos = 0
signal_strengths = []
screen_line = ""
screen_lines = []


def get_strength(cycle, register, signal_strengths):
    if cycle == 20 or (cycle - 20) % 40 == 0:
        signal_strengths.append(cycle * register)
    return signal_strengths


def update_screen(register, CRT_pos, screen_line):
    if CRT_pos <= register + 1 and CRT_pos >= register - 1:
        screen_line += "#"
    else:
        screen_line += "."

    CRT_pos += 1

    if CRT_pos % 40 == 0:
        print(screen_line)
        screen_line = ""
        CRT_pos = 0

    return [register, CRT_pos, screen_line]


with open("input_10.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()

        match line.split(" "):
            case [Op.NOOP.value]:
                [register, CRT_pos, screen_line] = update_screen(
                    register, CRT_pos, screen_line
                )

                cycle += 1
                get_strength(cycle, register, signal_strengths)

            case [Op.ADDX.value, num]:
                for c in range(0, 2):
                    [register, CRT_pos, screen_line] = update_screen(
                        register, CRT_pos, screen_line
                    )
                    cycle += 1
                    get_strength(cycle, register, signal_strengths)

                register += int(num)
            case _:
                raise Exception("Invalid OP")


print(signal_strengths)
print(sum(signal_strengths))
