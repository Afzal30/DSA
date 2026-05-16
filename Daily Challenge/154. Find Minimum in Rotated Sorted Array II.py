class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start + end) //2

            if nums[mid] < nums[end]:
                end = mid  # minimum is in left half including mid
            elif nums[mid] > nums[end]:
                start = mid + 1  # minimum is in right half excluding mid
            else:
                end -= 1  # nums[mid] == nums[right], cannot decide, safely shrink

        return nums[start]
