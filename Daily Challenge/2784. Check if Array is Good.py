class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n+1:
            return False

        nums.sort()
        #print(nums)

        for i in range(len(nums)-2):
            #print(nums[i])
            if nums[i]+1 !=nums[i+1]:
                return False

        return True



        
