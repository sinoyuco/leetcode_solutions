class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        # '1 4 3 2219'
        # arr = ['1']
        #k = 3
        for i in num:
            while k and arr and arr[-1] > i:
                arr.pop()
                k -= 1
            arr.append(i)

        while k:
            arr.pop()
            k -= 1

        result = ''.join(arr).lstrip('0')
        return result if result != '' else '0'
