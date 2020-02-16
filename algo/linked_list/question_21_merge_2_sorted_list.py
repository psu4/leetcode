# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://stackabuse.com/python-linked-lists/ listnode link
# https://www.freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d/

# Recursion solution

# Time complexity : O(n + m)

# Space complexity : O(n + m)

class Solution:
    def mergeTwoLists(self, l1, l2):

        #         print('this is l1')
        #         print(l1)

        #         print('this is l2')
        #         print(l2)

        if l1 is None:

            return l2

        elif l2 is None:

            return l1

        elif l1.val < l2.val:

            l1.next = self.mergeTwoLists(l1.next, l2)

            #             print('this is the first conditon')

            #             print('this is l1')
            #             print(l1)

            #             print('this is l2')
            #             print(l2)

            #             print('this is l1.val')
            #             print(l1.val)

            #             print('this is l2.val')
            #             print(l2.val)

            #             print('this is l1.next')
            #             print(l1.next)

            #             print('this is l2.next')
            #             print(l2.next)

            return l1

        else:

            l2.next = self.mergeTwoLists(l2.next, l1)

            #             print('this is the second conditon')

            #             print('this is l1')
            #             print(l1)

            #             print('this is l2')
            #             print(l2)


            #             print('this is l1.val')
            #             print(l1.val)

            #             print('this is l2.val')
            #             print(l2.val)

            #             print('this is l1.next')
            #             print(l1.next)

            #             print('this is l2.next')
            #             print(l2.next)

            return l2