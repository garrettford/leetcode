# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from math import ceil
        mapped = []
        n = 0 
        while head:
            mapped.append(head)
            n += 1
            head = head.next
        k = n // 2 if n % 2 else ceil(n/2)
        return mapped[k]