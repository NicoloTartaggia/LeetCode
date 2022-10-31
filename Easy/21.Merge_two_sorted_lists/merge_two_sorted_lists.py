# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        mergedList = ListNode()
        iterator = mergedList
        # Starting node of the mergedList
        if list1.val <= list2.val:
            iterator.val = list1.val
            list1 = list1.next
        else:
            iterator.val = list2.val
            list2 = list2.next
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                iterator.next = ListNode(list1.val)
                list1 = list1.next
            else:
                iterator.next = ListNode(list2.val)
                list2 = list2.next
            iterator = iterator.next
        if list1 != None:
            iterator.next = list1
        elif list2 != None:
            iterator.next = list2
            
        return mergedList