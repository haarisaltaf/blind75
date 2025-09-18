# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def findTarget(root, k, hashmap={}):
#print(root,k,hashmap, root.left, root.right)
# Terminating Case
    if (root.left.val is None) and (root.right.val is None):
        print('Both None')
        return False

# Base Case
    if (k  - root.val) in hashmap:
        print("in hashmap", k, root.val)
        return True

# Itertive Case
    if root.left.val is None:
        print(root.left.val)
        hashmap[root.val] = len(hashmap)
        return findTarget(root.right, k, hashmap)

    if root.right.val is None:
        print(root.right.val)
        hashmap[root.val] = len(hashmap)
        return findTarget(root.left, k, hashmap)
print("None worked")
