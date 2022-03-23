#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import *


class Solution:
    # def solution(self, nums, target):
    # def solution(self, s, numRows):
    def solution(self, s):
        ls = list(s.strip())
        if len(s) == 0:
            return 0
        ls = list(s.strip())

        sign = -1 if ls[0] == "-" else 1
        if ls[0] in ["-", "+"]:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord("0")
            i += 1
        return max(-(2 ** 31), min(sign * ret, 2 ** 31 - 1))
        pass


if __name__ == "__main__":
    inputs = [
        "42",
        "     -42",
        "4193 with words",
        "words and 987",
        "-+12",
        "+-12",
        "",
        "+1",
        " ",
    ]
    for x in inputs:
        print(Solution().solution(x))
