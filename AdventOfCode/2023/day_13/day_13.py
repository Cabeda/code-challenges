
class Challenge_13:
    def parse_file(self, file_name: str = "input_test.txt"):
        with open(file_name, "r") as file:
            for line in file:
                yield line.strip()


challenge = Challenge_13()
lines = challenge.parse_file()

[line for line in lines]
