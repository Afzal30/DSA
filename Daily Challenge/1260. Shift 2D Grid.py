class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        for i in range(k): #        for i in range(k%(m*n)): use modulo reduce duplicate roatations


            new_arr = [[0 for _ in range(n)] for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i==m-1 and j==n-1:
                        new_arr[0][0] = grid[i][j]
                    elif j == n-1:
                        new_arr[i+1][0] = grid[i][j]
                    else:
                        new_arr[i][j+1] = grid[i][j]

            grid = new_arr

        return grid
                                

        
