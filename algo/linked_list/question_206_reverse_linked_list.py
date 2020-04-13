# 206. Reverse Linked List

# easy and high frequency

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Reverse a singly linked list.

# the best explain video: https://www.youtube.com/watch?v=XDO6I8jxHtA

# the solution is around 6:00

# in this question, we need 3 pointers: prev, temp, head

# prev = previous value

# temp is to hold the temp head value

# head is the head value

# time complexity O(N)

# space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:

    print(head)

    print(head.next)

    prev = None

    while head is not None:
        # while head loop through each node in the linked list
        # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
        # ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
        # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
        # ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
        # ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
        # ListNode{val: 4, next: ListNode{val: 5, next: None}}
        # ListNode{val: 5, next: None}

        print(head)

        temp = head  # Make temp stores the current node. Prev is still None.

        head = head.next  # move the head to the next one

        temp.next = prev  # make the temp link to prev (the first prev=None)

        prev = temp  # move prev forward to temp, which is equal to head

    return prev  # return temp and prev will give the same result. but prev is better in case

    # the link list is empty