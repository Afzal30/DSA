#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    root = None

    def insertree(self,node,value):
        if not node:
            node = TreeNode(value)
            return node

        if value < node.val:
            node.left = self.insertree(node.left,value)
        if value > node.val:
            node.right = self.insertree(node.right,value)

        return node
        


    def insert(self,value):
        self.root = self.insertree(self.root,value)

    def createbst(self,nums,start,end):

        if end<=start:
            return

        mid = (start+end) // 2

        self.insert(nums[mid])
        self.createbst(nums,start,mid)
        self.createbst(nums,mid+1,end)



    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        self.createbst(nums,0,len(nums))

        return self.root



        
