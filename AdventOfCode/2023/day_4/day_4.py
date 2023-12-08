from dataclasses import dataclass


@dataclass
class Game:
    game_number: int
    win_numbers: list[int]
    numbers: list[int]
    total_wins: int = 0


class Challenge4:

    def getGameNumbers(self, lineText: str):
        game_title, result = lineText.split(":")
        game_num = int(game_title.replace("Card ", "").strip())
        game = Game(game_num, [], [])
        win_numbers, numbers = result.split("|")
        game.win_numbers = [
            int(number)
            for number in win_numbers.split(" ")
            if number.strip() != ""
        ]
        game.numbers = [
            int(number)
            for number in numbers.split(" ")
            if number.strip() != ""
        ]
        return game
    
    def countWinNumbers(self, game: Game):
        count = 0
        for number in game.numbers:
            if number in game.win_numbers:
                if count == 0:
                    count = 1
                else:
                    count *= 2
        return count

    def countWinNumbersNoDup(self, game: Game):
        count = 0
        for number in game.numbers:
            if number in game.win_numbers:
                    count += 1
        return count

    def challenge1(self, fileName="AdventOfCode/2023/day_4/input.txt"):
        total = 0
        games = []
        with open(fileName, "r") as f:
            for line in f:
                line = line.strip()

                if line:
                    # print(line)
                    game = self.getGameNumbers(line)
                    total += self.countWinNumbers(game)
                    game.total_wins += self.countWinNumbersNoDup(game)
                    games.append(game)

        return games, total 
    
    def countWinNumbers2(self, games: list[Game], game: Game) -> int:
        total = 1
        if game.total_wins > 0:
            start = game.game_number
            end = game.game_number + game.total_wins
            for i in range(start, end):
                # print(f"Count for card {i}")
                if i < len(games):
                    total += self.countWinNumbers2(games, games[i])
        return total
                
    
    def challenge2(self, games: list[Game]):
        total = 0
        for game in games:
                total_scratchboards = self.countWinNumbers2(games, game)
                total += total_scratchboards
                print(f"Total scratchboards for card {game.game_number}: {total_scratchboards}. Total: {total}")
        return total



if __name__ == "__main__":
    challenge = Challenge4()
    games, total = challenge.challenge1("AdventOfCode/2023/day_4/input.txt")
    total_scratchboards = challenge.challenge2(games)
    print(total)
    print(total_scratchboards)
