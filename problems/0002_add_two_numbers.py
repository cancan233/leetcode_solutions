#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        addone = 0
        head = output = ListNode("0")
        while l1 != None and l2 != None:
            empty = ListNode("#")
            empty.val = (l1.val + l2.val + addone) % 10
            if l1.val + l2.val + addone >= 10:
                addone = 1
            else:
                addone = 0
            l1 = l1.next
            l2 = l2.next
            output.next = empty
            output = output.next

        while l1 != None:
            empty = ListNode("#")
            empty.val = (l1.val + addone) % 10
            if (l1.val + addone) >= 10:
                addone = 1
            else:
                addone = 0
            l1 = l1.next
            output.next = empty
            output = output.next

        while l2 != None:
            empty = ListNode("#")
            empty.val = (l2.val + addone) % 10
            if (l2.val + addone) >= 10:
                addone = 1
            else:
                addone = 0
            l2 = l2.next
            output.next = empty
            output = output.next

        if addone:
            empty = ListNode("#")
            empty.val = 1
            output.next = empty

        return head.next
