"""

check if binary tree is balanced.

Complexity:
    Time: O(N)
    Space: O(1)

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def is_balanced(tree):
    def check_balanced(node):
        if not node:
            return True, -1

        balanced, l_height = check_balanced(node.left)
        if not balanced:
            return False, -1

        balanced, r_height = check_balanced(node.right)
        if not balanced:
            return -1

        height = max(l_height, r_height) + 1
        balanced = abs(l_height - r_height) <= 1

        return balanced, height

    balanced, height = check_balanced(tree)
    return balanced


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)

    node8.left = node4
    node8.right = node10
    node4.left = node2
    node4.right = node5
    node5.left = None
    node5.right = None

    node2.left = node1
    node2.right = node3
    node1.left = None
    node2.right = None
    node3.left = None
    node3.right = None

    node10.left = node9
    node10.right = node11
    node9.left = None
    node9.right = None
    node11.left = None
    node11.right = None

    print(is_balanced(node8))

