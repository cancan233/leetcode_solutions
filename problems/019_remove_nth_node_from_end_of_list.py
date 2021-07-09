#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fake = ListNode('#')
        fake.next = head
        p1 = p2 = fake
        for i in range(n):
            p1 = p1.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return fake.next
