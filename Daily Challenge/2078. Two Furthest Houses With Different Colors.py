class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max1,max2=0,0
        for i in range(len(colors)-1,0,-1):
            if colors[0] != colors[i]:
                max1 =  i
                break
        for j in range(len(colors)):
            if colors[j]!=colors[-1]:
                max2=len(colors)-1-j
                break
        return max(max1,max2)


        
