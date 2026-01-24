class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)

        maxsum = 0
        for i in range(int(len(nums)/2)):
            maxsum = max(maxsum, nums[i] + nums[len(nums)-1-i])
        return maxsum

        
