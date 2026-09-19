# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = curr = ListNode()

        while list1 and list2:
            if first is None:
                if list1.val <= list2.val:
                    first = list1
                    curr = first
                    list1 = list1.next
                else:
                    first = list2
                    curr = first
                    list2 = list2.next

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        if list1:
            curr.next = list1 
        elif list2: 
            curr.next = list2

        return first.next

                
        