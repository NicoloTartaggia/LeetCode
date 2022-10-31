# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def getNumber(self, l1: ListNode, multiplier) -> int:
        res = 0
        while l1.next is not None:
            res += l1.val*multiplier
            multiplier *= 10
            l1 = l1.next
        return res + l1.val*multiplier
        
    def getPos(self, tot: int) -> int:
        res = []
        if tot == 0:
            res.append(0)
        else:
            while tot != 0:
                res.append(tot % 10)
                tot = tot // 10
        return res
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tot = self.getNumber(l1, 1) + self.getNumber(l2, 1)
        tot_digits = self.getPos(tot)
        result = ListNode(tot_digits[0])
        current = result
        for i in range(1,len(tot_digits)):
            next_node = ListNode(tot_digits[i])
            current.next = next_node
            current = next_node
        return result