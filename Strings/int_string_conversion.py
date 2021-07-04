"""

Define 2 methods to convert int to string and vice-versa

Complexities:
    Time: O(N)
    Space: O(1)

"""


def int_to_string(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    s = []

    while True:
        s.append(chr(ord('0') + num % 10))
        num //= 10
        if num == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


import string


def string_to_int(inp_string):
    is_negative = 1
    if inp_string[0] == '-':
        is_negative = -1

    num = 0
    for i in range(1, len(inp_string)):
        num = num * 10 + string.digits.index(inp_string[i])

    return num * is_negative


if __name__ == "__main__":
    print(int_to_string(-123))
    print(string_to_int("-123"))
