class Solution(object):
    def letterCombinations(self, digits):
        if digits == '':
            return []

        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = ['']

        for i in digits:
            temp = []
            for j in result:
                for m in maps[i]:
                    temp.append(j+m)
            result = temp
        return result

