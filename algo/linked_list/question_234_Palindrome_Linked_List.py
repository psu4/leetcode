# 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.


# good link of the solution: https://www.youtube.com/watch?v=wk4QsvwQwdQ

# solution:

# part 1: 2 pointers to split the palindrome

# part 2: 3 pointers to reverse half of the palindrome

# part 3: 2 pointers to check if there is any difference in the 2 parts of the palindrome. if no, return True

# time complexity O(N)

# space complexity O(1)

# good linked list basic: https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

# reverse a link list: good video: solution at 6:00

# youtube: https://www.youtube.com/watch?v=XDO6I8jxHtA

# this question is the extended version of the reversed linklist LeetCode 206

# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

    #         print('this is head')

    #         print(head)

        slow = head

        fast = head

        while slow is not None and fast is not None:

            slow = slow.next

            fast = fast.next.next

        slow = self.reverse(slow)

        fast = head

        while slow is not None:

            if slow.val != fast.val:
                return False

            slow = slow.next
            fast = fast.next

        return True


    def reverse(self, head: ListNode):

        prev = None

        while head is not None:

            temp = head

            head = head.next

            temp.next = prev  # link temp into prev: the first iteration is like None 1 and after linking None <- 1

            prev = temp

            return prev

