#https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if not root:
            return

        queue = [root]
        while queue:

            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(res)
        countdict = {}
        for ele in res:
            if ele not in countdict:
                countdict[ele] = 1
            else:
                 countdict[ele] += 1

        
        get_mode = [ k for k,v in countdict.items() if v==max(list(countdict.values()))]

        return get_mode


#######using counter, recursion dfs############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        vals=[]
        dfs(root)
        counter = Counter(vals)
        mx = max(counter.values())
        return [k for k,v in counter.items() if v==mx]
