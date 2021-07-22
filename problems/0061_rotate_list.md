# Rotate List
> Medium

Given the `head` of a linked list, rotate the list to the right by `k` places.

## Examples
```
Input: [1,2,3] and k=200000
```

## Solution
Minimize the loop by dividing k with nums length. Double pointers to rotate the list.

``` python
"""
Performance: 52 ms faster than 17.18%
             14.5 MB less than %
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        # check list length
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1

        k = k % count

        if not k:
            return head

        # This part can be revised
        for i in range(k):
            p = head
            while p.next.next:
                p = p.next
            p.next.next = head
            head = p.next
            p.next = None
        return head

        # Or you can use two points
        dummy = ListNode("#")
        dummy.next = head

        for i in range(k):
            p1 = p2 = dummy
            while p2.next != None:
                previous = p2
                p2 = p2.next
            p2.next = p1.next
            p1.next = p2
            previous.next = None
        return dummy.next

        # optional answer, which is similar to #19
        p1 = p2 = head
        for i in range(k):
            p1 = p1.next

        while p1.next:
            p2 = p2.next
            p1 = p1.next

        p1.next = head
        head = p2.next
        p2.next = None
        return head
```