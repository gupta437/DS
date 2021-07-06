"""

write a program that takes a final score and scores for individual plays, and returns the num of combinations
of plays that result in the final score.


similar to coin change
You are given an integer array coins representing coins of different denominations and an
integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot
be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Complexities:
    Time: O(#scores*#final_score)
    Space: O(#final_Score + 1)

"""


def num_of_combinations(final_score, scores):
    memo = [0] * (final_score+1)
    memo[0] = 1

    for use_score in scores:
        for score in range(use_score, final_score+1):
            memo[score] += memo[score - use_score]

    return memo[-1]


if __name__ == "__main__":
    total_Score = 12
    scores = [2, 3, 7]
    print(num_of_combinations(total_Score, scores))