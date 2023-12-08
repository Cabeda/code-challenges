from dataclasses import dataclass
from re import search


@dataclass
class Point():
    x: int
    y: int
    
class Challenge:
    def challenge_1(self):
        with open("AdventOfCode/2023/day_3/input_test.txt", "r") as f:
            lines = [[*line] for line in f.readlines()]

            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    if search(r"(\d|\.)", lines[i][j]):
                        print(f"Found {lines[i][j]} at {i}, {j}")
                    elif lines[i][j] != "\n":
                        print(f"Found {lines[i][j]} at {i}, {j}")
                        if search(r"(\d|\.)", lines[i-1][j]):
                            print("Found valid number")
                        if search(r"(\d|\.)", lines[i-1][j-1]):
                            print("Found valid number")
                        elif search(r"(\d|\.)", lines[i+1][j]):
                            print("Found valid number")
                        elif search(r"(\d|\.)", lines[i][j-1]):
                            print("Found valid number")
                        elif search(r"(\d|\.)", lines[i][j+1]):
                            print("Found valid number")
                        elif search(r"(\d|\.)", lines[i+1][j+1]):
                            print("Found valid number")
                        elif search(r"(\d|\.)", lines[i-1][j+1]):
                            print("Found valid number")
                        elif search(r"(\d|\.)", lines[i+1][j-1]):
                            print("Found valid number")

            

if __name__ == "__main__":
    challenge = Challenge()
    challenge.challenge_1()