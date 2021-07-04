"""

Merge two sorted linked lists


Complexities:
    Time: O(M+N)
    Space: O(1)

"""


class Node:
    def __int__(self, data=None, next_node=None):
        self.val = data
        self.next = next_node


def merge_2_sorted_lists(head1, head2):
    head3 = tail = Node()

    while head1 and head2:
        if head1.val < head2.val:
            tail.next, head1 = head1, head1.next
        else:
            tail.next, head2 = head2, head2.next
        tail = tail.next

        tail.next = head1 or head2
    return head3.next


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
    node8 = Node()
    node8.val = 8
    node9 = Node()
    node9.val = 9
    node10 = Node()
    node10.val = 10

    head1 = node1
    node1.next = node3
    node3.next = node5
    node5.next = node7
    node7.next = None

    head2 = node2
    node2.next = node4
    node4.next = node6
    node6.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = None

    head3 = merge_2_sorted_lists(head1, head2)

    curr = head3
    while curr:
        print(curr.val)
        curr = curr.next
