# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Runtime: 777ms (faster than 97.62%)
# Memory: 27.25MB (beats 89.97%)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[0]
        diff = 0

        for i in prices:
            if i < min:
                min = i
                continue
            if i - min > diff:
                diff = i - min

        return diff


if __name__ == '__main__':  
    sol = Solution()


    # results = timeit.repeat(lambda: sol.maxProfit([7, 6, 4, 3, 1]), repeat=100, number=10000)

    # import statistics
    # print(statistics.fmean(results)*1000)

    # import cProfile
    # cProfile.run('sol.maxProfit([7, 6, 4, 3, 1])')

    sol.maxProfit([7, 6, 4, 3, 1])