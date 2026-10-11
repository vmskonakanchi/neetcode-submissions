# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(node,max_val):
            nonlocal count

            if not node:
                return

            if node.val >= max_val:
                # if the node val is > the root val then the node is good
                count += 1

            traverse(node.left,max(max_val,node.val))
            traverse(node.right,max(max_val,node.val))

        traverse(root,root.val)

        return count        