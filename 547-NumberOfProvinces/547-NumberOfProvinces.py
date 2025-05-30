# Last updated: 29/05/2025, 21:42:21
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        province_count = 0
        def dfs(current_city):
            visited.add(current_city)
            for neighbor in range(n):
                if isConnected[current_city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        for i in range(n):
            if i not in visited:
                province_count += 1
                dfs(i)
        return province_count
                