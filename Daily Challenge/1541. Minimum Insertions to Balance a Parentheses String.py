class Solution:
    def minInsertions(self, s: str) -> int:

        stack = []
        counter = 0
        index = 0

        while index<len(s):
            ch = s[index]

            if ch =="(":
                stack.append(ch)
            
            else:
                if not stack:
                    counter +=1
                    stack.append("(")
                
                if (index < len(s)-1 and s[index+1]==")"):
                    index += 1
                    stack.pop()

                else:
                    counter +=1
                    stack.pop()

            index +=1

        return counter + len(stack)*2
        
