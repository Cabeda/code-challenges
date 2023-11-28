from main import Solution

sol = Solution()

import timeit


def test_maxprofit():
    timeit.timeit(sol.maxProfit([7, 6, 4, 3, 1]), number=10)
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

def test_maxprofit_2():
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5