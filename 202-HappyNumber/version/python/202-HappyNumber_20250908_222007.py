# Last updated: 08/09/2025, 22:20:07
class Solution:
    def isHappy(self, n: int) -> bool:
        viewed = set()
        tmp = n
        while tmp != 1:
            new_tmp = 0
            while tmp:
                new_tmp += pow(tmp % 10, 2)
                tmp //= 10
            if new_tmp in viewed:
                break
            viewed.add(new_tmp)
            tmp = new_tmp
        return tmp == 1