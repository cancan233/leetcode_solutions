# Find First and Last Position of Element in Sorted Array
> medium. link: [click here](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

must write an algorithm with `O(log n)` runtime complexity.

## Examples
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]

## Solution
```python
class Solution:    
    """
    Runtime: 79 ms, faster than 90.88% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 15.6 MB, less than 12.39% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    """
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

```