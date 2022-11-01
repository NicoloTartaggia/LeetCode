# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution computing list's length
        # tmp = head
        # length = 0
        # while tmp:
        #     length += 1
        #     tmp = tmp.next
            
        # mid = length//2    
        # length = 0
        # while length < mid:
        #     length += 1
        #     head = head.next
        
        # return head
    
        # Solution with only one pass
        singleJump = doubleJump = head
        while doubleJump and doubleJump.next:
            singleJump = singleJump.next
            doubleJump = doubleJump.next.next
        return singleJump