# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # create a new list and append current roots to it with a key of levels in it -> so maybe a dictionary
        level_dict = {} # level -> list
        root_level = 0

        def traverse(node,level):
            if not node:
                return
            if level not in level_dict:
                level_dict[level] = list()
            level_dict[level].append(node.val)
            traverse(node.left,level + 1)
            traverse(node.right,level + 1)

        cur = root
        traverse(cur,root_level)

        return list(level_dict.values())
