"""


Complexities:
    Time: O(m*n)
    Space: O((m+1)(n+1))

"""


def edit_distance(str1, str2):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    memo = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

    for str2_idx in range(0, len(str2)+1):
        memo[0][str2_idx] = str2_idx

    for str1_idx in range(0, len(str1)+1):
        memo[str1_idx][0] = str1_idx

    for str1_idx in range(1, len(memo)):
        for str2_idx in range(1, len(memo[0])):
            if str1[str1_idx-1] == str2[str2_idx-1]:
                memo[str1_idx][str2_idx] = memo[str1_idx-1][str2_idx-1]
            else:
                memo[str1_idx][str2_idx] = \
                    min(memo[str1_idx-1][str2_idx], memo[str1_idx][str2_idx-1], memo[str1_idx-1][str2_idx-1]) + 1

    return memo[len(str1)][len(str2)]


def main():
    inp1 = ""
    inp2 = "Carthorse"
    print(edit_distance(inp1, inp2))


if __name__ == "__main__":
    main()