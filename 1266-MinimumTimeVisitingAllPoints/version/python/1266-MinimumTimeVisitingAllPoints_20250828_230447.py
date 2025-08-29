# Last updated: 28/08/2025, 23:04:47
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(1, len(points)):
            point = points[i - 1]
            next_point = points[i]
            result += max(abs(next_point[0] - point[0]), abs(next_point[1] - point[1]))
        return result
