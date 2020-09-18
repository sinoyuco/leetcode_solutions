def numPlayers(k, scores):
    # Write your code here
    count = 0
    a = sorted(scores)
    i = 1
    for j in range(len(a)):
        if j == 0:
            count += 1
        else:
            if a[j] == a[j-1]:
                
                if i <= k:
                    count += 1
            else:
                
                i = j+1
                if i <= k:
                    count += 1
        print(i, a[j])

    return count


sco = [4,5,2,2,3,4,5]
print(numPlayers(4,sco))
