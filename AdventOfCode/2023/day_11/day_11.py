class Challenge_11:
    def find_stars(self, map: list[list[str]]):
        stars = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "#":
                    stars.append((i, j))
        return stars
    
    def find_stars_2(self, map: list[list[str]], star_rows: set[int], star_cols: set[int], gravity: int = 2):
        stars = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "#":
                    prev_rows = [star for star in star_rows if star < i]
                    prev_cols = [star for star in star_cols if star < j]
                    row_gravity = gravity * len(prev_rows) - len(prev_rows)
                    col_gravity = gravity * len(prev_cols) - len(prev_cols)

                    stars.append((i+row_gravity, j + col_gravity))
        return stars

    def parse_file(self, file_name: str = "AdventOfCode/2023/day_11/input_test.txt"):
        map: list[list[str]] = []
        star_cols: set[int] = set()
        star_rows: set[int] = set()

        with open(file_name, "r") as file:
            line_num = 0
            for line in file:
                symbols = set(line.strip())
                chars = list(line.strip())
                map.append(chars)

                stars_indexes = set([i for i, x in enumerate(chars) if x == "#"])

                if len(stars_indexes) > 0:
                    star_cols = stars_indexes.union(star_cols)

                if len(symbols) == 1:
                        star_rows.add(line_num)
                        # map.append(chars)
                line_num += 1

        missing_cols = set([x for x in range(len(map[0])) if x not in star_cols])
        

        return map, star_rows, missing_cols

    def get_distance(self, star_a: tuple[int, int], star_b: tuple[int, int]):
        a = (star_a[0] + 1, star_a[1] + 1)
        b = (star_b[0] + 1, star_b[1] + 1)

        distance = abs(b[0] - a[0]) + abs(b[1] - a[1])
        print(f"Distance between {a} and {b} is {distance}")
        return distance

    def challenge(self, star_map: list[tuple[int, int]]):
        total_distance = 0
        for i in range(len(star_map) - 1):
            for j in range(i + 1, len(star_map)):
                print(f"Galaxy {i+ 1} and {j+ 1}")
                total_distance += self.get_distance(star_map[i], star_map[j])

        return total_distance


challenge = Challenge_11()

map, star_rows, star_cols = challenge.parse_file("AdventOfCode/2023/day_11/input.txt")
# star_map = challenge.find_stars(map)
star_map = challenge.find_stars_2(map, star_rows, star_cols, gravity=1000000)

print(star_map)

total_distance = challenge.challenge(star_map)

print(total_distance)
