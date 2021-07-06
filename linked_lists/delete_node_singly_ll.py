"""

Delete given node from singly linked list. Input node is guaranteed not to be the tail node.

"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.val = data
        self.next = next_node


"""

Complexities:
    Time: O(n)
    Space: O(1)
    
"""


def delete_given_node(head, node):
    if head is node:
        head = head.next
    else:
        curr = head
        while curr.next:
            if curr.next is node:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                break
            curr = curr.next

    return head


"""

Complexities:
    Time: O(1)
    Space: O(1)
    
"""


def delete_given_node(head, node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    ll1 = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    delete_given_node(ll1, node3)
    curr = ll1
    while curr:
        print(curr.val)
        curr = curr.next
