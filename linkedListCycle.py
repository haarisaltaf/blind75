# TODO: use 2-pointer for sliding window more efficient approach

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # sliding window approach -- so when the slow == fast.
        # -- by having a pointer move two at a time and the other moving only once, the fast will eventually overlap with the slow
        if head is None:
            return False

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            if slow == fast:
                return True
            slow = slow.next
        return False


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()

        if head is None:
            return False

        while head.next:
            if head in visited:
                return True

            else:
                visited.add(head)

            head = head.next
        return False
