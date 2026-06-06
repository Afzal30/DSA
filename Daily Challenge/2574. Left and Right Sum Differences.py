class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]
        rightsum = [0]
        left = 0
        right = 0
        n=len(nums)
        for i in range(1,n):
            left += nums[i-1]
            leftsum.append(left)
            right +=nums[n-i]
            rightsum.append(right)

        ans = []
        for i in range(n):
            diff = leftsum[i]-rightsum[n-i-1]
            ans.append(abs(diff))

        return ans
