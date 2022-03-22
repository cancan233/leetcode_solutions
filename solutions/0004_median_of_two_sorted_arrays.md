# Median of Two Sorted Arrays
> Hard

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

## Examples

```bash
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
```

```bash
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
```

```bash
Input: nums1 = [0, 0], nums2 = [0, 0]
Output: 0.0
```

```bash
Input: nums1 = [2], nums2 = []
Output: 2.0
```

## Solution

The idea is to seperate `nums1` and `nums2` as X1, X2 and Y1, Y2 partitions. The median will be calculated by the boundary values.

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = 0, len(nums1)
        m, n = len(nums1), len(nums2)
        
        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            if partitionX == 0:
                X1 = float("-inf")
            else:
                X1 = nums1[partitionX - 1]
            
            if partitionX == m:
                X2 = float("inf")
            else:
                X2 = nums1[partitionX]
            
            if partitionY == 0:
                Y1 = float("-inf")
            else:
                Y1 = nums2[partitionY - 1]
            
            if partitionY == n:
                Y2 = float("inf")
            else:
                Y2 = nums2[partitionY]
                
            if (X1 <= Y2) and (Y1 <= X2):
                if (m + n) % 2 == 0:
                    median = (max(X1, Y1) + min(X2, Y2)) / 2
                    return median
                else:
                    median = max(X1, Y1)
                    return median
            elif (Y1 > X2):
                start = partitionX + 1
            else:
                end = partitionX - 1
```