#https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        tree_val = []

        def inorder(node,tree_val):
            if not node:
                return

            if node.left:
                inorder(node.left,tree_val)

            tree_val.append(node.val)

            if node.right:
                inorder(node.right,tree_val)

        inorder(root,tree_val)
        print(tree_val)

        def bs_floor(lst,target,start,end):
            while start<=end:
                mid = start + (end-start)//2
                if lst[mid]==target:
                    return [target,target]
                elif lst[mid]>target:
                    end = mid-1
                else:
                    start = mid+1

            return [lst[end] if end>=0 else -1 , lst[start] if start<len(lst) else -1]

        
        tot_nodes = len(tree_val)
        res = []
        for ele in queries:
            res.append(bs_floor(tree_val,ele,0,tot_nodes-1))

        return res


        
