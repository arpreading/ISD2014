def listMaxRecursive(lst):
    if len(lst) == 1:
        return(lst[0])
    else:
        mx = listMaxRecursive(lst[1:])
        if lst[0] > mx:
            return(lst[0])
        else:
            return mx
        
