# Increasing Triplet Subsequence
> Medium. 

Given an integer array `nums`, return `true` *if there exists a triple of indices* `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

## Examples
```
Input: nums = [2, 1, 5, 0, 4, 6]
Output: True
```

## Solution

Find the smallest one, and the one that is greater than this one. If these two does not in the end of the list, then there is always a increasing triplet. But this method would not tell you how many pairs are there or the first encoutering triplet.

```python
"""
Performance: 556 ms faster than 92.38%
             24.6 MB less than 97.05%
"""
def increasingTriplet(nums):
    first = second = float("inf")
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
```