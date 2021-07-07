"""

Calculate Levenshtein distance
Complexities:
    Time: O(N^2)
    Space: O(N^2)

"""


def calc_levenshtein_distance(string1, string2):
    if not string1:
        return len(string2)

    if not string2:
        return len(string1)

    memo = [[0] * (len(string2)+1) for _ in range(len(string1)+1)]

    for idx in range(len(memo[0])):
        memo[0][idx] = idx

    for idx in range(len(memo)):
        memo[idx][0] = idx

    for row_idx in range(1, len(memo)):
        for col_idx in range(1, len(memo[0])):
            if string1[row_idx-1] == string2[col_idx-1]:
                memo[row_idx][col_idx] = memo[row_idx-1][col_idx-1]
            else:
                memo[row_idx][col_idx] = min(memo[row_idx-1][col_idx-1], memo[row_idx-1][col_idx], memo[row_idx][col_idx-1]) + 1

    return memo[-1][-1]


if __name__ == "__main__":
    inp1 = ""
    inp2 = "Carthorse"
    print(calc_levenshtein_distance(inp1, inp2))


