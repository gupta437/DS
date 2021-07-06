"""

program that 2 cycle-free singly ll, and determines of there exists a node that is common to bith lists

Complexities:
    Time: O(max(m, n))
    Space: O(1)

"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.val = data
        self.next = next_node


def test_overlapping_with_cycle_lls(list0, list1):
    root0, root1 = has_cycle(list0), has_cycle(list1)

    if not root0 and not root1:
        return test_overlapping_no_cycles_ll(list0, list1)
    elif (not root0 and root1) or (root0 and not root1):
        return None
    else:
        temp = root1
        while temp:
            temp = temp.next
            if temp is root0 or temp is root1:
                break
    return root1 if temp is root0 else None


def test_overlapping_no_cycles_ll(ll1, ll2):
    def length(ll):
        length_ll = 0
        while ll:
            length_ll += 1
            ll = ll.next
        return length_ll

    ll1_len, ll2_len = length(ll1), length(ll2)
    if ll1_len < ll2_len:
        ll1, ll2 = ll2, ll1

    for _ in range(abs(ll1_len - ll2_len)):
        ll1 = ll1.next

    while ll1 and ll2 and ll1 is not ll2:
        ll1, ll2 = ll1.next, ll2.next

    return ll1


def has_cycle(head):
    slow = fast = head

    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
    return None


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    ll1 = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node2

    node8 = Node(8)
    ll2 = node8
    node8.next = node3

    res_node = test_overlapping_with_cycle_lls(ll1, ll2)
    print(res_node.val)
