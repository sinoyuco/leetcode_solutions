def maxTickets(tickets):
    tickets = sorted(tickets)
    m = curr = 0
    for i in range(len(tickets)-1):
        if tickets[i+1] - tickets[i] <= 1:
            curr += 1
            if curr > m:
                m = curr
        else:
            curr = 0
    return m+1
