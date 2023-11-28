from enum import Enum


score: int = 0
draw: int = 3
win: int = 6
rock: int = 1
paper: int = 2
scissor: int = 3


class Guess(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSOR = "C"
    Loss = "X"
    Draw = "Y"
    Win = "Z"


with open("input_2.txt", "r") as f:
    for line in f.readlines():
        split: list[str] = line.strip().split(" ")

        points = 0
        print(split)

        match split:
            case [Guess.ROCK.value, Guess.Loss.value]:
                points = scissor
            case [Guess.ROCK.value, Guess.Draw.value]:
                points = draw + rock
            case [Guess.ROCK.value, Guess.Win.value]:
                points = win + paper
            case [Guess.PAPER.value, Guess.Draw.value]:
                points = draw + paper
            case [Guess.PAPER.value, Guess.Loss.value]:
                points = rock
            case [Guess.PAPER.value, Guess.Win.value]:
                points = win + scissor
            case [Guess.SCISSOR.value, Guess.Win.value]:
                points = win + rock
            case [Guess.SCISSOR.value, Guess.Loss.value]:
                points = paper
            case [Guess.SCISSOR.value, Guess.Draw.value]:
                points = draw + scissor
            case _:
                print("No match. Stopping the program")
                break

        score = score + points

print(f"Got a total of {score}")
