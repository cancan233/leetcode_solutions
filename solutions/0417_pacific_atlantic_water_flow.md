# Pacific Atlantic Water Flow
> medium. link: [click here](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## Problem


## Examples


## Solution
```python
"""
Runtime: 496 ms, faster than 18.97% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.4 MB, less than 78.76% of Python3 online submissions for Pacific Atlantic Water Flow.
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        can_reach_p = [[0 for i in range(n)] for j in range(m)]
        can_reach_a = [[0 for i in range(n)] for j in range(m)]
        results = []
        for i in range(m):
            self.dfs(heights, can_reach_p, i, 0)
            self.dfs(heights, can_reach_a, i, n-1)
        for j in range(n):
            self.dfs(heights, can_reach_p, 0, j)
            self.dfs(heights, can_reach_a, m-1, j)
        for i in range(m):
            for j in range(n):
                if can_reach_p[i][j] and can_reach_a[i][j]:
                    results.append([i, j])
        return results
        
    def dfs(self, heights, can_reach, row, column):
        direction = [-1, 0, 1, 0, -1]
        if can_reach[row][column]:
            return
        can_reach[row][column] = 1
        for i in range(4):
            x = row + direction[i]
            y = column + direction[i+1]
            if x >= 0 and x < len(heights) and y >= 0 and y < len(heights[0]) and heights[x][y] >= heights[row][column]:
                self.dfs(heights, can_reach, x, y)
```