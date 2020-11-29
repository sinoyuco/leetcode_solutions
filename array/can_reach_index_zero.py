class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        def dfs(arr, pos):
            if pos >= 0 and pos < len(arr):
                nonlocal seen
                if arr[pos] == 0:
                    return True
                l,r = pos-arr[pos], pos+arr[pos]
                if r in seen and l in seen:
                    return False
                seen.add(l)
                seen.add(r)
                return dfs(arr, l) or dfs(arr, r)
            
        return dfs(arr, start)