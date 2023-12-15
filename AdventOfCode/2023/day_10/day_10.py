import os
from dataclasses import dataclass
from enum import Enum
from time import sleep
from typing import Optional, Tuple


class PipeType(Enum):
    HORIZONTAL = "-"
    VERTICAL = "|"
    L = "L"
    J = "J"
    SEVEN = "7"
    F = "F"
    NONE = "."
    S = "S"


@dataclass
class Pipe:
    element: PipeType | int
    startDistance: Optional[int] = None


@dataclass
class Row:
    pipes: list[Pipe]


@dataclass
class Coordinate:
    x: int
    y: int


@dataclass
class Map:
    rows: list[Row]
    startPosition: Coordinate


def get_moves(pipe: Pipe) -> list[Coordinate]:
    match pipe.element:
        case PipeType.HORIZONTAL:
            return [Coordinate(1, 0), Coordinate(-1, 0)]
        case PipeType.VERTICAL:
            return [Coordinate(0, 1), Coordinate(0, -1)]
        case PipeType.L:
            return [Coordinate(0, -1), Coordinate(1, 0)]
        case PipeType.J:
            return [Coordinate(0, -1), Coordinate(-1, 0)]
        case PipeType.SEVEN:
            return [Coordinate(0, 1), Coordinate(-1, 0)]
        case PipeType.F:
            return [Coordinate(0, 1), Coordinate(1, 0)]
        case PipeType.NONE:
            return []
        case PipeType.S:
            return []
        case _:
            raise Exception("Invalid Pipe")


class Challenge_10:
    def parse_file(
        self, file_name: str = "AdventOfCode/2023/day_10/input_test.txt"
    ) -> Map:
        map: Map = Map([], Coordinate(0, 0))
        with open(file_name, "r") as file:
            for line in file:
                row = Row([])

                for num in line.strip():
                    pipe = Pipe(PipeType(num))
                    row.pipes.append(pipe)
                    if pipe.element == PipeType.S:
                        map.startPosition = Coordinate(
                            len(row.pipes) - 1, len(map.rows)
                        )

                map.rows.append(row)

        return map

    def updatePosition(
        self,
        map: Map,
        current_Position: Coordinate,
        prev_move: Coordinate,
        distance: int,
    ):
        pipe = map.rows[current_Position.y].pipes[current_Position.x]

        if pipe.element == PipeType.NONE or pipe.startDistance is not None:
            return None, current_Position

        moves = get_moves(pipe)

        move = moves[0]

        if Coordinate(
                current_Position.x + moves[0].x,
                current_Position.y + moves[0].y,
            ) == prev_move:
            move = moves[1] 
            if Coordinate(
                    current_Position.x + moves[1].x,
                    current_Position.y + moves[1].y,
                ) != prev_move:
                return None, current_Position

        pipe.startDistance = distance
        pipe.element = distance
        self.print_map(map)

        next_position = Coordinate(
            current_Position.x + move.x, current_Position.y + move.y
        )

        return next_position, current_Position

    def print_map(self, map: Map):
        os.system("cls" if os.name == "nt" else "clear")
        for row in map.rows:
            pipes = []
            for pipe in row.pipes:
                if type(pipe.element) == PipeType:
                    pipes.append(pipe.element.value)
                else:
                    pipes.append(str(pipe.element))
            print("".join(pipes))
        sleep(0.5)

    def challenge(self, map: Map):
        # Find valid positions in the map
        validStartPositions: list[Tuple[Coordinate, Coordinate]] = []

        left = (
            map.rows[map.startPosition.y].pipes[map.startPosition.x - 1]
            if map.startPosition.x - 1 >= 0
            else None
        )
        right = (
            map.rows[map.startPosition.y].pipes[map.startPosition.x + 1]
            if map.startPosition.x + 1 < len(map.rows[0].pipes)
            else None
        )
        up = (
            map.rows[map.startPosition.y - 1].pipes[map.startPosition.x]
            if map.startPosition.y - 1 >= 0
            else None
        )
        down = (
            map.rows[map.startPosition.y + 1].pipes[map.startPosition.x]
            if map.startPosition.y + 1 < len(map.rows)
            else None
        )

        if left and (
            left.element == PipeType.HORIZONTAL
            or left.element == PipeType.L
            or left.element == PipeType.F
        ):
            validStartPositions.append(
                (
                    Coordinate(map.startPosition.x, map.startPosition.y - 1),
                    map.startPosition,
                )
            )
        if right and (
            right.element == PipeType.HORIZONTAL
            or right.element == PipeType.J
            or right.element == PipeType.SEVEN
        ):
            validStartPositions.append(
                (
                    Coordinate(map.startPosition.x, map.startPosition.y + 1),
                    map.startPosition,
                )
            )
        if up and (
            up.element == PipeType.VERTICAL
            or up.element == PipeType.SEVEN
            or up.element == PipeType.F
        ):
            validStartPositions.append(
                (
                    Coordinate(map.startPosition.x - 1, map.startPosition.y),
                    map.startPosition,
                )
            )
        if down and (
            down.element == PipeType.VERTICAL
            or down.element == PipeType.L
            or down.element == PipeType.J
        ):
            validStartPositions.append(
                (
                    Coordinate(map.startPosition.x + 1, map.startPosition.y),
                    map.startPosition,
                )
            )

        distance = 0
        map.rows[map.startPosition.y].pipes[map.startPosition.x].startDistance = 0
        map.rows[map.startPosition.y].pipes[map.startPosition.x].element = 0
        # self.print_map(map)

        distance += 1
        counter = len(validStartPositions)
        distanceCounter = 0

        while validStartPositions:
            if distanceCounter == counter:
                distance += 1
                distanceCounter = 1
            else:
                distanceCounter += 1

            next_position, prev_position = validStartPositions.pop(0)
            next_position_value, prev_position_value = self.updatePosition(
                map, next_position, prev_position, distance
            )

            if next_position_value is None:
                counter -= 1
            else:
                validStartPositions.append((next_position_value, prev_position_value))

        startDistances = [
            pipe.startDistance
            for row in map.rows
            for pipe in row.pipes
            if pipe.startDistance is not None
        ]

        return max(startDistances)

    def challenge_2(self) -> int:
        return 0


if __name__ == "__main__":
    challenge = Challenge_10()

    rows_test = challenge.parse_file()
    result_test = challenge.challenge(rows_test)
    print(f"Max distance from S is: {result_test}")

    rows = challenge.parse_file("AdventOfCode/2023/day_10/input_test_2.txt")
    result = challenge.challenge(rows)
    print(f"Max distance from S is: {result}")

    rows = challenge.parse_file("AdventOfCode/2023/day_10/input.txt")
    result = challenge.challenge(rows)
    print(f"Max distance from S is: {result}")
