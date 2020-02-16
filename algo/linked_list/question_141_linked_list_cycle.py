# 141. Linked List Cycle


# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# this is the question to find out whether the linked list is a loop or not

# we should use 2 pointers to solve this problem

# https://www.youtube.com/watch?v=MFOAbpfrJ8g

class Solution:
    def hasCycle(self, head:

    ListNode) -> bool:

    if head is None:
        return False

    fast = head.next
    slow = head

    while fast is not None and fast.next is not None and slow is not None:

        if fast == slow:

            return True

        else:
            fast = fast.next.next
            slow = slow.next

    return False