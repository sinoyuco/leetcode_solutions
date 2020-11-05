def findCircleNum(M):
    count = 0
    visited = [False]*len(M)

    def dfs(student):
        visited[student] = True
        for s in range(len(M)):
            if M[student][s] and not visited[s]:
                dfs(s)

    for i in range(len(M)):
        print(visited)
        if not visited[i]:
            print(i)
            count += 1
            dfs(i)
    return count


a = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(a))
