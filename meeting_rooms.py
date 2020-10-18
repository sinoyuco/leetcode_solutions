def meetingRooms(arr):
    # arr = [[0,30], [5,10], [15,20]]
    l,h = [i[0] for i in arr], [j[1] for j in arr]
    l, h = sorted(l), sorted(h)
    rooms = 0
    while l:
        start = l.pop(0)
        if start < h[0]:
            rooms+=1
        else:
            h.pop(0)

    return rooms

# print(meetingRooms([[0, 30], [5,10], [15, 20]]))
# print(meetingRooms([(1, 3), (9, 18), (3, 7), (6, 12), (4, 9)]))


