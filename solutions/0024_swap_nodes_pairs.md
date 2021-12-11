# Swap Nodes in Pairs
> Medium

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

## Examples
```
Input: head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
```

## Solution
``` python
"""
Performance: 32 ms faster than 66.33%
             14.3 MB less than %
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        output = head.next
        head.next = self.swapPairs(head.next.next)
        output.next = head
        return output

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode("0")
        dummy.next = head

        if head == None or head.next == None:
            return head

        current = dummy
        while current.next != None and current.next.next != None:
            previous = current
            current = current.next
            after = current.next

            previous.next = after
            current.next = after.next
            after.next = current
        return dummy.next
```