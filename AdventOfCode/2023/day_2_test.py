from day_2 import Challenge2


def test_challenge2():
    challenge = Challenge2()

    result_total, result_min = challenge.challenge1("AdventOfCode/2023/inputs/input_2_test.txt")

    assert result_total == 8
    assert result_min == 2286

def test_challenge2_blue():
    challenge = Challenge2()

    result_total, result_min = challenge.challenge1("AdventOfCode/2023/inputs/input_2_2_test.txt")

    assert result_total == 0
    assert result_min == 1560