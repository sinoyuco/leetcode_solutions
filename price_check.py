def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    count = 0
    for i in range(len(productSold)):
        prod = productSold[i]
        actual_p = productPrices[products.index(prod)]
        if actual_p != soldPrice[i]:
            count += 1
    return count
