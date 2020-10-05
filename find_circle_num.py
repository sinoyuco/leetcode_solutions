class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited = [False]*len(M)

        def dfs(student):
            visited[student] = True
            for s in range(len(M)):
                if M[student][s] and not visited[s]:
                    dfs(s)

        for i in range(len(M)):
            if not visited[i]:
                count += 1
                dfs(i)
        return count
