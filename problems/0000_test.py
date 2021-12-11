#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import *


class Solution:
    def minWindow(self, s, t):
        minwindow = ""
        count = t.counter()
        p1, p2 = 0, 0
        for p2 in range(len(s)):
            if count[s[p2]] >= 0:
                pass 
            while cnt == len(t):
                if (r - l + 1 < min_size):
                    min_l = 
                if 
            minwindow = s[p1:p2]
        return minwindow


if __name__ == "__main__":
    # 0076
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
