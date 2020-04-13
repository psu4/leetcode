# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

# Definition for singly-linked list.

# best video for this question

# https://www.youtube.com/watch?v=paScukd62C8&t=371s

# 2 pointer solution

# time complexity: O(n)

# space complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    # if the head is null, return null

    if head is None or head.next is None:

        return None

    # set up 2 pointers at the location 0

    slow = head

    fast = head

    # now move the fast head to the n+1 position
    i = 0

    while i <= n:

        if fast is None:  # if n > len(linklist), return the slow.next (the last element in the link list)

            return slow.next

        fast = fast.next

        i = i + 1

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next  # when fast is null, remove the n element.

    return head
