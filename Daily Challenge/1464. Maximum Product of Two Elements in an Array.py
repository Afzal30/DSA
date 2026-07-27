class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #print(nums)
        nums = sorted(nums)
        #print(nums)
        return (nums[-1]-1) * (nums[-2]-1)
        
