# Last updated: 29/05/2025, 21:42:20
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        max_content = 0
        g.sort()
        s.sort()
        for cookie_size in s:
            if cookie_size >= g[max_content]:
                max_content += 1
                if max_content == len(g): break
        return max_content