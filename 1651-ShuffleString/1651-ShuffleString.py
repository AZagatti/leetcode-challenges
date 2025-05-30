# Last updated: 29/05/2025, 21:42:17
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [""] * len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        return "".join(arr)