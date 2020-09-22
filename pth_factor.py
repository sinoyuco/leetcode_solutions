def pthFactor(n, p):
    # Write your code here
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors += [i, n//i]

    unique = sorted(list(set(factors)))
    # print(unique)
    return 0 if p > len(unique) else unique[p-1]
