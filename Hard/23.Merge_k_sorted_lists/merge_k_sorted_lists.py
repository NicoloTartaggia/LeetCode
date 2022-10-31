from typing import List, Optional
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next
    
    def print_listnode(self):
        while self:
            print(self.val, "->", end = '')
            self = self.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        heap = []
        res = ListNode(-1)
        builder = res
        for index, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, index, node))
                
        while heap:
            val, index, node = heappop(heap)
            builder.next = node
            builder = builder.next
            if node.next:
                lists[index] = lists[index].next
                heappush(heap, (lists[index].val, index, lists[index]))
        return res.next


if __name__ == "__main__":
    n3 = ListNode(5, None)
    n2 = ListNode(4, n3)
    n1 = ListNode(1, n2)

    n6 = ListNode(4, None)
    n5 = ListNode(3, n6)
    n4 = ListNode(1, n5)
    
    n8 = ListNode(6, None)
    n7 = ListNode(2, n8)

    l1 = [n1, n4, n7]

    s = Solution().mergeKLists(l1)
    s.print_listnode()