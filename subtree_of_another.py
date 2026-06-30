# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_subtree(r,p):
            if not r and not p:
                return True
            elif  (r and not p) or (p and not r):
                return False
            elif r.val!=p.val:
                return False
            return check_subtree(r.left,p.left) and check_subtree(r.right,p.right)
        def has_subtree(r):
            if not r:
                return False
            if check_subtree(r,subRoot):
                return True
            return has_subtree(r.left) or has_subtree(r.right)
        return has_subtree(root)
    
        