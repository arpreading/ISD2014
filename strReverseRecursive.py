def recursiveReverse(s):

    if len(s) ==1:
        return(s)
    else:
        return s[-1] + recursiveReverse(s[:-1])
