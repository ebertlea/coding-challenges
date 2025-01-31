# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedListHead = ListNode(0)
        current = mergedListHead

        while list1 and list2:
            if list1.val<list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2

        return mergedListHead.next
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #print("list 1: ", list1)
        #print("list 2: ", list2)
        #print("\n")
        if not list1:
            #print("finished list 2: ", list2)
            return list2
        if not list2:
            #print("finished list 1: ", list1)
            return list1
        
        if (list1.val < list2.val):
            #print('hey 1')
            list1.next = self.mergeTwoLists(list1.next, list2)
            #print("finished list 1: ", list1)
            return list1
        else:
            #print('hey 2')
            list2.next = self.mergeTwoLists(list1, list2.next)
            #print("finished list 2: ", list2)
            return list2
