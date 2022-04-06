# Longest Common Prefix
> easy. link: [click here](https://leetcode.com/problems/longest-common-prefix/)

## Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Examples
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
## Solution

> Runtime: 45 ms, faster than 62.15% of Python3 online submissions for Longest Common Prefix.

> Memory Usage: 14 MB, less than 13.49% of Python3 online submissions for Longest Common Prefix.

``` python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    if i > 0:
                        return strs[0][:i]
                    else:
                        return ""
        return strs[0]
```

> Runtime: 37 ms, faster than 80.45% of Python3 online submissions for Longest Common Prefix.

> Memory Usage: 13.8 MB, less than 90.80% of Python3 online submissions for Longest Common Prefix.

``` python
class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
```
