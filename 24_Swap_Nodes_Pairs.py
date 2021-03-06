#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cancan Huang @ 2019-07-21

# I saw this solution online. I cannot imagine such a brief solution.

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
