# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if q and p and q.val == p.val:
            L = self.isSameTree(p.left, q.left)
            R = self.isSameTree(p.right, q.right)
            return L and R

        else:
            return False


        