# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Getting length of both lists
        tmpA, tmpB = headA, headB
        lenA, lenB = 0, 0
        while tmpA != None:
            lenA += 1
            tmpA = tmpA.next
        while tmpB != None:
            lenB += 1
            tmpB = tmpB.next
            
        # First we "consume" the extra nodes of the longer list. Then, we try to find the intersection
        tmpA, tmpB = headA, headB 
        while tmpA != None and tmpB != None:
            if lenA > lenB:
                tmpA = tmpA.next
                lenA -= 1
            elif lenB > lenA:
                tmpB = tmpB.next
                lenB -= 1
            else:
                if tmpA == tmpB:
                    return tmpA
                else:
                    tmpA = tmpA.next
                    tmpB = tmpB.next
        return None