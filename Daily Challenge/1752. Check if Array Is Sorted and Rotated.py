class Solution:
    def check(self, nums: List[int]) -> bool:
        #flag = False
        def is_sorted(arr):
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    return False
            return True

        if is_sorted(nums):
            return True
        for i in range(len(nums)-1):
            #print(i," rotation")
            new_arr = nums[i+1:]+nums[:i+1]
            #print(new_arr)
            if is_sorted(new_arr):
                return True
                

        return False
