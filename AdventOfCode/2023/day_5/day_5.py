from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    soil = "seed-to-soil map:"
    fertilizer = "soil-to-fertilizer map:"
    water = "fertilizer-to-water map:"
    light = "water-to-light map:"
    temperature = "light-to-temperature map:"
    humidity = "temperature-to-humidity map:"
    location = "humidity-to-location map:"

@dataclass
class Converter:
    category: Category
    source: int
    destination: int
    range: int


class Mapper:
    seeds: list[int]
    converters: list[Converter] = []

class Challenge():
    def parse_file(self,file_name: str) -> Mapper:
        mapper = Mapper()
        with open(file_name) as f:
            category: Category
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                if line.lower().startswith("seeds:"):
                    nums = line.split(":")[1].strip().split(" ")
                    mapper.seeds = [int(num) for num in nums]
                    continue
                
                match line.lower():
                    case Category.soil.value:
                        category = Category.soil
                        continue
                    case Category.fertilizer.value:
                        category = Category.fertilizer
                        continue
                    case Category.water.value:
                        category = Category.water
                        continue
                    case Category.light.value:
                        category = Category.light
                        continue
                    case Category.temperature.value:
                        category = Category.temperature
                        continue
                    case Category.humidity.value:
                        category = Category.humidity
                        continue
                    case Category.location.value:
                        category = Category.location
                        continue
                    
                destination, source, range = line.split(" ")
                mapper.converters.append(Converter(category, int(source), int(destination), int(range)))

        return mapper
    
    def conversion(self, seed, converters: list[Converter]):
        for converter in converters:
            if converter.source >= seed <= converter.source + converter.range:
                return  converter.destination + seed - converter.source
        return seed
    
    def seed_to_location(self, converters: dict[Category, list], seed):
        soil = self.conversion(seed, converters[Category.soil])
        # print(f"Converted seed {seed} to soil {soil}")
        fertilizer = self.conversion(soil, converters[Category.fertilizer])
        # print(f"Converted soil {soil} to fertilizer {fertilizer}")
        water = self.conversion(fertilizer, converters[Category.water])
        # print(f"Converted fertilizer {fertilizer} to water {water}")
        light = self.conversion(water, converters[Category.light])
        # print(f"Converted water {water} to light {light}")
        temperature = self.conversion(light, converters[Category.temperature])
        # print(f"Converted light {light} to temperature {temperature}")
        humidity = self.conversion(temperature, converters[Category.humidity])
        # print(f"Converted temperature {temperature} to humidity {humidity}")
        location = self.conversion(humidity, converters[Category.location])
        # print(f"Converted humidity {humidity} to location {location}")

        return location


    def challenge_1(self, mapper: Mapper):
        min = mapper.seeds[0]

        converters_dict: dict[Category, list] = {category: [] for category in Category}
        for converter in mapper.converters:
            converters_dict[converter.category].append(converter)

        for seed in mapper.seeds:
            location = self.seed_to_location(converters_dict, seed)

            if location < min:
                min = location
                print(f"New min: {min}")

        print(min)


    def challenge_2(self, mapper: Mapper):
        min = None
        location = None

        converters_dict: dict[Category, list] = {category: [] for category in Category}
        for converter in mapper.converters:
            converters_dict[converter.category].append(converter)
    
        for i in range(0, len(mapper.seeds), 2):
            print(f"Start range {mapper.seeds[i]}:{mapper.seeds[i] + mapper.seeds[i+1]}")
            for seed in  range(mapper.seeds[i], mapper.seeds[i] + mapper.seeds[i+1]):
                location = self.seed_to_location(converters_dict, seed)
                if not min or location < min:
                    min = location
                    print(f"New min: {min}")

        print(min)
        



if __name__ == "__main__":
    challenge = Challenge()
    mapper = challenge.parse_file("AdventOfCode/2023/day_5/input.txt")
    #challenge.challenge_1(mapper)
    challenge.challenge_2(mapper)