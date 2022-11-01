# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        newHead = tmp
        while tmp != None:
            if tmp == head:
                tmp = tmp.next
                newHead.next = None
            else:
                curr = tmp
                tmp = tmp.next
                curr.next = newHead
                newHead = curr
        return newHead