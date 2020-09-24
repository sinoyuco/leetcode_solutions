def scatterPalindrome(str):
    result = []
    for i in range(len(str)):
        a = str[i]
        count = 0
        for j in range(len(a)):
            b = set()
            for k in range(j, len(a)):
                if a[k] in b:
                    b.remove(a[k])
                else:
                    b.add(a[k])

                if len(b) < 2:
                    count+=1

        result.append(count)
    return count


print(scatterPalindrome('abba'))
            