# Longest Palindromic Substring (回文子串)
> medium. link: [click here](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem
Given a string `s`, return the longest palindromic substring in `s`.

## Examples
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is alsos a valid answer
```

```
Input: s = "cbbd"
Output: "bb"
```

## Solution

中心扩展法。以每个字符为中心，向两边扩展。时间复杂度O(nlogn)。

> Runtime: 924 ms, faster than 81.64% of Python3 online submissions for Longest Palindromic Substring.
> Memory Usage: 14 MB, less than 41.07% of Python3 online submissions for Longest Palindromic Substring.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""

        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        for i in range(len(s)):
            output = max(palindrome(s, i, i), palindrome(s, i, i + 1), output, key=len)

        return output
```