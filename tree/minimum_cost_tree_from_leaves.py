class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [math.inf]
        for i in range(len(arr)):
            while stack and stack[-1] <= arr[i]:
                res += stack.pop()*min(arr[i], stack[-1])
            stack.append(arr[i])

        while len(stack) > 2:
            res += stack.pop()*stack[-1]

        return res
