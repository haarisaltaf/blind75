# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # two point, slow and fast, if the next head is the one
        # to be removed, have slow point to fast.next
        count, countHead = 0, head

        while countHead:
            count += 1
            countHead = countHead.next

        if (count == 1 and n) or (count == n):
            # when count == n: range would return an empty iterable (returns an iterable of size 0)
            # and therefore never run hence the edge case above
            return head.next

        currHead = head
        for i in range(count-n-1):
            currHead = currHead.next

        print(currHead.val)
        currHead.next = currHead.next.next

        return head
