import functools
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    distance_record: int


class Challenge_6:
    def parse_file(self, file_name) -> list[Race]:
        input: list[str] = []
        races: list[Race] = []
        with open(file_name) as file:
            input = file.readlines()

        race_times = [value for value in input[0].strip().split(":")[1].split(" ") if value != ""]
        distance_records = [value for value in input[1].strip().split(":")[1].split(" ") if value != ""]

        for i in range(len(race_times)):
            race = Race(int(race_times[i]), int(distance_records[i]))
            races.append(race)

        return races

    def challenge(self, races: list[Race]):
        race_options: list[int] = []
        for race in races:
            total_options = 0
            for i in range(1, race.time -1):
                race_time = i * (race.time - i)
                if race_time > race.distance_record:
                    total_options += 1
            race_options.append(total_options)
        
        # multiply all race_options together
        total = functools.reduce(lambda a, b: a*b, race_options)
            
        
        print(total)
            


if __name__ == "__main__":
    challenge = Challenge_6()
    file = challenge.parse_file("AdventOfCode/2023/day_6/input_2.txt")
    challenge.challenge(file)