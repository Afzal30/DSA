class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ele in s:
            #print(stack)
            if ele == ")":
                temp = ""
                while stack[-1]!='(':
                    temp += stack.pop(-1)
                stack.pop(-1)
                stack.extend(temp)
                #print("stack now",stack)
            else:
                stack.append(ele)
        #print("final stack",stack)
        return ''.join(stack)
        
