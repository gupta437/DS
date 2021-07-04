"""

Check if given singly ll has cycle, if yes then return start of the cycle

Complexities:
    Time: O()
    Space:

"""


class Node:
    def __int__(self, data=None, next=None):
        self.val = data
        self.next = next


def has_cycle(head):
    slow = fast = head

    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
    return None


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

    head1 = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2

    res_head = has_cycle(head1)
    if res_head:
        print(res_head.val)
    else:
        print("No cycle detected")

    head2 = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    res_head2 = has_cycle(head2)
    if res_head2:
        print(res_head2.val)
    else:
        print("No cycle detected")
