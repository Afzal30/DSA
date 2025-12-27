# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.longest_path = 0

        def findheight(node):
            if not node:
                return 0
            leftheight = findheight(node.left)
            rightheight = findheight(node.right)

            left_arrow = 0
            right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = leftheight
            if node.right and node.right.val == node.val:
                right_arrow = rightheight


            self.longest_path = max(self.longest_path , left_arrow+right_arrow+1)
            return max(right_arrow, left_arrow) + 1

        findheight(root)
        return self.longest_path - 1 if self.longest_path else 0
