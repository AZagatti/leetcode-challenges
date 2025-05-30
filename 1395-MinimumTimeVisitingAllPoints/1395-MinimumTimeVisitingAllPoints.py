# Last updated: 29/05/2025, 21:42:13
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            point1 = points[i]
            point2 = points[i + 1]
            dx = abs(point2[0] - point1[0])
            dy = abs(point2[1] - point1[1])
            total_time += max(dx, dy)
        return total_time