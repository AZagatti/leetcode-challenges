# Last updated: 07/05/2025, 23:36:53
# Iterative with queue, sinking the island points (1 to 0).
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def on_board(board, x, y):
            if x < 0 or x >= len(board):
                return False
            if y < 0 or y >= len(board[0]):
                return False
            return True

        island_count = 0
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    queue.append((r, c))
                    grid[r][c] = "0"
                while queue:
                    line, col = queue.popleft()

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        next_r, next_c = line + dr, col + dc

                        if on_board(grid, next_r, next_c) and grid[next_r][next_c] == "1":
                            queue.append((next_r, next_c))
                            grid[next_r][next_c] = "0"
        return island_count