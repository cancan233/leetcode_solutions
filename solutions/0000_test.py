#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import *


class Solution:
    # def solution(self, nums, target):
    # def solution(self, s, numRows):
    def solution(self, x):
        output = ""
        x = str(x)
        if x[0] == "-":
            output += "-"
            x = x[1:]
        output += x[-1]
        for i in range(len(x) - 2, -1, -1):
            # 2^31 - 1 = 2147483647
            # 2^31 = 2147483648
            if int(output) < -214748364 or int(output) > 214748364:
                return 0
            elif int(output) == -214748364 and int(x[i]) > 8:
                return 0
            elif int(output) == 214748364 and int(x[i]) > 7:
                return 0
            else:
                output += x[i]
        return int(output)

        pass


if __name__ == "__main__":
    inputs = [123, -123, 120, 1000000, 1563847412]
    for x in inputs:
        print(Solution().solution(x))
