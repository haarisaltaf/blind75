# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # cache - set each individual list to have it so that we can easily compare without
        # merge each k > 1 sorted list with first sorted list.

        def mergeTwoLists(list1, list2):
            tempList = ListNode()
            currHead = tempList

            while list1 and list2:
                if list1.val < list2.val:
                    currHead.next = list1
                    list1 = list1.next
                    # added at list1 pointer, next needs to be checked next

                else:
                    currHead.next = list2
                    list2 = list2.next

                currHead = currHead.next

            if list1:
                currHead.next = list1

            if list2:
                currHead.next = list2

            return tempList.next

        # base case
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        # recursive case
        middle = len(lists) // 2

        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])

        # return
        return mergeTwoLists(left, right)
