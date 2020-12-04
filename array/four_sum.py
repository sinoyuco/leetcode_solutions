from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        maps = defaultdict(int)
        result = 0
        for i in range(len(A)):
            for j in range(len(A)):
                maps[A[i]+B[j]] += 1
        for x in range(len(C)):
            for y in range(len(C)):
                result += maps[-C[x]-D[y]]
        return result
