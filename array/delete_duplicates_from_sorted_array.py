"""

Delete duplicates from sorted array

Complexities:
    Time: O(N)
    Space: O(1)

"""


def delete_duplicates(sorted_array):
    prev_idx, idx = 0, 1

    while idx < len(sorted_array):
        if sorted_array[prev_idx] != sorted_array[idx]:
            prev_idx += 1
            sorted_array[prev_idx] = sorted_array[idx]
        idx += 1

    return prev_idx+1


if __name__ == "__main__":
    print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 13]))
    print(delete_duplicates([2, 3, 5, 7, 11, 13]))
    print(delete_duplicates([2, 2, 3, 5, 5, 7, 11, 11, 13]))
    print(delete_duplicates([2, 2, 2, 2]))
