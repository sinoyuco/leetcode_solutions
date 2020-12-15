class Solution:
    def addDigits(self, num: int) -> int:
        l = sum([int(i) for i in str(num)])
        while l >= 10:
            t = sum([int(i) for i in str(l)])
            l = t
        return l
