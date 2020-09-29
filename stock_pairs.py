def stockPairs(stocksProfit, target):
    # Write your code here
    count = 0
    maps = {}
    for i in range(len(stocksProfit)):
        for j in range(i, len(stocksProfit)):
            if stocksProfit[i] + stocksProfit[j] == target and (str(stocksProfit[i])+str(stocksProfit[j])) not in maps:
                count += 1
                maps[(str(stocksProfit[i])+str(stocksProfit[j]))] = 1
                maps[(str(stocksProfit[j])+str(stocksProfit[i]))] = 1
    return count
