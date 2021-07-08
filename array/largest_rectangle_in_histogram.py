"""

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Complexities:
    Time: O(N)
    Space: O(1)

"""


def largest_rectangle_area(heights):
    stack = [-1]
    idx = 0
    max_area = 0

    while idx < len(heights):
        if stack[-1] == -1 or heights[stack[-1]] <= heights[idx]:
            stack.append(idx)
            idx += 1
        else:
            curr_idx = stack.pop()
            width = idx - stack[-1] - 1
            max_area = max(max_area, width * heights[curr_idx])

    while stack[-1] != -1:
        curr_idx = stack.pop()
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[curr_idx] * width)

    return max_area


if __name__ == "__main__":
    ia = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(ia))
