"""

Complexities:
    Time: O(N^2)
    Space: O(N)

"""


def number_of_ways_traverse_2d_matrix(rows,cols):
    if rows == cols == 0:
        return 1

    memo = [1] * cols

    for row_idx in range(1, rows):
        for col_idx in range(1, cols):
            memo[col_idx] += memo[col_idx-1]

    return memo[-1]


if __name__ == "__main__":
    print(number_of_ways_traverse_2d_matrix(4, 4))
