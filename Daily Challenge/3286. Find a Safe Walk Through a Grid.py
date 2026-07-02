class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Compute starting health
        rem_health = health-1 if grid[0][0] else health

        # If starting health <= 0:
        #     return False
        if rem_health<=0:
            return False

        # best_health = ...
        best_health = [[float('-inf')] * cols for _ in range(rows)]

        # queue.append(...)
        queue.append((0,0,rem_health))


        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        best_health[0][0] = rem_health

        while queue:

            row, col, health = queue.popleft()

            # Destination?
            if row == rows-1 and col == cols-1:
                return True

            # Explore all four directions
            for x,y in directions:

                next_health = health

                # Bounds
                nx,ny = x+row,y+col
                if nx<0 or ny<0 or nx>=rows or ny>=cols:
                    continue

                # Compute next health
                if grid[nx][ny] == 1:
                    next_health -=1

                # Health <= 0
                if next_health <=0:
                    continue

                # Better than previous?
                if next_health > best_health[nx][ny]:
                    best_health[nx][ny] = next_health
                    queue.append((nx,ny,next_health))

                # Update

                # Push into queue

        return False
