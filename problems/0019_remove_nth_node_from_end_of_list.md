# Remove Nth Node From End of List
> Medium

Given the `head` of a linked list, remove the n<sup>th</sup> node from the end of the list and return its head.

## Examples
```
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

## Solution
Double pointers. The first pointer is ahead of the second one by n steps.

```python
"""
Performance: 36 ms faster than 51.76%
             14 MB less than 98.59%
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fake = ListNode('#')
        fake.next = head
        p1 = p2 = fake
        for i in range(n):
            p1 = p1.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return fake.next
```