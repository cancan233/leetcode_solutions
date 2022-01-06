# Max Area of Island
> medium. link: [click here](https://leetcode.com/problems/max-area-of-island/)

## Problem
You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the `grid` are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in `grid`. If there is no island, return `0`.

## Examples
```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

## Solution
``` python
"""
Runtime: 216 ms, faster than 13.87% of Python3 online submissions for Max Area of Island.
Memory Usage: 16.8 MB, less than 52.48% of Python3 online submissions for Max Area of Island.
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if sum(list(map(sum, grid))) == 0:
            return 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(self.dfs(grid, i, j), max_area)
        return max_area
    
    def dfs(self, grid, r, c):
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area = 1
        direction = [-1, 0, 1, 0, -1]
        for i in range(len(direction)-1):
            x = r + direction[i]
            y = c + direction[i+1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                area += self.dfs(grid, x, y)
        return area
```