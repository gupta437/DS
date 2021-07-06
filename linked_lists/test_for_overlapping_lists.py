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


def test_overlapping_no_cycle_lls(list0, list1):
    def length(l):
        length_l = 0
        while l:
            length_l += 1
            l = l.next
        return length_l

    list0_len = length(list0)
    list1_len = length(list1)

    if list0_len < list1_len:
        list0, list1 = list1, list0

    start = abs(list0_len - list1_len)

    for _ in range(start):
        list0 = list0.next

    while list0 and list1 and list0 is not list1:
        list0 = list0.next
        list1 = list1.next

    return list0


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
    node7.next = None

    node8 = Node(8)
    ll2 = node8
    node8.next = node3

    res_node = test_overlapping_no_cycle_lls(ll1, ll2)
    print(res_node.val)
