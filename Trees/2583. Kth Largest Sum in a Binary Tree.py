#https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        level_sum = []
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
            level_sum.append(sum(currentlevelnodes))

        print(level_sum)

        return sorted(level_sum)[-k] if len(level_sum)>=k else -1
            
