def climbingLeaderboard(ranked, player):
    # Write your code here
    #brute force approach - time limits exceeded
    # ranks = []
    # for i in range(len(player)):
    #     r_count = 1
    #     for j in range(len(ranked)):
    #         if player[i] >= ranked[j]:
    #             ranks.append(r_count)
    #             break

    #         if j == len(ranked)-1:
    #             ranks.append(r_count+1)

    #         if j == 0:
    #             r_count += 1
    #         else:
    #             if ranked[j] != ranked[j-1]:
    #                 r_count += 1
    # return ranks

    #shorter than O(n*m) because l is not resetted so you don't go through the entire array.
    uniq = list(set(ranked))
    uniq.sort(reverse=True)
    print(uniq)
    ranks = []
    l = len(uniq)
    for s in player:
            while (l > 0) and (s >= uniq[l-1]):
                l -= 1
            ranks.append(l+1)
    return ranks


