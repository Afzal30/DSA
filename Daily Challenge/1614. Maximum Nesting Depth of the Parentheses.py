class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        count =0
        for ele in s:
            if ele =="(":
                count +=1
            elif ele == ")":
                count -=1

            maxi = max(maxi, count)

        return maxi

        
