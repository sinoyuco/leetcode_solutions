def deleteProducts(ids, m):
    # Write your code here
    freq_sorted = sorted(ids, key=ids.count, reverse=False)
    return len(set(freq_sorted[m:]))
