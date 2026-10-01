class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in  s:
            if ele in ("(","{", "["):
                stack.append(ele)
            else:
                if len(stack)==0:
                    return False
                else:
                    if ele == ")":
                        if stack[-1]=="(":
                            stack.pop(-1)
                        else:
                            return False
                    elif ele == "}":
                        if stack[-1]=="{":
                            stack.pop(-1)
                        else:
                            return False
                    elif ele == "]":
                        if stack[-1]=="[":
                            stack.pop(-1)
                        else:
                            return False
        if len(stack)==0:
            return True
        else:
            return False
                
