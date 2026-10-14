
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    island_count += 1

                    queue = deque()
                    queue.append((row, col))
                    grid[row][col] = "0"

                    while queue:
                        current_row, current_col = queue.popleft()

                        directions = [
                            (-1, 0),
                            (1, 0),
                            (0, -1),
                            (0, 1)
                        ]

                        for row_change, col_change in directions:
                            neighbor_row = current_row + row_change
                            neighbor_col = current_col + col_change

                            if (
                                0 <= neighbor_row < rows
                                and 0 <= neighbor_col < cols
                                and grid[neighbor_row][neighbor_col] == "1"
                            ):
                                queue.append((neighbor_row, neighbor_col))
                                grid[neighbor_row][neighbor_col] = "0"

        return island_count
