"""

Maximum value contiguous subsequence:
[-2, 11, -4, 13, -5, 2] -> 11, -4, 13 -> 20
[1, -3, 4, -2, -1, 6] -> 4, -2, -1, 6 -> 7

Complexities:
    Time: O(N)
    Space: O(1)

"""


def max_subarray_sum(inp_array):
    max_sum = inp_array[0]

    for i in range(1, len(inp_array)):
        inp_array[i] = max(inp_array[i-1] + inp_array[i], inp_array[i])
        max_sum = max(max_sum, inp_array[i])

    return max_sum


if __name__ == "__main__":
    input_array1 = [-2, 11, -4, 13, -5, 2]
    print(max_subarray_sum(input_array1))
    input_array2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(input_array2))
