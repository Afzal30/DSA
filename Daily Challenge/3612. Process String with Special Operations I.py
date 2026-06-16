class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for ele in s:
            if ele == "*":
                if res:
                    res = res[:-1]
            elif ele == "#":
                res += res
            elif ele == "%":
                res = res[::-1]

            else:
                res += ele

        return res        
