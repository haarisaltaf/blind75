# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # use two-poiinter to find the midpoint of the list then use that
        # to establish which half to reverse the linked list and append in order

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow == up to midpoint, fast = end

        # reverse second half

        current = slow.next
        slow.next = None
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        first = head
        second = previous

        while second:
            temp = first.next
            temp2 = second.next

            first.next = second
            second.next = temp

            first = temp
            second = temp2
