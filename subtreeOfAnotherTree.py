# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # traverse till node == subroot head
        # then check if rest matches to rubroot
        def checkRest(tree1, tree2):
            if not tree1 and not tree2:
                return True

            if tree1.val != tree2.val:
                return False

            return checkRest(tree1.left, tree2.left) and checkRest(tree1.right, tree2.right)

        if root and subRoot:
            if root.val == subRoot.val:
                return checkRest(root, subRoot)
            return self.isSubtree(root.left, subRoot.left) or self.isSubtree(root.right, subRoot.right)

        return False
