
from main import Solution

sol = Solution()

def test_invalid():
    assert sol.isValid("(){}}{") is False
def test_string():
    sol = Solution()
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("()") is True

def test_incepted():
    assert sol.isValid("({})") is True

def test__multiple_incepted():
    assert sol.isValid("[({(())}[()])]") is True
