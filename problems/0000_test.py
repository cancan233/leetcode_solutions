#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def climstairs(self, n):
        return n


if __name__ == "__main__":
    test_cases = [17]
    for test_case in test_cases:
        print(Solution().climstairs(test_case))
