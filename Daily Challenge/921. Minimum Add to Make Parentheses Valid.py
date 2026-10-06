class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for ele in s:
            if ele == "(":
                stack.append(ele)
            else:
                if len(stack)>0 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    stack.append(ele)

        return len(stack)
