        
#https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,lst):
        if not node:
            return
        
        self.helper(node.left,lst)
        self.helper(node.right,lst)
        lst.append(node.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        lst=[]

        self.helper(root,lst)
        return lst
        
