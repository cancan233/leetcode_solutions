# Add Two Numbers
> easy. link: [click here](https://leetcode.com/problems/add-two-numbers/)

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Examples
``` 
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

## Solution

Runtime: 68 ms, faster than 77.20% of Python3 online submissions for adding two numbers.

Memory Usage: 14.1 MB, less than 89.84% of Python3 online submissions for adding two numbers.

## Code

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        addone = 0
        head = output = ListNode("0")
        while l1 != None and l2 != None:
            empty = ListNode("#")
            empty.val = (l1.val + l2.val + addone) % 10
            if l1.val + l2.val + addone >= 10:
                addone = 1
            else:
                addone = 0
            l1 = l1.next
            l2 = l2.next
            output.next = empty
            output = output.next

        while l1 != None:
            empty = ListNode("#")
            empty.val = (l1.val + addone) % 10
            if (l1.val + addone) >= 10:
                addone = 1
            else:
                addone = 0
            l1 = l1.next
            output.next = empty
            output = output.next

        while l2 != None:
            empty = ListNode("#")
            empty.val = (l2.val + addone) % 10
            if (l2.val + addone) >= 10:
                addone = 1
            else:
                addone = 0
            l2 = l2.next
            output.next = empty
            output = output.next

        if addone:
            empty = ListNode("#")
            empty.val = 1
            output.next = empty

        return head.next
```