#https://leetcode.com/problems/k-closest-points-to-origin/description/
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        myheap = []

        for x,y in points:

            dist = x*x + y*y
            
            heapq.heappush(myheap,(-dist,[x,y]))

            if len(myheap) > k:
                heapq.heappop(myheap)


        return [point for (_,point) in myheap]

        
        
