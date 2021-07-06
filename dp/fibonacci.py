"""

Calculate fibonacci

Complexities:
    Time: O(N)
    Space: O(1)

"""


def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1

    for i in range(1, n):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    print(fibonacci(6))
