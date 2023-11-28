import { assertEquals } from "https://deno.land/std@0.201.0/assert/mod.ts";
// # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// # You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// # Runtime: 68ms (faster than 89.79%)
// # Memory: 50.96 MB (beats 98.42%)

function maxProfit(prices: number[]): number {
  let min = prices[0];
  let diff = 0;

  for (let i of prices) {
    if (i < min) {
      min = i;
      continue;
    }
    if (i - min > diff) {
      diff = i - min;
    }
  }
  return diff;
}

Deno.test("test simple stock", () => {
  const result1 = maxProfit([7, 1, 5, 3, 6, 4]);

  assertEquals(result1, 5);
});
