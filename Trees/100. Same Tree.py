#https://leetcode.com/problems/same-tree/

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
            else:
                res.append("n")


        res.append(node.val)

        if node.right:
            right = self.helper(node.right,res)
            if right:
                res.append(right.val)

            else:
                res.append("n")

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        lst1= []
        lst2 = []
        self.helper(p,lst1)
        self.helper(q,lst2) 

        #
        return lst1 == lst2
    
#the above appoach is using helper function traver each node inorder method and compare the output array of two trees
#even though it is given 100% beats runtime, effective, in solution tab found that without helper function and even not to compare the whole tree
#that is we are comparing both trees simulatneowusly at any node it is not same we are returning false not comparing the rest of the tree 

        
##effective approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left , q.left) and self.isSameTree(p.right,q.right)

        
