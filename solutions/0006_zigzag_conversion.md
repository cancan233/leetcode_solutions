# ZigZag conversion
> medium. link: [click here](https://leetcode.com/problems/zigzag-conversion/)

## Problem
take a string and make the conversion given a number of rows.

## Examples
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R
```

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

```
Input: s = "A", numRows = 1
Output: "A"
```

## Solution
> Runtime: 77 ms, faster than 65.55% of Python3 online submissions for Zigzag Conversion.

> Memory Usage: 14 MB, less than 80.76% of Python3 online submissions for Zigzag Conversion.

``` python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        table = ["" for j in range(numRows)]
        row = 0
        direction = "down"
        for letter in s:
            table[row] += letter

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(table)
```