#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import *


class Solution:
    def solution(self, nums, target):
        left = self.lower_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left > right:
            return [-1, -1]
        return [left, right]

    def lower_bound(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return l

    def higher_bound(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            print(l, r)
        return r


if __name__ == "__main__":
    # nums = [5, 7, 7, 8, 8, 10]
    nums = []
    target = 5
    print(Solution().solution(nums, target))
