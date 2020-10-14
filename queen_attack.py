def queensAttack(n, k, r_q, c_q, obstacles):
    maps, count = {}, 0
    for j in obstacles:
        maps[''.join([str(v) for v in j])] = 1

    dirs = [[1, 1], [-1, -1], [1, -1], [-1, 1],
            [0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in dirs:
        cur = [r_q, c_q]
        while 1 <= cur[0] <= (n) and 1 <= cur[1] <= (n):
            cur[0] += i[0]
            cur[1] += i[1]

            if ''.join([str(val) for val in cur]) in maps or not(1 <= cur[0] <= (n) and 1 <= cur[1] <= (n)):
                break
            else:
                count += 1
    return count
