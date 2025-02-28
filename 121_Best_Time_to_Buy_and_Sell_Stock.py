# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#______________________
#      INFORMATION
#______________________

"""_summary_
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
#______________________
#      SOLUTION
#______________________
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = float('inf')
        
        for price in prices:
            if price < lowest_price:
                lowest_price = price

            profit = price - lowest_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit

solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([7,1,5,3,6,4]))

# def main():
#     time = input("Please input your time: ")
#     print(convert(time))

# def convert(time):
#     hours, minutes = time.split(":")
#     b_time = "breakast time"
#     l_time = "lunch time"
#     d_time = "dinner_time"

#     # return cases:
#     # Breakfast
#     if hours == "8" and minutes == "0": return(b_time)
#     # Lunch time
#     if hours == "13" and minutes == "0": return(l_time)
#     # dinner time
#     if hours == "19" and minues == "0": return(d_time)

#     # Breakfast time
#     if hours == "7":
#         return minutes_tracker(minutes, b_time)
#     # Lunch time
#     if hours == "12":
#          return minutes_tracker(minutes, l_time)
#     # dinner time
#     if hours == "18":
#          return minutes_tracker(minutes, d_time)

# def minutes_tracker(minutes, meal):
#     if minutes >= "0" and minutes <= "59":
#             return meal
#         else:
#          return None


# if __name__ == "__main__":
#     main()
