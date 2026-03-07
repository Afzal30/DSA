#https://leetcode.com/problems/merge-bsts-to-create-single-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        n = len(trees)

        #if only one BST is given, return it
        if n==1:
            return trees[0]

        #list of leaf node of the given BSTs
        all_leaves_node = set()
        for tree in trees:
            #print("tree.val",tree.val)
            if tree.left:
                all_leaves_node.add(tree.left.val)
            if tree.right:
                all_leaves_node.add(tree.right.val)

        #print("all_leaves_node",all_leaves_node)


        #find the root node in which other bst can be merged
        root = None
        for tree in trees:
            if tree.val not in all_leaves_node:
                root = tree

        #if we can't fine root, we can't build merged bst
        if not root:
            return None

        #list of trees other than root tree
        list_of_remaining_tree = []
        for tree in trees:
            if tree != root:
                list_of_remaining_tree.append(tree)

        
        #create a dictionary to map the value to it tree
        root_tree_dictionary = {}
        for tree in list_of_remaining_tree:
            root_tree_dictionary[tree.val] = tree

        #merging the BSTs
        self.helper(root,root_tree_dictionary)

        #check the final root is valid BST
        if len(root_tree_dictionary)==0 and self.checkvalidbst(root, float('-inf'), float('inf')):
            return root

        return None


    def helper(self,root,root_tree_dictionary):
        if not root:
            return None

        #if root is find in dictionary then we can merget and remove the root from the dictinory
        if root.val in root_tree_dictionary:
            tree = root_tree_dictionary[root.val]
            root.left = tree.left
            root.right = tree.right
            root_tree_dictionary.pop(root.val)

        left = self.helper(root.left,root_tree_dictionary)
        right = self.helper(root.right,root_tree_dictionary)


    #function to check valid BST or not

    def checkvalidbst(self,node,minvalue,maxvalue):
        if not node:
            return True

        if node.val < minvalue or node.val > maxvalue:
            return False

        return ( self.checkvalidbst(node.left,minvalue,node.val-1) and 
                 self.checkvalidbst(node.right,node.val+1,maxvalue) )


#https://www.youtube.com/watch?v=leTbZ4LK7lA - video explanation

              
        




        

        
        
