# Two Sum
> easy. link: [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples
``` 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```
Input: nums = [3,3], target = 6
Output: [0,1]
```
## Solution
Solution 1: use dictionary for search (hash in python)

Solution 2: use two pointers on the sorted arrays

## Code
```python
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
```
