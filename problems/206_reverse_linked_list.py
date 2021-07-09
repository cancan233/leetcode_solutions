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
