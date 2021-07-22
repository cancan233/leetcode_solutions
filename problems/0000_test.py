#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(nums):
    first = second = float("inf")
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
        print(first, second)
    return False


if __name__ == "__main__":
    input = [2, 1, 5, 0, 4, 6]
    print(solution(input))
    # print(random.randint(0, 500))
