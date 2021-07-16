#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        output = head
        if not head or not head.next:
            return head
        head = self.reverseList(head.next)
        output.next.next = output
        output.next = None
        return head

    # iterative solution
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p1 = None
        while head:
            p2 = head.next
            head.next = p1
            p1 = head
            head = p2
        return head
        # another way
        next = None
        while head:
            head.next, head, next = next, head.next, head
        return next  # ***important***
