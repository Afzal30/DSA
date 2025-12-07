#https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        queue = [root.left,root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True
