"""

write a program that takes an array A and an index i into A, and rearranges the elements such that all elements
less than A[i](the pivot) appear first, followed by elements equal to the pivot, followed by elements greater
than the pivot.

"""

"""

Complexities:
    Time: O(N)
    Space: O(1)

"""


def sort_around_pivot_2_pass(pivot_index, input_array):
    smaller = 0
    pivot = input_array[pivot_index]
    for i in range(len(input_array)):
        if input_array[i] < pivot:
            input_array[smaller], input_array[i] = input_array[i], input_array[smaller]
            smaller += 1

    larger = len(input_array) - 1
    for i in range(len(input_array) - 1, -1, -1):
        if input_array[i] > pivot:
            input_array[larger], input_array[i] = input_array[i], input_array[larger]
            larger -= 1

    return input_array


"""

Complexities:
    Time: O(N)
    Space: O(1)

"""


def sort_flag_single_pass(pivot_idx, nums):
    smaller, equal, larger = 0, 0, len(nums) - 1
    pivot = nums[pivot_idx]

    while equal < larger:
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            equal += 1
            smaller += 1
        elif nums[equal] > pivot:
            nums[equal], nums[larger] = nums[larger], nums[equal]
            larger -= 1
        else:
            equal += 1
    return nums


if __name__ == "__main__":

    ia = [0, 1, 1, 0, 2, 1, 2]
    print(sort_around_pivot_2_pass(1, ia))

    ib = [0, 1, 1, 0, 2, 1, 2]
    print(sort_flag_single_pass(1, ib))

