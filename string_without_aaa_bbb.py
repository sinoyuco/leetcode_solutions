def strWithout3a3b(self, A: int, B: int) -> str:
    str = ''
    while A > 0 or B > 0:
        if str[-2:] == 'aa':
            str += 'b'
            B -= 1
        elif str[-2:] == 'bb':
            str += 'a'
            A -= 1
        else:
            if B > A:
                str += 'b'
                B -= 1
            else:
                str += 'a'
                A -= 1
    return str
