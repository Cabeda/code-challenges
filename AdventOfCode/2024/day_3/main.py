import re


class Challenge:
    def __init__(self):
        self.data = []
        self.load_data()
        self.part1()
        self.part2()

    def load_data(self):
        with open("input.txt") as f:
            self.data = f.read()

    def part1(self):
        print("Part 1")
        print(self.data)

        ops_strings = re.findall(r"mul\(\d+,\d+\)", self.data)

        ops = [re.findall(r"\d+", op) for op in ops_strings]

        total = sum([int(op[0]) * int(op[1]) for op in ops])

        print(total)

    def part2(self):
        print("Part 2")

        ops_strings = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", self.data) # type: ignore

        multiply = True
        total = 0
        for op in ops_strings:

            match op:
                case "do()":
                    multiply = True
                case "don't()":
                    multiply = False
                case _:
                    if multiply:
                        nums = re.findall(r"\d+", op) 
                        total += int(nums[0]) * int(nums[1])


        print(ops_strings)
        print(total)


challenge = Challenge()

# challenge.part1()
challenge.part2()
