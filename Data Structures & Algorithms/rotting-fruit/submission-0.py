from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        # Part 1: put every rotten orange in line, and count the fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        # Part 2: spread the rot, one orange at a time
        while queue:
            row, col, time = queue.popleft()
            minutes = time
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for nr, nc in neighbors:
                # Part 3: is the neighbor on the grid and a fresh orange?
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))

        # Part 4: did every orange rot?
        if fresh > 0:
            return -1
        return minutes