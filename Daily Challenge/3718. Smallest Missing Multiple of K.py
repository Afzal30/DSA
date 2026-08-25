class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i=1
        for ele in nums:
            if ele > (i*k):
                return i * k
            elif ele == (i*k):
                i+=1

        return i * k
            
        
