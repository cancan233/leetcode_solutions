#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        # check list length
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1

        k = k % count

        if not k:
            return head

        # This part can be revised
        for i in range(k):
            p = head
            while p.next.next:
                p = p.next
            p.next.next = head
            head = p.next
            p.next = None
        return head

        # optional answer, which is similar to #19
        # p1 = p2 = head
        # for i in range(k):
        #     p1 = p1.next

        # while p1.next:
        #     p2 = p2.next
        #     p1 = p1.next

        # p1.next = head
        # head = p2.next
        # p2.next = None
        # return head
