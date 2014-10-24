def member (item, lst):
    found = False
    index = 0
    while not found and index < len(lst):
        if item == lst[index]:
            found = True
        index += 1    
    return found    

##def member (item, lst):
##    found = False
##    index = 0
##    while not found and index < len(lst):
##        found = item == lst[index]
##        index += 1
##    return found    
            
print(member("a",[]))
print(member("a",["a",2,3,4]))
print(member("a",[1,2,3,"a"]))
print(member("a",[1,2,3]))
