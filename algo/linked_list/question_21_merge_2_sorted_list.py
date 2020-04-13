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

    # good linked list basic: https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

    # good youtube video for optimized solution:

    # https://www.youtube.com/watch?v=1SDVa-p_CZs

    class Solution:

        def mergeTwoLists(self, l1, l2):

            # solution 1: store into the temporary l3 linked list

            dummy = ListNode(0)

            l3 = dummy  # make dummy points at the l3's head

            while l1 is not None and l2 is not None:

                if l1.val <= l2.val:

                    print(l1.val)

                    l3.next = l1

                    l1 = l1.next

                else:

                    l3.next = l2

                    l2 = l2.next

                l3 = l3.next

            if (l1 is not None):
                l3.next = l1

            if (l2 is not None):
                l3.next = l2

            return dummy.next  # now dummy is "[0,1,1,2,3,4,4]" and if we do dummy.next, it will give dummy
            # the new head "[1,1,2,3,4,4]"

# Slower solution: Recursion solution

# Time complexity : O(n + m)

# Space complexity : O(n + m)

class Solution:
    def mergeTwoLists(self, l1, l2):

        print('this is l1')
        print(l1)

        print('this is l2')
        print(l2)

        if l1 is None:

            return l2

        elif l2 is None:

            return l1

        elif l1.val < l2.val:

            l1.next = self.mergeTwoLists(l1.next, l2)

            print('this is the first conditon')

             print('this is l1')
             print(l1)

             print('this is l2')
             print(l2)

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