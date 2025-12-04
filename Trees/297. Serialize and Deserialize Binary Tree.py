#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    string = ""
    def helper(self,node):

        if not node:
            self.string+="n,"
            return self.string

        self.string += str(node.val) + ","

        self.helper(node.left)
        self.helper(node.right)   

        return self.string     

    def helper2(self,data):
        
        val = data.pop(0)

        if val == "n":
            return None

        node = TreeNode(int(val))

        node.left = self.helper2(data)
        node.right = self.helper2(data)

        return node



    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = self.helper(root)
        print("ans",ans)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        node = self.helper2(data)
        return node

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
