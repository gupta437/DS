"""

Given an array nums of non-negative integers, return an array consisting of all the even elements of nums,
followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

Complexities:
    Time: O(N)
    Space: O(1)


"""


def sort_by_parity(input_array):
    j = len(input_array) - 1
    i = 0
    while i != j:
        if input_array[i] % 2 == 0:
            i += 1
        else:
            # swap
            input_array[i], input_array[j] = input_array[j], input_array[i]
            j -= 1
    return input_array


if __name__ == "__main__":
    inp_array = [3, 1, 2, 4, 6]
    print(sort_by_parity(inp_array))

