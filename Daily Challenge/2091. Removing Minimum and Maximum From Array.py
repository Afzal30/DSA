#https://leetcode.com/problems/removing-minimum-and-maximum-from-array/?envType=daily-question&envId=2026-08-30
#solved by Own
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        n = len(nums)
        print(n)
        print(a,b)
        half = n//2
        index_a = nums.index(a)
        index_b = nums.index(b)
        print(index_a,index_b)

        if index_a == index_b:
            return 1

        else:
            if index_a < index_b:
                count1 = index_a + 1 + min(n - index_b, index_b - index_a)
                count2 = n - index_b + min(index_a + 1,index_b-index_a)
                return min(count1,count2)
            else:
                count1 = index_b + 1 + min(n - index_a, index_a - index_b)
                count2 = n-index_a + min(index_b + 1,index_a-index_b) 
                return min(count1,count2)


#simple clearn apperoach

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        return min(
            right + 1,                  # Remove both from left
            n - left,                   # Remove both from right
            left + 1 + n - right        # One from each side
        )

                

        




        
