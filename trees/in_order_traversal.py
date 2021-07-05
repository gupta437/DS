"""

Traverse a binary tree in in-order fashion i.e. L,N,R

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def in_order_traversal_recursive(node, result):
    if node:
        in_order_traversal_recursive(node.left, result)
        result.append(node.val)
        in_order_traversal_recursive(node.right, result)


def in_order_traversal_iterative(root):
    """
       1.1 Create an empty stack
       2.1 Do following while root is not NULL
           a) Push root's right child and then root to stack.
           b) Set root as root's left child.
       2.2 Pop an item from stack and set it as root.
           a) If the popped item has a right child and the right child
               is at top of stack, then remove the right child from stack,
               push the root back and set root as root's right child.
           b) Else print root's data and set root as NULL.
       2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

       :param root:
       :return: list nodes data upon traversal
       """

    curr = root
    result = stack = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

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
    in_order_traversal_recursive(root, res)
    print(res)

    print(in_order_traversal_iterative(root))
