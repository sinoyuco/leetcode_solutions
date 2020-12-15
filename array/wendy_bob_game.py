def gameWinner(colors):
    # Write your code here
    wc = bc = 0
    for i in range(1,len(colors)-1):
        c = colors[i]
        cp = colors[i-1]
        cn = colors[i+1]
        if c == cp == cn == 'w':
            wc+=1
        elif c == cp == cn =='b':
            bc+=1
    return 'wendy' if wc > bc else 'bob'