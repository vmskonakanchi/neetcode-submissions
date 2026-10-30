# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(node,res):
            if not node:
                return
            res.append(node.val)
            traverse(node.left,res)
            traverse(node.right,res)

        res = []
        traverse(root,res)
        res.sort()

        return res[k - 1]