from copy import copy


class Challenge_13:
    def parse_file(self, file_name: str = "input_test.txt"):
        lines = []
        with open(file_name, "r") as file:
            for line in file:
                lines.append(line.strip())

        return lines

    def get_column(self, line: list[str], col_index: int) -> str:
        list_chars = [row[col_index] for row in line]

        return "".join(list_chars)

    def flip_vertical(self, lines: list[str]) -> list[str]:
        """Flip the lines vertically."""

        dataset = []
        for i in range(len(lines[0])):
            dataset.append(self.get_column(lines, i))

        return dataset

    def retrieve_dataset(self, lines: list[str]):
        """Return two lists, the lists are separated by an empty line (\n)."""
        datasets: list[list[str]] = []

        dataset: list[str] = []

        for line in lines:
            if line == "":
                datasets.append(copy(dataset))
                dataset = []
                continue

            dataset.append(line)

        datasets.append(copy(dataset))

        return datasets

    def find_duplicate_line(self, lines: list[str]) -> int:
        """Find the duplicate line in the list of lines."""
        # if lines[0] == lines[len(lines) - 1]:
        #     return 1

        for i in range(len(lines) - 1):
            if lines[i] == lines[i + 1]:
                return i + 1
        return 0
    
    def find_reflected_rows(self, grid, smudges=0):
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]

            # Checking if there is exactly a certain amount of smudges (a difference between
            # corresponding elements) between the rows `above` and `below`. It does this by iterating over
            # each pair of corresponding elements in `above` and `below` and counting the number of
            # differences. If the count is equal to smudges, it means there is exactly that amount of smudges
            if (
                sum(
                    sum(0 if a == b else 1 for a, b in zip(x, y))
                    # x, y are the rows
                    for x, y in zip(above, below)
                )
                == smudges
            ):
                return r

        return 0

    
    def print_dataset(self, dataset: list[str], col_index: int = 0, is_vertical: bool = False):

        if is_vertical:
            row = ""
            for i in range(len(dataset[0])):
                if i == col_index -1:
                    row += "v"
                else:
                    row += "*"
            print(f"{col_index} to the left")
            print(row)
            
        for i in range(len(dataset)):
            print(dataset[i])

            if i == col_index -1 and not is_vertical:
                print(f"v {col_index} to the top")
        print("\n\n")

challenge = Challenge_13()
lines = challenge.parse_file("day_13/input.txt")

datasets = challenge.retrieve_dataset(lines)

vertical_nums: list[int] = []
horizontal_nums: list[int] = []

solution1 = 0
solution2 = 0
for horizontal in datasets:
    solution1 += challenge.find_reflected_rows(horizontal) * 100
    solution2 += challenge.find_reflected_rows(horizontal, 1) * 100
    
    block = list(zip(*horizontal))
    vertical = challenge.flip_vertical(horizontal)
    solution1 += challenge.find_reflected_rows(block)
    solution2 += challenge.find_reflected_rows(block, 1)

print(solution1)
print(solution2)

