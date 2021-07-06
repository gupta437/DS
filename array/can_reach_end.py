"""

program rakes an array of n int, where A[i] denotes the max you can advance from index 1, and returns whether it is possible
to advance to thelast index starting from the beginning of the array.

Complexities:
    Time: O(N)
    Space: O(1)

"""


def can_reach_end(inp_array):
    furthest_reach_so_far, last_idx = 0, len(inp_array) - 1
    i = 0

    while i <= furthest_reach_so_far < last_idx:
        furthest_reach_so_far = max(furthest_reach_so_far, inp_array[i] + i)
        i += 1

    return furthest_reach_so_far >= last_idx


if __name__ == "__main__":
    print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
    print(can_reach_end([3, 2, 0, 0, 2, 0, 1]))
