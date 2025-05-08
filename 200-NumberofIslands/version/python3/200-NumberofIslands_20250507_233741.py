# Last updated: 07/05/2025, 23:37:41
# Recursive sinking the island points (0 to 1).
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def on_board(board, x, y):
            if x < 0 or x >= len(board):
                return False
            if y < 0 or y >= len(board[0]):
                return False
            return True

        island_count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if not on_board(grid, r, c) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r, next_c = r + dr, c + dc
                dfs(next_r, next_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                dfs(r, c)
                
        return island_count