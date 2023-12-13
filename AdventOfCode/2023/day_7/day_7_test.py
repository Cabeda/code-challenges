from day_7 import Challenge_7, Hand, Play

challenge = Challenge_7()


def test_card_values():
    assert challenge.get_card_value("A", False) == 14
    assert challenge.get_card_value("K", False) == 13
    assert challenge.get_card_value("Q", False) == 12
    assert challenge.get_card_value("J", False) == 11
    assert challenge.get_card_value("T", False) == 10
    assert challenge.get_card_value("9", False) == 9
    assert challenge.get_card_value("8", False) == 8
    assert challenge.get_card_value("7", False) == 7
    assert challenge.get_card_value("6", False) == 6
    assert challenge.get_card_value("5", False) == 5
    assert challenge.get_card_value("4", False) == 4
    assert challenge.get_card_value("3", False) == 3
    assert challenge.get_card_value("2", False) == 2
    assert challenge.get_card_value("A", True) == 14
    assert challenge.get_card_value("K", True) == 13
    assert challenge.get_card_value("Q", True) == 12
    assert challenge.get_card_value("T", True) == 10
    assert challenge.get_card_value("9", True) == 9
    assert challenge.get_card_value("8", True) == 8
    assert challenge.get_card_value("7", True) == 7
    assert challenge.get_card_value("6", True) == 6
    assert challenge.get_card_value("5", True) == 5
    assert challenge.get_card_value("4", True) == 4
    assert challenge.get_card_value("3", True) == 3
    assert challenge.get_card_value("2", True) == 2
    assert challenge.get_card_value("J", True) == 1

def test_card_hands():
    hand = Hand(["A","A","A","A","A"], 50)
    assert hand.play == Play.FIVE_OF_A_KIND
    
    hand = Hand(["J","A","A","A","A"], 50)
    assert hand.play == Play.FOUR_OF_A_KIND
    
    hand = Hand(["J","J","A","A","A"], 50)
    assert hand.play == Play.FULL_HOUSE

    hand = Hand(["8","J","A","A","A"], 50)
    assert hand.play == Play.THREE_OF_A_KIND
    
    hand = Hand(["J","J","9","A","A"], 50)
    assert hand.play == Play.TWO_PAIRS
    
    hand = Hand(["J","J","9","8","A"], 50)
    assert hand.play == Play.ONE_PAIR
    
    hand = Hand(["J","K","A","9","8"], 50)
    assert hand.play == Play.HIGH

def test_card_hands_joker():
    
    hand = Hand(["J","A","A","A","A"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

    hand = Hand(["J","J","A","A","A"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

    hand = Hand(["J","J","A","A","A"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

    hand = Hand(["J","J","J","J","J"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND
    
    hand = Hand(["J","K","A","9","8"], 50, True)
    assert hand.play == Play.ONE_PAIR
    
    hand = Hand(["J","K","A","A","8"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["J","K","A","A","K"], 50, True)
    assert hand.play == Play.FULL_HOUSE
    
    hand = Hand(["A","J","A","A","K"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND

    hand = Hand(["A","A","8","K","J"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["K","T","J","J","T"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND

    hand = Hand(["K","5","3","J","T"], 50, True)
    assert hand.play == Play.ONE_PAIR

    hand = Hand(["A","9","J","K","9"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["5","J","A","6","J"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["9","2","J","2","Q"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["J","7","6","7","6"], 50, True)
    assert hand.play == Play.FULL_HOUSE

    hand = Hand(["J","Q","2","K","K"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["7","2","J","2","7"], 50, True)
    assert hand.play == Play.FULL_HOUSE

    hand = Hand(["5","J","2","T","5"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["T","T","T","8","J"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND

    hand = Hand(["4","J","8","4","4"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND

    hand = Hand(["J","J","J","J","K"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

def test_card_hands_joker_high():

    hand = Hand(["6","T","9","Q","J"], 50, True)
    assert hand.play == Play.ONE_PAIR

    hand = Hand(["T","9","A","J","4"], 50, True)
    assert hand.play == Play.ONE_PAIR

    hand = Hand(["T","Q","K","J","7"], 50, True)
    assert hand.play == Play.ONE_PAIR

def test_card_hands_joker_one_pair():

    hand = Hand(["6","6","9","Q","J"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["Q","7","4","J","4"], 50, True)
    assert hand.play == Play.THREE_OF_A_KIND

    hand = Hand(["T","T","J","J","4"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND

    hand = Hand(["T","T","J","J","J"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

def test_card_hands_joker_two_pair():

    hand = Hand(["6","6","9","9","J"], 50, True)
    assert hand.play == Play.FULL_HOUSE

def test_card_hands_joker_three():

    hand = Hand(["6","6","9","J","J"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND
    
    hand = Hand(["6","6","6","J","J"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

def test_card_hands_joker_full_house():

    hand = Hand(["6","6","J","J","J"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

    hand = Hand(["6","6","6","K","K"], 50, True)
    assert hand.play == Play.FULL_HOUSE


def test_card_hands_joker_four():
    hand = Hand(["A","J","J","Q","J"], 50, True)
    assert hand.play == Play.FOUR_OF_A_KIND

    hand = Hand(["6","6","6","6","J"], 50, True)
    assert hand.play == Play.FIVE_OF_A_KIND

def test_challenge_1():
    file_test = challenge.parse_file("AdventOfCode/2023/day_7/input_test.txt", jokerMode=False)
    assert challenge.challenge(file_test) == 6440
    
    file = challenge.parse_file("AdventOfCode/2023/day_7/input.txt", jokerMode=False)
    assert challenge.challenge(file) == 251216224

def test_challenge_2():
    file_test = challenge.parse_file("AdventOfCode/2023/day_7/input_test.txt", jokerMode=True)
    assert challenge.challenge_2(file_test) == 5905

    file = challenge.parse_file("AdventOfCode/2023/day_7/input.txt", jokerMode=True)
    assert challenge.challenge_2(file) == 250825971
