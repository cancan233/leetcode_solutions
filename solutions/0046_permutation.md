# Permutation
> easy. link: [click here](https://leetcode.com/problems/permutations/)

## Problem


## Examples


## Solution
```python
"""
Runtime: 62 ms, faster than 19.80% of Python3 online submissions for Permutations.
Memory Usage: 14.5 MB, less than 44.29% of Python3 online submissions for Permutations.
"""
class Solution:
    def permute(self, nums):
        output = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            output.extend(perms)
            nums.append(n)

        return output
```