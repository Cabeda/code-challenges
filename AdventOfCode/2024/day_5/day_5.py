import pathlib

class Challenge_5:
    def __init__(self):
        self.data: list[list[str]] = []
        self.load_data()
        self.part1()
        self.part2()

    def load_data(self):
        # Get file path
        file_path = pathlib.Path(__file__).parent / "input_test.txt"
        with open(file_path) as f:
            self.data = [list(line) for line in f.read().splitlines()]

    def part1(self):
        print("Part 1")

    def part2(self):
        print("Part 2")


challenge = Challenge_5()
