#https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,res):
        if not node:
            return None

        if node.left:
            left = self.helper(node.left,res)

            if left:
                res.append(left.val)

        res.append(node.val)

        if node.right:
            right = self.helper(node.right,res)
            if right:
                res.append(right.val)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        self.helper(root,res)
        return res
        



        
