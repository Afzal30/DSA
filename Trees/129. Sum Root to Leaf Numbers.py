#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    

    def helper(self,node,sum,lst):

        if not node:
            return 0

        if not node.left and not node.right:
            sum += str(node.val)
            lst.append(sum)

        left = self.helper(node.left,sum+str(node.val),lst)
        right = self.helper(node.right,sum+str(node.val),lst)

        return lst



        

        


        

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        lst =[]

        ans = self.helper(root,"",lst)
        print(ans)
        tot = 0
        for ele in ans:
            tot += int(ele)

        return tot
        

        
""""
Runtime
0
ms
Beats
100.00%
Analyze Complexity
Memory
17.70
MB
Beats
85.99%

"""


#we can try another apporch without type conversion


class Solution:

    

    def helper(self,node,sum):

        if not node:
            return 0

        #this is core logic to add sum of value of node while traversing, 
        sum = sum *10 + node.val

        if not node.left and not node.right:
            return sum

        left = self.helper(node.left,sum)
        right = self.helper(node.right,sum)

        return left + right
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        return self.helper(root,0)
       
