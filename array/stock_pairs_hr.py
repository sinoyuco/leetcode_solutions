def stockPairs(stocksProfit, target):
    # Write your code here
    maps = {}
    # [5,7,9,..]
    count = 0
    seen = set()
    for i in range(len(stocksProfit)):
        curr = stocksProfit[i]
        if target-curr in maps and (min(curr, target-curr),max(curr, target-curr)) not in seen:
            count +=1
            seen.add((min(curr, target-curr), max(curr, target-curr)))
        else:
            maps[curr] = 1
    return count