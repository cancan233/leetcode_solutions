#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import *


class Solution:
    # def solution(self, nums, target):
    # def solution(self, s, numRows):
    def solution(self, height):
        left, right = 0, len(height) - 1
        max_container = 0
        while left < right:
            max_container = max(
                max_container, min(height[left], height[right]) * (right - left)
            )
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_container

        pass


if __name__ == "__main__":
    inputs = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [1, 10, 1, 10]]
    for x in inputs:
        print(Solution().solution(x))
