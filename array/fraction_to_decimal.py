class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        initialn, initiald = num, den
        res = ""
        num, den = abs(num), abs(den)
        d, r = divmod(num, den)
        res += str(d)
        if r != 0:
            res += '.'
            maps = {}
            while r != 0:
                if r in maps:
                    res = res[:maps[r]]+'('+res[maps[r]:]+')'
                    break
                maps[r] = len(res)
                r *= 10
                d = r//den
                r = r % den
                res += str(d)
        return res if initialn*initiald > 0 or initialn == 0 else '-'+res
