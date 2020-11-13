def weight_combinations(weights, maxCapacity):
    result = []
    for i in range(len(weights)):
        if weights[i] <= maxCapacity:
            rec_call = weight_combinations(weights[(i+1):],maxCapacity-weights[i])
            result.append(rec_call+weights[i])
    if(len(result)==0):
        return 0
    return max(result)

print(weight_combinations([7,4,4],8))
    