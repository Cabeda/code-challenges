import pathlib
import re


class Challenge:
    def __init__(self):
        self.data: list[list[str]] = []
        self.load_data()
        self.part1()
        self.part2()

    def load_data(self):
        # Get file path
        file_path = pathlib.Path(__file__).parent / "input.txt"
        with open(file_path) as f:
            self.data = [list(line) for line in f.read().splitlines()]

    def part1(self):
        print("Part 1")
        data = self.data
        total = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if data[i][j] == "X":
                    total += self.search(i, j, (1, 0), "")
                    total += self.search(i, j, (0, 1), "")
                    total += self.search(i, j, (1, 1), "")
                    total += self.search(i, j, (-1, 0), "")
                    total += self.search(i, j, (0, -1), "")
                    total += self.search(i, j, (-1, -1), "")
                    total += self.search(i, j, (1, -1), "")
                    total += self.search(i, j, (-1, 1), "")
        print(total)

    def search(
        self, x: int, y: int, direction: tuple[int, int], word: str, locate_word="XMAS"
    ) -> int:
        if x < 0 or y < 0 or x >= len(self.data) or y >= len(self.data[x]):
            return 0

        total = 0
        word += self.data[x][y]

        if len(re.findall(word, "XMAS")) == 0:
            return 0

        if word == locate_word:
            return 1

        total += self.search(x + direction[0], y + direction[1], direction, word)

        return total

    def part2(self):
        print("Part 2")
        data = self.data
        total = 0
        for i in range(1, len(self.data) - 1):
            for j in range(1, len(self.data[i]) - 1):
                if data[i][j] == "A":
                    try:
                        if data[i + 1][j+ 1] == "S" and data[i - 1][j - 1] == "M" or data[i + 1][j+ 1] == "M" and data[i - 1][j - 1] == "S":
                            if data[i + 1][j + -1] == "M" and data[i - 1][j + 1] == "S" or data[i + 1][j + -1] == "S" and data[i - 1][j + 1] == "M":
                                total += 1
                    except IndexError:
                        pass

        print(total)


challenge = Challenge()
