class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        diff = r-l
        for i in range(len(nums)):
            if i + l - 1 < len(nums):
                tot1 = sum(nums[i:i+l])
                #print("tot1", tot1)
                if tot1 > 0 :
                    ans = min(ans,tot1)
                j=1
                while i+j-1 < len(nums) and j<=diff:
                    tot2 = sum(nums[i:i+j+l])
                    #print("tot2", tot2)
                    if tot2 > 0 :
                        ans = min(ans,tot2)
                    j+=1

            #print(ans)
        if ans == float('inf'): 
            return -1
        else:
            return ans
            


        
