#https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        
        def dfs(node):
            if not node:
                return float('inf'),float('-inf'),0

            leftmin, leftmax, leftsum = dfs(node.left)
            rightmin, rightmax, rightsum = dfs(node.right)

            if (leftmax < node.val < rightmin):
                temp  = leftsum + rightsum + node.val
                self.ans = max(self.ans,temp)

                return min(leftmin,node.val),max(rightmax,node.val),temp

            return float('-inf'),float('inf'),0

        dfs(root)

        return self.ans
