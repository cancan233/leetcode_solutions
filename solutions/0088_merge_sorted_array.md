# Merge Sorted Array
> easy. link: [click here](https://leetcode.com/problems/merge-sorted-array/)

## Problem


## Solution

```python
def solution(self, nums1, m, nums2, n):
    """
    Runtime: 40 ms, faster than 44.62% of Python3 online submissions for Merge Sorted Array.
    Memory Usage: 13.9 MB, less than 99.78% of Python3 online submissions for Merge Sorted Array.
    """
    m, n = m - 1, n - 1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[m + n + 1] = nums1[m]
            m -= 1
        else:
            nums1[m + n + 1] = nums2[n]
            n -= 1
        print(m, n)

    if n >= 0:
        nums1[: n + 1] = nums2[: n + 1]
```