# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # My solution: we use a main ListNode n. Looping through the given list, we make every node
        # pointing to n. If there is a cycle, at a certain point we reach n. Otherwise we reach the
        # last node and we exit the loop.
        n = ListNode(0)
        while head != None:
            tmp = head
            head = head.next
            tmp.next = n
            if head == n:
                return True
        return False