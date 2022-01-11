# Sum of Root To Leaf Binary Numbers
> easy. link: [click here](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)

## Problem


## Examples


## Solution
```python
"""
Runtime: 63 ms, faster than 13.07% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 14.6 MB, less than 68.32% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
"""
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path = (path << 1) + node.val
            if not node.right and not node.left:
                return path
            return dfs(node.right, path) + dfs(node.left, path)
        return dfs(root, 0)
            
```