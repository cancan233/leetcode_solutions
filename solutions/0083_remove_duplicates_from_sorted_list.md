# Remove Duplicates from Sorted List
> Easy

Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list `sorted` as well.

## Examples
```
Input： head = [1, 1, 2, 3, 3]
Output: [1, 2, 3]
```

## Solution
``` python
"""
Performance: 40 ms faster than 81.8%
             14.2 MB less than 80.89%
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        if p1:
            p1 = p1.next
        while p1 != None:
            if p2.val == p1.val:
                p1 = p1.next
                if p1 == None:
                    p2.next = None
            else:
                p2.next = p1
                p2 = p2.next
                p1 = p1.next
        return head
```

``` python
# Online solution. same speed. but more concise
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return
    output = head
    while head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return output
```