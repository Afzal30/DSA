class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kdict = {}

        for ele in knowledge:
            kdict[ele[0]] =ele[1]

        stack = []
        ans = ""
        for ele in s:
            #print("stack",stack)
            if ele == ')':
                temp=""
                while stack[-1] != "(":
                    #print("stack in while",stack)
                    temp += stack.pop(-1)

                stack.pop(-1)
                key = temp[::-1]
                val = kdict.get(key,"?")
                stack.append(val)

            else:
                stack.append(ele)

        return "".join(stack)


         

        
