class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def recursive_call(c, s):
            if len(s) == k:
                result.append(s)
                return
            for i in range(c, n+1):
                recursive_call(i+1,s+[i])

        recursive_call(1, [])
        return result