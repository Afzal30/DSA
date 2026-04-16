#https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        lst = []
        for u,v in counter.items():
            heapq.heappush_max(lst,(v,u))

        print(counter)

        res = []
        for i in range(k):
            ans = heapq.heappop_max(lst)
            res.append(ans[1])

        return res
        
