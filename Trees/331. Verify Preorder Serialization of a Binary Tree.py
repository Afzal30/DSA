#https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        lst = preorder.split(",")

        degree = 1

        for ele in lst:
            degree -= 1

            if degree < 0 :
                return False

            if ele != "#":
                degree +=2

        return degree == 0
        

"""Another approach  
for each element in the string, append the character,
and while stack length>2 and the last 2 character of stack is ## and the last 3rd character is not #:
pop for 3 times
append # for 1 time """

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        data structure: stack, binary search tree
        algorithm: preorder traversal scanning 
        time complexity: O(n)
        space complexity: O(n)

        """
        stack=[]
        for n in preorder.split(","):
            stack.append(n)
            while len(stack)>2 and stack[-2:]==["#"]*2 and stack[-3]!="#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return stack==["#"]
