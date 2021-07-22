# Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return the `reversed list`.

## Examples
```
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

## Solution

```python

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        output = head
        if not head or not head.next:
            return head
        head = self.reverseList(head.next)
        output.next.next = output
        output.next = None
        return head
```

``` python
    # iterative solution
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p1 = None
        while head:
            p2 = head.next
            head.next = p1
            p1 = head
            head = p2
        return head
        # another way
        next = None
        while head:
            head.next, head, next = next, head.next, head
        return next  # ***important***
```