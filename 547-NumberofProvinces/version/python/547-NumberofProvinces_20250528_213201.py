# Last updated: 28/05/2025, 21:32:01
'''
-----
Using Union-Find.
-----
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        provinces = n
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            nonlocal provinces
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                parent[root1] = root2
                provinces -= 1
                return True
            return False

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return provinces

