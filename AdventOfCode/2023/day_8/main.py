from dataclasses import dataclass
from enum import Enum
from functools import reduce
from math import gcd


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


@dataclass
class Node:
    value: str
    left: str
    right: str


@dataclass
class Instructions:
    directions: list[Direction]
    nodes: dict[str, Node]


class Challenge_8:
    def parse_file(self, file_name: str = "AdventOfCode/2023/day_8/input_test.txt"):
        with open(file_name, "r") as file:
            content = file.readlines()

            directions: list[Direction] = [
                Direction(direction) for direction in content[0].strip()
            ]
        instructions = Instructions(directions, dict())

        for i in range(2, len(content)):
            value, nodes = content[i].strip().split("=")

            left, right = nodes.replace("(", "").replace(")", "").split(",")

            instructions.nodes[value.strip()] = Node(
                value.strip(), left.strip(), right.strip()
            )

        return instructions

    def challenge(self, instructions: Instructions) -> int:
        current_node = instructions.nodes["AAA"]
        iterations = 0
        while True:
            match instructions.directions[iterations % len(instructions.directions)]:
                case Direction.LEFT:
                    current_node = instructions.nodes[current_node.left]
                case Direction.RIGHT:
                    current_node = instructions.nodes[current_node.right]

            iterations += 1
            if current_node.value == "ZZZ":
                break

        return iterations

    def lcm(self, a, b):
        return a * b // gcd(a, b)

    def challenge_2(self, instructions: Instructions) -> int:
        starting_nodes: list[Node] = [
            instructions.nodes[node]
            for node in instructions.nodes
            if node.endswith("A")
        ]
        iterations = 0
        steps_needed = []
        nodes: list[Node] = starting_nodes

        while len(nodes) > 0:
            temp_nodes: list[Node] = []
            for node in nodes:
                if node.value.endswith("Z"):
                    steps_needed.append(iterations)
                    continue

                match instructions.directions[
                    iterations % len(instructions.directions)
                ]:
                    case Direction.LEFT:
                        temp_nodes.append(instructions.nodes[node.left])
                    case Direction.RIGHT:
                        temp_nodes.append(instructions.nodes[node.right])

            iterations += 1
            nodes = temp_nodes

        return reduce(self.lcm, steps_needed)


if __name__ == "__main__":
    challenge = Challenge_8()

    instructions_test = challenge.parse_file("AdventOfCode/2023/day_8/input_test.txt")
    total_iterations_test = challenge.challenge(instructions_test)
    print(total_iterations_test)

    instructions = challenge.parse_file("AdventOfCode/2023/day_8/input.txt")
    total_iterations = challenge.challenge(instructions)
    print(total_iterations)

    instructions_test_2 = challenge.parse_file(
        "AdventOfCode/2023/day_8/input_test_2.txt"
    )
    total_iterations_2_test = challenge.challenge_2(instructions_test_2)

    print(total_iterations_2_test)

    total_iterations_2 = challenge.challenge_2(instructions)

    print(total_iterations_2)
