'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a 
linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        # number of steps taken
        itr = 0
        while l1:
            # multiply the node value by 10^number of steps
            a += l1.val * (10 ** itr)
            l1 = l1.next
            itr += 1
        # reset steps
        itr = 0
        b = 0
        while l2:
            b += l2.val * (10 ** itr)
            l2 = l2.next
            itr += 1
        # use list to split the sum into separate digits
        sumList = list(str(a + b))
        result = None
        # go through the sumList and create a Node for each digit
        # and connect it to the previous digit
        for d in sumList:
            temp = ListNode(int(d))
            temp.next = result
            result = temp
        return result