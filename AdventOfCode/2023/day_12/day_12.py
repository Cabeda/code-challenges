from concurrent.futures import ProcessPoolExecutor
from functools import cache
from typing import Any, Generator


class Challenge_12:
    def parse_file(self, file_name: str = "AdventOfCode/2023/day_12/input_test.txt"):
        with open(file_name, "r") as file:
            for line in file:
                yield line.strip()

    
    def generate_regex(self, groups_damaged: list[int]) -> str:
        reg: str = "[.]*"
        for group in groups_damaged:
            reg = reg + (group * "#") + "[.]+"

        return reg[:-4] + "[.]*"

    # @lru_cache(maxsize=None)
    # def generate_possibilities(self, regex: str, string: str) -> int:
    #     count = 0

        
    #     if "?" not in string:
    #         return 0

    #     for i in range(len(string)):
    #         if string[i] == "?":
    #             new_string = string
    #             new_string_1 = new_string.replace("?", "#", 1)
    #             new_string_2 = new_string.replace("?", ".", 1)

    #             if fullmatch(regex, new_string_1):
    #                 count += 1
    #             if fullmatch(regex, new_string_2):
    #                 count += 1

    #             count += self.generate_possibilities(
    #                 regex, new_string_2
    #             ) + self.generate_possibilities(regex, new_string_1)

    #     return count

    @cache
    def generate_possibilities(self, string: str) -> set[str]:
        num_question_marks = string.count("?")
        num_possibilities = 2**num_question_marks

        possibilities = set()
        for i in range(num_possibilities):
            binary = bin(i)[2:].zfill(num_question_marks)
            new_string = string
            for b in binary:
                new_string = (
                    new_string.replace("?", "#", 1)
                    if b == "0"
                    else new_string.replace("?", ".", 1)
                )
            possibilities.add(new_string)

        return possibilities

    @cache
    def process_line(self, line, repeat: int = 5):
        springs, group = line.split(" ")
        springs = "?".join([springs] * repeat)
        groups_damaged = [int(val) for val in group.split(",")]
        groups_damaged *= repeat

        print(springs)
        print(groups_damaged)

        regex = self.generate_regex(groups_damaged)

        total = self.generate_possibilities(regex)

        # count_possibilities = 0
        # for string in possibilities:
        #     result = fullmatch(regex, string)
        #     if result is not None:
        #         count_possibilities += 1
        return total

    def challenge(self, lines: Generator[str, Any, None], repeat: int = 1) -> int:
        with ProcessPoolExecutor() as executor:
            results = executor.map(self.process_line, lines)

        return sum(results)


if __name__ == "__main__":
    challenge = Challenge_12()
    lines = challenge.parse_file("AdventOfCode/2023/day_12/input.txt")
    result = challenge.challenge(lines, 5)

    print(result)
