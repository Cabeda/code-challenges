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
            if seed >= converter.source and seed <= converter.source + converter.range:
                return  converter.destination + seed - converter.source
        return seed
    
    def seed_to_location(self, converters, seed):
        soil_converters = [converter for converter in converters if converter.category == Category.soil]
        soil = self.conversion(seed, soil_converters)
        print(f"Converted seed {seed} to soil {soil}")
        fertilizer_converters = [converter for converter in converters if converter.category == Category.fertilizer]
        fertilizer = self.conversion(soil, fertilizer_converters)
        print(f"Converted soil {soil} to fertilizer {fertilizer}")
        water_converters = [converter for converter in converters if converter.category == Category.water]
        water = self.conversion(fertilizer, water_converters)
        print(f"Converted fertilizer {fertilizer} to water {water}")
        light_converters = [converter for converter in converters if converter.category == Category.light]
        light = self.conversion(water, light_converters)
        print(f"Converted water {water} to light {light}")
        temperature_converters = [converter for converter in converters if converter.category == Category.temperature]
        temperature = self.conversion(light, temperature_converters)
        print(f"Converted light {light} to temperature {temperature}")
        humidity_converters = [converter for converter in converters if converter.category == Category.humidity]
        humidity = self.conversion(temperature, humidity_converters)
        print(f"Converted temperature {temperature} to humidity {humidity}")
        location_converters = [converter for converter in converters if converter.category == Category.location]
        location = self.conversion(humidity, location_converters)
        print(f"Converted humidity {humidity} to location {location}")

        return location


    def challenge_1(self, mapper: Mapper):
        min = mapper.seeds[0]

        for seed in mapper.seeds:
            location = self.seed_to_location(mapper.converters, seed)

            if location < min:
                min = location

        print(min)


    def challenge_2(self, mapper: Mapper):
        min = None
        location = None
    
        for i in range(0, len(mapper.seeds), 2):
            print(f"Start range {mapper.seeds[i]}:{mapper.seeds[i] + mapper.seeds[i+1]}")
            for seed in  range(mapper.seeds[i], mapper.seeds[i] + mapper.seeds[i+1]):
                location = self.seed_to_location(mapper.converters, seed)
                if not min or location < min:
                    min = location

        print(min)
        



if __name__ == "__main__":
    challenge = Challenge()
    mapper = challenge.parse_file("AdventOfCode/2023/day_5/input.txt")
    #challenge.challenge_1(mapper)
    challenge.challenge_2(mapper)