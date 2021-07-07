"""

check if binary tree is symmetric.

Complexity:
    Time:
    Space:

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def is_symmetric(tree):
    def check_symmetric(left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        elif left_tree and right_tree:
            return (left_tree.val == right_tree.val
                    and check_symmetric(left_tree.left, right_tree.right)
                    and check_symmetric(left_tree.right, right_tree.left))
        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node6 = Node(3)
    node7 = Node(2)
    node8 = Node(1)

    node4.left = node3
    node4.right = node6

    node3.right = node2
    node3.left = None

    node2.right = node1
    node2.left = None

    node1.left = node1.right = None

    node6.left = node7
    node6.right = None

    node7.left = node8
    node7.right = None

    node7.left = node7.right = None

    print(is_symmetric(node4))

