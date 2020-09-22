def pthFactor(n, p):
    # Write your code here
    i = 1
    k = 0
    while i <= n:
        if n % i == 0:
            k += 1

        if k == p:
            return i

        i += 1

    return 0
