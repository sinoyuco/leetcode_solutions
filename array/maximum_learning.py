def maximumLearning(iv, articles, p):
    # Write your code here

    def dfs(articles, iv, pagesLeft, current):
        if pagesLeft == 0:
            maxiv = max(maxiv, current)
        for i in range(len(articles)):
            if pagesLeft > articles[0]*2:
                pagesLeft -= 2*articles.pop(0)
                current += iv.pop(0)
                dfs(articles, iv, pagesLeft, current)
            else:
                maxiv = max(maxiv, current)

    maxiv = 0
    dfs(articles, iv, p, 0)
    return maxiv
