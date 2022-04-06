# 3Sum With Multiplicity
> medium. link: [click here](https://leetcode.com/problems/3sum-with-multiplicity/)

## Problem
Given an integer array `arr`, and an integer `target`, return the number of tuples `i`, `j`, `k` such that `i < j < k` and `arr[i] + arr[j] + arr[k] == target`.

As the answer can be very large, return it **modulo** 10<sup>9</sup> + 7

## Examples
```
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
```

```
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
```

## Solution
>Runtime: 7858 ms, faster than 5.81% of Python3 online submissions for 3Sum With Multiplicity.

>Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for 3Sum With Multiplicity.
``` python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        for i in range(len(arr)):
            count += self.helper(arr, i, target - arr[i])
        return count % (10 ** 9 + 7)

    def helper(self, arr, i, target):
        count = 0
        freq = {}
        for num in arr[i + 1 :]:
            remaining = target - num
            if remaining in freq:
                count += freq[remaining]
            freq[num] = freq.get(num, 0) + 1
        return count
```

> Runtime: 84 ms, faster than 88.95% of Python3 online submissions for 3Sum With Multiplicity.

> Memory Usage: 14.2 MB, less than 22.67% of Python3 online submissions for 3Sum With Multiplicity.

``` python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        cnt = Counter(arr)  # obtain the number of instances of each number
        res, i, l = 0, 0, len(arr)
        while i < l:  # in replacement of the for-loop, so that we can increment i by more than 1
            j, k = i, l-1  # j should be the leftmost index, hence j=i instead of j=i+1
            while j < k:  # i <= j < k; arr[i] <= arr[j] <= arr[k]
                if arr[i]+arr[j]+arr[k] < target:
                    j += cnt[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= cnt[arr[k]]
                else:  # arr[i]+arr[j]+arr[k] == target
                    if arr[i] != arr[j] != arr[k]:  # Case 1: All the numbers are different
                        res += cnt[arr[i]]*cnt[arr[j]]*cnt[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:  # Case 2: The smaller two numbers are the same
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*cnt[arr[k]]//2  # math.comb(cnt[arr[i]], 2)*cnt[arr[k]]
                    elif arr[i] != arr[j] == arr[k]:  # Case 3: The larger two numbers are the same
                        res += cnt[arr[i]]*cnt[arr[j]]*(cnt[arr[j]]-1)//2  # math.comb(cnt[arr[j]], 2)*cnt[arr[i]]
                    else:  # Case 4: All the numbers are the same
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*(cnt[arr[i]]-2)//6  # math.comb(cnt[arr[i]], 3)
					# Shift pointers by the number of instances of the number
                    j += cnt[arr[j]]
                    k -= cnt[arr[k]]
            i += cnt[arr[i]]  # Shift pointer by the number of instances of the number
        return res%1000000007
```