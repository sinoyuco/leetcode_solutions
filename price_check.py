def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here

    maps = {}
    for i in len(products):
        maps[products[i]] = productPrices[i]

    count = 0
    for i in range(len(productSold)):
        prod = productSold[i]
        actual_p = maps[prod]
        if actual_p != soldPrice[i]:
            count += 1
    return count
