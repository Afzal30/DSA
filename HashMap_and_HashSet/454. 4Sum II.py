#https://leetcode.com/problems/4sum-ii/description/
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        pair_sum ={}
        count = 0
        for i in range(n):
            for j in range(n):
                tot = nums1[i]+nums2[j]
                pair_sum[tot] = pair_sum.get(tot,0)+1


        for k in range(n):
            for l in range(n):
                target = - (nums3[k] + nums4[l])

                count += pair_sum.get(target,0)

        return count
        
