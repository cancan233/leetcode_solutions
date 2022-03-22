#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import *


class Solution:
    # def solution(self, nums, target):
    def solution(self, s, numRows):
        if numRows == 1 or numRows > len(s):
            return s

        table = ["" for j in range(numRows)]
        row = 0
        direction = "down"
        for letter in s:
            table[row] += letter

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(table)

        pass


if __name__ == "__main__":
    # nums = [5, 7, 7, 8, 8, 10]
    nums = []
    target = 5
    # print(Solution().solution(nums, target))

    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().solution(s, numRows))
