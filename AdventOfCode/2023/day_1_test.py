from day_1 import Challenge_1


def test_texttoint():
    challenge = Challenge_1()
    assert challenge.textToNum("one") == "1"
    assert challenge.textToNum("two") == "2"
    assert challenge.textToNum("three") == "3"
    assert challenge.textToNum("four") == "4"
    assert challenge.textToNum("five") == "5"
    assert challenge.textToNum("six") == "6"
    assert challenge.textToNum("seven") == "7"
    assert challenge.textToNum("eight") == "8"
    assert challenge.textToNum("nine") == "9"


def test_multipleNumbers():
    challenge = Challenge_1()
    assert challenge.textToNum("nineone") == "91"
    assert challenge.textToNum("oneone") == "11"
    assert challenge.textToNum("twothree") == "23"

def test_multipleNumbersWithGarbage():
    challenge = Challenge_1()
    assert challenge.textToNum("4nineeightdgfseven2") == "498dgf72"

def test_challenge_1():
    challenge = Challenge_1()
    assert challenge.challenge_1("AdventOfCode/2023/inputs/input_1_1_test.txt") == 142

def test_challenge_2():
    challenge = Challenge_1()

    assert challenge.textToNum("two1nine") == "219"
    assert challenge.textToNum("eightwothree") == "823"
    assert challenge.textToNum("abcone2threexyz") == "abc123xyz"
    assert challenge.textToNum("xtwone3four") == "x2134"
    assert challenge.textToNum("4nineeightseven2") == "49872"
    assert challenge.textToNum("zoneight234") == "z18234"
    assert challenge.textToNum("7pqrstsixteen") == "7pqrst6teen"


    assert challenge.removeLetters("219") == 29
    assert challenge.removeLetters("8wo3") == 83
    assert challenge.removeLetters("abc123xyz") == 13
    assert challenge.removeLetters("x2ne34") == 24
    assert challenge.removeLetters("49872") == 42
    assert challenge.removeLetters("z1ight234") == 14 
    assert challenge.removeLetters("7pqrst6teen") == 76

    assert challenge.challenge_2("AdventOfCode/2023/inputs/input_1_2_test.txt") == 281
