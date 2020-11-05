def fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    # Write your code here
    rev = False if sortOrder == 0 else True
    #sort the array based on sort parameter and order
    news = sorted(items, key=lambda x: int(x[sortParameter]) if sortParameter != 0 else x[sortParameter], reverse=rev)

    result = []
    #append the name to result if item index divided by items per page indicates that
    #  the item should be on the given page.
    for i in range(len(news)):
        if i//itemsPerPage == pageNumber:
            result.append(news[i][0])
    return result
