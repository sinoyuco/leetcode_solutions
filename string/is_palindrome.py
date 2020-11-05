class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        a, y = '', x
        while y > 0:
            a += str(y % 10)
            y //= 10

        return int(a) == x
