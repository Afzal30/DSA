# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0:
            return None

        r = preorder[0]


        for i in range(len(inorder)):
            if r == inorder[i]:
                index = i
                break

        node = TreeNode(r)

        node.left  = self.buildTree(preorder[1:index+1],inorder[0:index])
        node.right = self.buildTree(preorder[index+1:len(preorder)],inorder[index+1:len(inorder)])

        return node

        
        
