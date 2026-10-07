# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_set = set()
        q_set = set()

        def traverse(node,unique_set,pos,level):
            if not node:
                return
            
            unique_set.add((pos,node.val,level))

            traverse(node.left,unique_set,"left",level + 1)
            traverse(node.right,unique_set,"right",level + 1)

        
        traverse(p, p_set,"root",0)
        traverse(q, q_set,"root",0)

        return p_set == q_set

        