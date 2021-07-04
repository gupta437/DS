"""

Reverse singly linked list

Complexities:
    Time: O(N)
    space: O(1)

"""


class Node:
    def __int__(self, data=None, next=None):
        self.val = data
        self.next = next


def reverse_singly_ll(head):
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


if __name__ == "__main__":
    node1 = Node()
    node1.val = 1
    node2 = Node()
    node2.val = 2
    node3 = Node()
    node3.val = 3
    node4 = Node()
    node4.val = 4
    node5 = Node()
    node5.val = 5
    node6 = Node()
    node6.val = 6
    node7 = Node()
    node7.val = 7

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None

    head2 = reverse_singly_ll(head)

    curr = head2
    while curr:
        print(curr.val)
        curr = curr.next

