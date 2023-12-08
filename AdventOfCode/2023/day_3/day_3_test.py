from day_3 import Challenge, Num

c = Challenge()



def test_checkValidPosition():
    n = Num(2,2, "123")
    c.check_number_symbol([n], 2,2)
    assert n.is_valid is True

    n = Num(2,2, "123")
    c.check_number_symbol([n], 0,0)
    assert n.is_valid is False

    n = Num(2,2, "123")
    c.check_number_symbol([n], 3,4)
    assert n.is_valid is True

    n = Num(2,2, "123")
    c.check_number_symbol([n], 4,4)
    assert n.is_valid is False

    n = Num(2,2, "123")
    c.check_number_symbol([n], 3,5)
    assert n.is_valid is True

    n = Num(2,2, "123")
    c.check_number_symbol([n], 3,6)
    assert n.is_valid is False