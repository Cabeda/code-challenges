class Challenge2:
    def maxCheck(self, ball, type, max):
        if type in ball:
            value = int(ball.replace(type, "").strip())
            if value > max:
                return False, value
            else:
                return True, value

    def challenge1(self, fileName="inputs/input_2_1.txt"):
        blue_max = 14
        red_max = 12
        green_max = 13

        total = 0
        total_min = 0
        with open(fileName, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    print(line)
                    game, result = line.split(":")
                    gameNumber = int(game.replace("Game ", ""))
                    valid = True
                    blue_min = 0
                    red_min = 0
                    green_min = 0

                    sets = result.split(";")

                    for set in sets:
                        balls = set.split(",")

                        for ball in balls:
                            if "green" in ball:
                                is_valid, value = self.maxCheck(
                                    ball, "green", green_max
                                )
                                if value > green_min:
                                    green_min = value
                            elif "blue" in ball:
                                is_valid, value = self.maxCheck(ball, "blue", blue_max)
                                if value > blue_min:
                                    blue_min = value
                            elif "red" in ball:
                                is_valid, value = self.maxCheck(ball, "red", red_max)
                                if value > red_min:
                                    red_min = value
                            
                            valid = valid and is_valid

                    if valid:
                        total += gameNumber

                    print(
                        f"Valid: {valid}: Could have played with red: {red_min}, green: {green_min}, blue: {blue_min}"
                    )
                    total_min += blue_min * red_min * green_min

        return total, total_min


if __name__ == "__main__":
    challenge = Challenge2()
    # total_1 = challenge.challenge1()
    total, total_min = challenge.challenge1()

    # print("total: ", total_1)
    print(f"total test: {total} and total min: {total_min}")
