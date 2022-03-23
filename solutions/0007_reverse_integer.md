# Reverse Integer
> medium. link: [click here](https://leetcode.com/problems/reverse-integer/)

## Problem
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [-2<sup>31</sup>, 2<sup>31</sup>-1], then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

## Examples
```
Input: x = 123
Output: 321
```
```
Input: x = -123
Output: -321
```
```
Input: x = 120
Output: 21
```
## Solution

>Runtime: 32 ms, faster than 91.85% of Python3 online submissions for Reverse Integer.

>Memory Usage: 13.8 MB, less than 71.36% of Python3 online submissions for Reverse Integer.

``` python
class Solution:
    def reverse(self, x: int) -> int:
        output = ""
        x = str(x)
        if x[0] == "-":
            output += "-"
            x = x[1:]
        output += x[-1]
        for i in range(len(x) - 2, -1, -1):
            # 2^31 - 1 = 2147483647
            # 2^31 = 2147483648
            if int(output) < -214748364 or int(output) > 214748364:
                return 0
            elif int(output) == -214748364 and int(x[i]) > 8:
                return 0
            elif int(output) == 214748364 and int(x[i]) > 7:
                return 0
            else:
                output += x[i]
        return int(output)
```