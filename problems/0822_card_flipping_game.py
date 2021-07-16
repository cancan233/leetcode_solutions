#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Thoughts:

If fronts[i] == backs[i], the number cannot be good number if flipped or not. For other numbers, we only need to find the smallest value because we only need to flip that card to make the number as a good number
"""


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_card = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same_card.add(fronts[i])
        output = min([x for x in fronts + backs if x not in same_card], default=0)
        return output
