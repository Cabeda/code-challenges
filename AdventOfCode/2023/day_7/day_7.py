import functools
from dataclasses import dataclass
from enum import Enum
from typing import Counter


class Play(Enum):
    FIVE_OF_A_KIND = 0
    FOUR_OF_A_KIND = 1
    FULL_HOUSE = 2
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 4
    ONE_PAIR = 5
    HIGH = 6


@dataclass
class Hand:
    cards: list[str]
    points: int
    jokerMode: bool = False
    play: Play = Play.HIGH

    def __init__(self, cards: list[str], points: int, jokerMode: bool = False):
        self.cards = cards
        self.points = points
        self.jokerMode = jokerMode
        self.update_play(jokerMode)

    def joker_converter(self):
        jokers = self.cards.count("J")
        hand = [c for c in self.cards if c != 'J']
        counts = sorted(Counter(hand).values(), reverse=True)
        if jokers > 0:

            if jokers == 5:
                self.play = Play.FIVE_OF_A_KIND
            elif counts[0] + jokers == 5:
                self.play = Play.FIVE_OF_A_KIND
            elif counts[0] + jokers == 4:
                self.play = Play.FOUR_OF_A_KIND
            elif counts[0] + jokers == 3 and counts[1] == 2:
                self.play = Play.FULL_HOUSE
            elif counts[0] + jokers == 3:
                self.play = Play.THREE_OF_A_KIND
            elif counts[0] == 2 and (jokers or counts[1] == 2):
                self.play = Play.TWO_PAIRS
            elif counts[0] == 2 or jokers:
                self.play = Play.ONE_PAIR
                
            
            

    def update_play(self, jokerMode = False):
        cards = set(self.cards)
        if len(cards) == 1:
            self.play = Play.FIVE_OF_A_KIND
        elif len(cards) == 2:
            if (
                self.cards.count(self.cards[0]) == 2
                or self.cards.count(self.cards[1]) == 2
                or self.cards.count(self.cards[2]) == 2
                or self.cards.count(self.cards[4]) == 2
            ):
                self.play = Play.FULL_HOUSE
            else:
                self.play = Play.FOUR_OF_A_KIND
        elif len(cards) == 3:
            if (
                self.cards.count(self.cards[0]) == 3
                or self.cards.count(self.cards[1]) == 3
                or self.cards.count(self.cards[2]) == 3
            ):
                self.play = Play.THREE_OF_A_KIND
            else:
                self.play = Play.TWO_PAIRS
        elif len(cards) == 4:
            self.play = Play.ONE_PAIR
        else:
            self.play = Play.HIGH

        if jokerMode:
            self.joker_converter()




class Challenge_7:
    def parse_file(self, file_name, jokerMode: bool = False) -> list[Hand]:
        hands: list[Hand] = []
        with open(file_name) as file:
            for line in file:
                hand, points = line.split(" ")
                cards = [c for c in hand]
                hands.append(Hand(cards, int(points), jokerMode))

        return hands

    def get_card_value(self, card: str, jokerMode: bool) -> int:
        if card == "A":
            return 14
        elif card == "K":
            return 13
        elif card == "Q":
            return 12
        elif card == "J":
            if jokerMode:
                return 1
            else:
                return 11
        elif card == "T":
            return 10
        else:
            return int(card)

    def compare_hands(self, hand_1: Hand, hand_2: Hand) -> int:
        if hand_1.play.value > hand_2.play.value:
            return -1
        elif hand_1.play.value < hand_2.play.value:
            return 1
        else:
            # Same points, check cards one by one
            for i in range(len(hand_1.cards)):
                hand_1_card_value = self.get_card_value(hand_1.cards[i], hand_1.jokerMode)
                hand_2_card_value = self.get_card_value(hand_2.cards[i], hand_2.jokerMode)
                if hand_1_card_value < hand_2_card_value:
                    return -1
                elif hand_1_card_value > hand_2_card_value:
                    return 1
        return 0

    def challenge(self, hands: list[Hand]):
        sorted_hands = sorted(hands, key=functools.cmp_to_key(self.compare_hands))

        total = 0
        for i in range(len(sorted_hands)):
            print(
                f"{''.join(sorted_hands[i].cards)} -> {sorted_hands[i].play}: {sorted_hands[i].points} * {i + 1}"
            )
            total += sorted_hands[i].points * (i + 1)

        print(total)
        return total

    def challenge_2(self, hands: list[Hand]):
        sorted_hands = sorted(hands, key=functools.cmp_to_key(self.compare_hands))

        total = 0
        for i in range(len(sorted_hands)):
            print(
                f"{''.join(sorted_hands[i].cards)} -> {sorted_hands[i].play}: {sorted_hands[i].points} * {i + 1}"
            )
            total += sorted_hands[i].points * (i + 1)

        print(total)
        return total


if __name__ == "__main__":
    challenge = Challenge_7()
    # file = challenge.parse_file("AdventOfCode/2023/day_7/input_test.txt")
    # challenge.challenge(file)
    # file_test_2 = challenge.parse_file("AdventOfCode/2023/day_7/input_test.txt", jokerMode=True)
    # challenge.challenge_2(file_test_2)
    
    file_2 = challenge.parse_file("AdventOfCode/2023/day_7/input.txt", jokerMode=True)
    challenge.challenge_2(file_2)

