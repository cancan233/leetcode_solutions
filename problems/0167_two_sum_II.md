# Two Sum II - Input Array Is Sorted
> easy. link: [click here](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem


## Solution

```python
def twoSum(numbers, target):
    """
    Runtime: 68 ms, faster than 42.47% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    Memory Usage: 14.4 MB, less than 96.55% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    """
    index1, index2 = 0, len(numbers) - 1
    while index1 < index2:
        if numbers[index1] + numbers[index2] == target:
            return (index1 + 1, index2 + 1)
        if numbers[index1] + numbers[index2] < target:
            index1 += 1
        if numbers[index1] + numbers[index2] > target:
            index2 -= 1
    return None
```