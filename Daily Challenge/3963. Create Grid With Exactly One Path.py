#solved by own

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        for i in range(m):
            tmp = []
            for j in range(n):
                if i==0 or j==n-1:
                    tmp.append(".")
                else:
                    tmp.append("#")
            ans.append(''.join(tmp))
        return ans





        
