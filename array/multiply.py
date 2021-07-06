"""

Program takes two arrays representing int and returns an int representing their product.

Complexities:
    Time:
    Space:

"""


def multiply(array1, array2):
    sign = 1 if (array1[0] < 0 and array2[0] < 0) or (array1[0] >=0 or array2[0] >= 0) else -1

    array1[0], array2[0] = abs(array1[0]), abs(array2[0])

    result = [0] * (len(array1) + len(array2))

    for i in reversed(range(len(array1))):
        for j in reversed(range(len(array2))):
            result[i+j+1] += array1[i] * array2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] = result[i+j+1] % 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]

    result[0] = result[0] * sign
    return result


if __name__ == "__main__":
    print(multiply([1], [9]))
