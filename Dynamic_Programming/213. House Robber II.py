class Solution:
    def rob(self, nums: List[int]) -> int:


        @cache
        def helper(n,flag):
            if n>=len(nums):
                return 0

            if flag:
                return max( nums[n]+helper(n+1,False), helper(n+1,True))
            else:
                return helper(n+1,True)

        return max(helper(0,True),helper(0,False))

            

#optimized version
"""Your logic is close, but the issue is with how you are handling the initial calls:

return max(helper(0,True,True),helper(0,False,False))

The second call:

helper(0, False, False)

means:

you are at house 0
but flag=False means you cannot rob this house

So this path is basically "skip first house".

But the first call:

helper(0, True, True)

incorrectly sets first_house_robbed=True before actually robbing it.

That creates wrong behavior because even if the recursion later decides to skip house 0, the last house is still treated as blocked.

Fix

You should only mark first_house_robbed=True when you actually rob house 0.

Replace this:

return max(helper(0,True,True),helper(0,False,False))

with:

return helper(0, True, False)

Then inside the rob choice:

nums[n] + helper(...)

update whether first house was robbed.

Corrected Version"""


from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        @cache
        def helper(n, can_rob, first_house_robbed):

            if n >= len(nums):
                return 0

            # last house
            if n == len(nums) - 1:

                # cannot rob last house
                if first_house_robbed or not can_rob:
                    return helper(n + 1, True, first_house_robbed)

                # can rob last house
                return max(
                    nums[n] + helper(n + 1, False, first_house_robbed),
                    helper(n + 1, True, first_house_robbed)
                )

            if can_rob:

                robbed_first = first_house_robbed or (n == 0)

                return max(
                    nums[n] + helper(n + 1, False, robbed_first),
                    helper(n + 1, True, first_house_robbed)
                )

            return helper(n + 1, True, first_house_robbed)

        return helper(0, True, False)
