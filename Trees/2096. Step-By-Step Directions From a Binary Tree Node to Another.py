#https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findpath(node,val,path):
            if node.val==val:
                return True
            if node.left and findpath(node.left,val,path):
                path+="L"
            elif node.right and findpath(node.right,val,path):
                path +="R"
            return path

        src_val_path = []
        dest_val_path = []

        findpath(root,startValue,src_val_path)
        findpath(root,destValue,dest_val_path)



        while len(src_val_path) and len(dest_val_path) and src_val_path[-1]== dest_val_path[-1]:
            src_val_path.pop()
            dest_val_path.pop()



        return "".join("U" * len(src_val_path)) + "".join(reversed(dest_val_path))

