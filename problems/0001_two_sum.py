#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    # Solution 1

    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            d[num] = i

    # Solution 2

    def twoSum(nums, target):
        array = list(zip(nums, range(len(nums))))
        array.sort()
        i, j = 0, len(nums) - 1
        while i <= j:
            if array[i][0] + array[j][0] == target:
                return [array[i][1], array[j][1]]
            elif array[i][0] + array[j][0] > target:
                j -= 1
            elif array[i][0] + array[j][0] < target:
                i += 1

