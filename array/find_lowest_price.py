def findLowestPrice(products, discounts):
    # Write your code here
    maps = {}
    subtotal = 0
    for i in discounts:
        maps[i[0]] = str(i[1]) + " " + str(i[2])
    for j in products:
        price = int(j[0])
        lowest = price
        for d in j[1:]:
            if d != 'EMPTY':
                splitted = maps[d].split()
                t, am = splitted[0], int(splitted[1])
                if t == '0':
                    if am < lowest:
                        lowest = am
                elif t == '1':
                    if (price-(price*am/100)) < lowest:
                        lowest = (price-(price*am/100))
                else:
                    if (price-am) < lowest:
                        lowest = (price-am)
        subtotal += lowest
    return int(subtotal)
