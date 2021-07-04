"""

Check if the string is plaindrome.

Complexities:
    Time: O(N)
    Space: O(1)

"""


def is_palindrome(inp_array):
    return all(inp_array[i] == inp_array[~i] for i in range(len(inp_array) // 2))


if __name__ == "__main__":
    print(is_palindrome('abab'))
    print(is_palindrome('baab'))
