class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        #print(nums)
        missed = []
        for i in range(len(nums)-1):
            temp =nums[i]
            while temp + 1 != nums[i+1]:
                missed.append(temp+1)
                temp += 1
                #print(temp)

        return missed



        
