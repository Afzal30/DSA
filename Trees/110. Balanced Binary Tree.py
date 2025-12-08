#https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self,node):

        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        return max(left,right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
