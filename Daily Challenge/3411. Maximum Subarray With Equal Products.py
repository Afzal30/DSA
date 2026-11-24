class Solution:
    def maxLength(self, nums: List[int]) -> int:

        length = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = nums[i:j+1]
                prod = math.prod(temp)
                gcd = math.gcd(*temp)
                lcm = math.lcm(*temp)

                if prod == gcd * lcm :
                    length = max(len(temp),length)

        return length
