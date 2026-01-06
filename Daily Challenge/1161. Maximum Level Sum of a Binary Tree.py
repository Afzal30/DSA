#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        maxsum = float('-inf')
        maxlevel = 0
        cur_level = 0

        if not root:
            return

        queue = [root]


        while queue:
            cur_level += 1
            #print("cur_level ", cur_level )
            levelsize = len(queue)
            currentlevelnodes = []
            for i in range(levelsize):
                curr = queue.pop(0)
                currentlevelnodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #print("cur_level",cur_level)
            if sum(currentlevelnodes)>maxsum:
                maxsum = sum(currentlevelnodes)
                maxlevel = cur_level
            print(maxlevel,maxsum)
        return maxlevel

            
                
