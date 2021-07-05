"""

search element in bst

Complexities:
    Time: O(h) h is the height of the tree
    Space: O(1)

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def search_bst(tree, key):
    return (tree if not tree or tree.data == key else search_bst(tree.left, key)
            if key < tree.data else search_bst(tree.right, key))


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

    print(search_bst(root, 2))
