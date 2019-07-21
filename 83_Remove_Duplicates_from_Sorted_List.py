# -*- coding: utf-8 -*-
# @Author: cancan233
# @Date:   2019-07-20 22:55:18
# @Last Modified by:   cancan233
# @Last Modified time: 2019-07-20 23:13:43

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        if p1:
            p1 = p1.next
        while p1 != None:
            if p2.val == p1.val:
                p1 = p1.next
                if p1 == None:
                    p2.next = None
            else:
                p2.next = p1
                p2 = p2.next
                p1 = p1.next
        return head

# Online solution. same speed. but more concise
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return
    output = head
    while head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return output
