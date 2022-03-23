# String to Integer (atoi)
> medium. link: [click here](https://leetcode.com/problems/string-to-integer-atoi/)

## Problem
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. `"123"` -> `123`, `"0032"` -> `32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2<sup>31</sup> should be clamped to -2<sup>31</sup>, and integers greater than 2<sup>31</sup> - 1 should be clamped to 2<sup>31</sup> - 1.
6. Return the integer as the final result.

**Note:**

* Only the space character `' '` is considered a whitespace character.
* Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

## Examples
```
Input: s = "4193 with words"
Output: 4193
```

```
Input: "-+12"
Output: 0
```

```
Input: ""
Output: 0
```

## Solution

[Leetcode Solution](https://leetcode.com/problems/string-to-integer-atoi/solution/)

>Runtime: 56 ms, faster than 38.67% of Python3 online submissions for String to Integer (atoi).

>Memory Usage: 14 MB, less than 39.97% of Python3 online submissions for String to Integer (atoi).

``` python
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        while start < len(s):
            if s[start] != " ":
                break
            start += 1
        if start == len(s):
            return 0

        if s[start] == "-":
            output = s[start]
        elif s[start] == "+":
            output = ""
        elif s[start].isdigit():
            output = s[start]
        else:
            return 0
        start += 1
        while start < len(s):
            if s[start].isdigit():
                output += s[start]
            else:
                break
            start += 1

        if output == "-" or output == "":
            return 0

        output = int(output)
        if output > 2 ** 31 - 1:
            output = 2 ** 31 - 1
        elif output < -(2 ** 31):
            output = -(2 ** 31)

        return output
```