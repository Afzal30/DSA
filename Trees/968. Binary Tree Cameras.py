#https://leetcode.com/problems/binary-tree-cameras/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node :
                return 0

            res = dfs(node.left) + dfs(node.right)

            cur = min (node.left.val if node.left else float('inf'), node.right.val if node.right else float('inf'))

            if cur == 0:
                node.val = 1
                res +=1

            elif cur == 1:
                node.val = 2

            return res
            
        
        return dfs(root) + (root.val==0)



            

        
