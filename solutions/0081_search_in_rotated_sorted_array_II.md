# Search in Rotated Sorted Array II
> medium. link: [click here](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## Problem
Given the array `nums` after the rotation and an integer `target`, return `true` if `target` is in `nums`, or `false` if it is not in `nums`.

## Examples
```
[2,5,6,0,0,1,2]
0
[2,5,6,0,0,1,2]
3
[3, 1]
1
```
## Solution
```python
"""
Runtime: 93 ms, faster than 5.32% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 15 MB, less than 64.87% of Python3 online submissions for Search in Rotated Sorted Array II.
"""
def search(self, nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid]:
            left += 1
        elif nums[left] < nums[mid]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return False
```
