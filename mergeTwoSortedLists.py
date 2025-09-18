# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Merging two sorted linked lists to return a big SORTED linked list
        tempList = ListNode()
        currPoint = tempList

        while list2 and list1:
            if list1.val < list2.val:
                # not .val as that would just define currPoint as an int rather than object pointer
                currPoint.next = list1
                list1 = list1.next
            else:
                currPoint.next = list2
                list2 = list2.next

            currPoint = currPoint.next

        if list1:
            currPoint.next = list1

        else:
            currPoint.next = list2

        return tempList.next
# adding to list but alrready initiallised with 0 hence why .next needed
