"""

Program takes an array of non negative integers as input and return result after plus 1.

Complexities:
    Time: O(N)
    Space: O(1)

"""


def plus_one(digits):
    digits[-1] += 1
    for idx in reversed(range(1, len(digits))):
        if digits[idx] != 10:
            break
        digits[idx] = 0
        digits[idx - 1] += 1

    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)

    return digits


if __name__ == "__main__":
    print(plus_one([9, 9]))
    print(plus_one([1, 2, 3]))
    print(plus_one([1, 9]))




