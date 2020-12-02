def playlist(songs):
    # Write your code here
    ct = 0
    for i in range(len(songs)):
        for j in range(i+1, len(songs)):
            if not (songs[i]+songs[j]) % 60:
                ct += 1
    return ct
