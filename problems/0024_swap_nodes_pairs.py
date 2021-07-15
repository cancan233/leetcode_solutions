#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        output = head.next
        head.next = self.swapPairs(head.next.next)
        output.next = head
        return output

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode("0")
        dummy.next = head

        if head == None or head.next == None:
            return head

        current = dummy
        while current.next != None and current.next.next != None:
            previous = current
            current = current.next
            after = current.next

            previous.next = after
            current.next = after.next
            after.next = current
        return dummy.next
