def sumAlistRecursive(lst):
    if len(lst) == 1:
        return(lst[0])
    else:
        return lst[0] + sumAlistRecursive(lst[1:])
