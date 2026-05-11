#https://leetcode.com/problems/target-sum/description/
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        hashmap = {}
        def solve(cursum,i):
            if (cursum,i) in hashmap:
                return hashmap[(cursum,i)]
            if i==len(nums):

                if cursum == target:
                    return 1

                return 0

            positive = solve(cursum+nums[i],i+1)
            negative = solve(cursum-nums[i],i+1)

            hashmap[(cursum,i)] = positive + negative
            return positive + negative

        return solve(0,0)
            
