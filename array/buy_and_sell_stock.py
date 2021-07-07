"""

Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be
made by buying and then selling one share of that stock. There is not need to buy if no profit is possible.

Complexities:
    Time: O(N)
    Space: O(1)

"""


def buy_and_sell(prices):
    min_so_far, max_profit = prices[0], 0

    for price in prices[1:]:
        max_profit_today = price - min_so_far
        max_profit = max(max_profit, max_profit_today)
        min_so_far = min(min_so_far, price)

    return max_profit


if __name__ == "__main__":
    print(buy_and_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
