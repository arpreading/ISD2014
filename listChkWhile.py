def member (item, lst):
    found = False
    counter = 0
    while counter < len(lst):
        if item in lst:
            found = True
        else:
            found = False
        counter+=1    
    return found   
    
        
        
print(member("a",[]))
print(member("a",["a",2,3,4]))
print(member("a",[1,2,3,"a"]))
print(member("a",[1,2,3]))
