# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous  # .next changed to point to previous
            previous = current
            current = temp
        return previous

# recrusively

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # base case:
        if head is None:
            return None

        if head.next is None:
            newHead = head
        # recursive case:
        else:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead
