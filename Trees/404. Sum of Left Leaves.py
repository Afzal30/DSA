#https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tot = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0


        if root.left and not root.left.left and not root.left.right:
            self.tot += root.left.val

        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)

        return self.tot

#########another solution - passing flag 0 - left,1 - right along with the arguments so that ignore right chiled############

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.find_val(root, 1)
    
    def find_val(self, root: Optional[TreeNode], flag: int) -> int:
        if not root:
            return 0
        if flag == 0 and not root.right and not root.left:
            return root.val
        return self.find_val(root.left, 0) + self.find_val(root.right, 1)
