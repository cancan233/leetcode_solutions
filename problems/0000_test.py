#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(nums):
    output = set()
    nums.sort()
    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        storage = {}
        for j in range(i + 1, len(nums)):
            if nums[j] in storage:
                output.add((nums[i], storage[nums[j]], nums[j]))
            storage[target - nums[j]] = nums[j]
    return output


if __name__ == "__main__":
    input = [-2, 0, 1, 1, 2]
    # input = [0, 0, 0, 0]
    input = [-1, 0, 1, 2, -1, -4]
    print(solution(input))
