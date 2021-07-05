"""

Traverse a binary tree in pre-order fashion i.e. N,L,R

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def pre_order_traversal_recursive(node, result):
    if node:
        result.append(node.val)
        pre_order_traversal_recursive(node.left, result)
        pre_order_traversal_recursive(node.right, result)


def pre_order_traversal_iterative(node):
    result = []
    curr = node
    stack = []
    while curr or stack:
        if curr:
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()

    return result


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

    res = []
    pre_order_traversal_recursive(root, res)
    print(res)

    print(pre_order_traversal_iterative(root))

