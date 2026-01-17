class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        s = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                min_x = max(bottomLeft[i][0], bottomLeft[j][0])
                max_x = min(topRight[i][0], topRight[j][0])
                min_y = max(bottomLeft[i][1], bottomLeft[j][1])
                max_y = min(topRight[i][1], topRight[j][1])

                sLen = min(max_x - min_x, max_y - min_y)
                s = max(s, sLen)

        return s * s
        
