""""

test if a binary tree satisfies the BST property
Complexities:
    Time:
    Space:

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def if_bst(tree):
    def are_keys_in_range(tree, low, high):
        if not tree:
            return True
        elif not low <= tree.val <= high:
            return False
        return are_keys_in_range(tree.left, low, tree.val) and are_keys_in_range(tree.right, tree.val, high)

    return are_keys_in_range(tree, float('-inf'), float('inf'))


if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(1)
    node3 = Node(4)
    node4 = Node(2)
    node5 = Node(5)

    root = node1
    root.left = node2
    root.right = node3
    root.left.right = node4
    root.right.right = node5

    print(if_bst(root))
