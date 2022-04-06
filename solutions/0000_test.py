#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *


class Solution:
    def solution(self, nums):
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        output = set()
        for i in range(len(nums)):
            remaining = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < remaining:
                    j += 1
                elif nums[j] + nums[k] > remaining:
                    k -= 1
                else:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return [list(x) for x in output]
        pass


if __name__ == "__main__":
    inputs = [
        [-1, 0, 1, 2, -1, -4],
        [],
        [0],
        [-1, -2, -3, 1, 1, 2, 3, 4, 5],
        [-2, 0, 1, 1, 2],
    ]
    for x in inputs:
        print(Solution().solution(x))
