class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        visited = set()
        for ele in nums:
            if ele in visited:
                return ele
            else:
                visited.add(ele)
        
