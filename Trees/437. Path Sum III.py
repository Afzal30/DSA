#https://leetcode.com/problems/path-sum-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,path):
            if not node:
                return 0

            path.append(node.val)
            temp_sum = 0
            count = 0
            print(path)
            for val in reversed(path):
                temp_sum += val
                if temp_sum == targetSum:
                    count+=1
            
            count += dfs(node.left,path)
            count += dfs(node.right,path)
            path.pop()
            return count

        return dfs(root,[])
        
