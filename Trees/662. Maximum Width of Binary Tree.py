#https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = []
        self.max_width = 0

        def dfs(node,depth,index):

            if not node:
                return
            
            if len(queue) == depth:
                queue.append(index)
            curr_width = index - queue[depth] + 1

            self.max_width = max(curr_width,self.max_width)


            dfs(node.left,depth+1,index*2)
            dfs(node.right,depth+1,index*2+1)

        dfs(root,0,0)
        
        return self.max_width
