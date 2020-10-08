class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        maps = {'}': '{', ')': '(', ']': '['}
        for i in s:
            if i in maps:
                if arr:
                    t = arr.pop()
                else:
                    t = '#'

                if maps[i] != t:
                    return False
            else:
                arr.append(i)
        return True if len(arr) == 0 else False
