#https://leetcode.com/problems/subarray-sum-equals-k/description/
#https://www.youtube.com/watch?v=fFVZt-6sgyo
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        cursum = 0

        #key = prefix_sum , value = count of prefix_sum till that index
        #for the first element there is no prefix sum or it is 0 
        #as we are traking the count of each prefix sum occrued so far, so 0 occured 1 time, for the first element, hence initiliaze dict with 0:1

        prefix_sum_count = { 0: 1} 

        for num in nums:
            cursum += num
            diff = cursum - k
            res += prefix_sum_count.get(diff,0)
            prefix_sum_count[cursum] = prefix_sum_count.get(cursum,0) + 1


        return res






        
