def stockPairs(stocksProfit, target):
    # Write your code here
    count = 0
    maps = {}
    # for i in range(len(stocksProfit)):
    #     for j in range(i, len(stocksProfit)):
    #         if stocksProfit[i] + stocksProfit[j] == target and (str(stocksProfit[i])+str(stocksProfit[j])) not in maps:
    #             count += 1
    #             maps[(str(stocksProfit[i])+str(stocksProfit[j]))] = 1
    #             maps[(str(stocksProfit[j])+str(stocksProfit[i]))] = 1
    # return count

    for i in range(len(stocksProfit)):
        if (target-stocksProfit[i]) in maps and maps[(target-stocksProfit[i])] == 0:
            maps[(target-stocksProfit[i])] = 1
            count += 1
        else:
            maps[stocksProfit[i]] = 0
    return count

print(stockPairs([1,1,3,46,1,3,9], 47))
