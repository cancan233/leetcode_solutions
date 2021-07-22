# Longest Substring without Repeating Characters
> medium. link: [click here](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem

Given a string s, find the length of the longest substring without repeating characters.

## Examples

```
Input: s = " "
Ouput: 1
```

```
Input: s = "pwwkew"
Output: 3
```

## Solutions
Use dictionary to store the visited characters. Use slide window to calculate the length of the substrings and only return the largest number. Once the character is repeated, decrease left hand until the repeated character is out of the window, otherwise, increase right hand.

## Code

``` python
"""
Performance: 776 ms faster than 8.55%
             19.1 MB less than 24.24%
"""
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        output = ""
        p1 = p2 = 0
        d = {}
        outputs = []
        while p2 < len(s):
            if s[p2] not in d:
                output += s[p2]
                d[s[p2]] = p2
            else:
                outputs.append(output)
                output = ""
                p1 = d[s[p2]]
                p2 = p1
                d = {}
            p2 += 1
        outputs.append(output)
        return len(max(outputs, key=len))
```

``` python
"""
Performance: 52 ms faster than 92.23%
             14.4 MB less than 24.24%
"""
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            # usedChar stores the largest index of visitied characters so far
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
```