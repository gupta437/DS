"""

Traverse a binary tree in level-order fashion

"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
        

def level_order_traversal(root):
    """
    1 Visit the root
    2 While traversing level l, keep all the elements at level l+1 in queue.
    3 Go to the next level and visit all the nodes at that level.
    4 Repeat this until all levels are completed.

    :param root:
    :return: list nodes data upon traversal
    """
    result = []

    if root:
        visited = [root]
        while visited:
            node = visited.pop(0)
            result.append(node.get_data())
            if node.has_left():
                visited.append(node.get_left())
            if node.has_right():
                visited.append(node.get_right())

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

    print(level_order_traversal(root))

