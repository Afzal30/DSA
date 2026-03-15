#https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxwindow = []
        heap = []

        for i in range(len(nums)):

            heapq.heappush(heap,(-nums[i],i))

            while heap[0][1] <= i-k :
                heapq.heappop(heap)

            if i >= k-1:
                maxwindow.append(-heap[0][0])

        return maxwindow
        
