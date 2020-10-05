class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join(["0" if i == "1" else "1" for i in "{0:b}".format(N)]), 2)
