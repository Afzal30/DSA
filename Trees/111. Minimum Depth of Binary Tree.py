#https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

############################using recursion##############################3
class Solution:

    
    def minDepth(self, root: Optional[TreeNode]) -> int:

        hieght = 0

        if not root:
            return 0

        leftheight = self.minDepth(root.left)
        rightheight = self.minDepth(root.right)

        if root.left and root.right:
            return min(leftheight, rightheight) + 1
        elif root.left and not root.right:
            return leftheight+1
        elif root.right and not root.left:
            return rightheight+1
        else:
            return 1
        
############################using queue or iteration##############################
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = [(root,1)]

        while queue:

            node,depth = queue.pop(0)

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))


        
