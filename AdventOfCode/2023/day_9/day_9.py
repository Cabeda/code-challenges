
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Row():
    values: list[int]

class Challenge_9:
    def parse_file(self, file_name: str = "AdventOfCode/2023/day_9/input_test.txt") -> list[Row]:
        rows: list[Row] = []
        with open(file_name, "r") as file:
            
            for line in file:
                row = Row([int(value) for value in line.strip().split(" ")])
                rows.append(row)
        
        return rows


    def get_diff_row(self, row: list[int]) -> Tuple[int, int]:
        diff_row = []
        prev, after = 0, 0
        for i in range(1, len(row)):
            diff_row.append(row[i] - row[i - 1])

        if sum(diff_row) == 0:
            return row[0], row[-1]
        else:
           prev, after = self.get_diff_row(diff_row)

        return row[0] - prev, row[-1] + after

    def challenge(self, rows: list[Row]) -> Tuple[int, int]:

        prev_values = []
        after_values = []
        for row in rows:
            prev, after = self.get_diff_row(row.values)
            print(prev, after)
            prev_values.append(prev)
            after_values.append(after)
        return sum(prev_values), sum(after_values)

    def challenge_2(self) -> int:
        return 0


if __name__ == "__main__":
    challenge = Challenge_9()

    rows_test = challenge.parse_file()
    result_test =  challenge.challenge(rows_test)
    print(result_test)
    
    rows = challenge.parse_file("AdventOfCode/2023/day_9/input.txt")
    result =  challenge.challenge(rows)
    print(result)
