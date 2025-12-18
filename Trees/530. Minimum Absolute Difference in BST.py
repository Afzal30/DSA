#https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self,node,res):
        if not node:
            return
        
        if node.left:
            self.helper(node.left,res)
        res.append(node.val)
        if node.right:
            self.helper(node.right,res)

        return res

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        minimum = math.inf
        res = []
        res = self.helper(root,res)
        for i in range(1,len(res)):
            if abs(res[i]-res[i-1]) < minimum:
                minimum = res[i] - res[i-1]

        return minimum

        
        
