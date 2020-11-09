def recursive_multip(a,b):
    lo = a if a < b else b
    hi = b if b > a else a

    def product(lo,hi):
        if lo == 0:
            return 0
        elif lo == 1:
            return hi

        halflo = lo // 2
        halfmult = product(halflo, hi)

        if lo % 2 == 0:
            return halfmult + halfmult
        else:
            return halfmult + halfmult + hi

    return product(lo, hi)


print(recursive_multip(10,7))
