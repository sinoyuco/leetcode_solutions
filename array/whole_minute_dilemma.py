import collections
def playlist(songs):
    # Write your code here
    # quadratic, how to make linear?
    # ct = 0
    # for i in range(len(songs)):
    #     for j in range(i+1, len(songs)):
    #         if not (songs[i]+songs[j]) % 60:
    #             ct += 1
    # return ct

    #hashmap - linear
    ct = 0
    maps = collections.defaultdict(int)
    for i in songs:
        if i % 60 == 0:
            ct+=maps[0]
        else:
            ct += maps[60-i%60]
        maps[i%60] += 1
    return ct


