def member (item, lst):
    found = False
    index = 0
    while not found and index < len(lst):
        if item == lst[index]:
            found = True
        index += 1    
    return found    

member("a",["a",2,3,4])
member(2,["a",2,3,4])

def member_list(lst_of_items, lst):
    match = True
    for i in lst_of_items:
        if not member(i,lst):
            match = False
    return match    

# tests
print(member_list([],[]))
print(member_list(["a"],[]))
print(member_list(["a",2],["a",2,3,4]))
print(member_list([6,"a"],[1,2,3,"a"]))
print(member_list([6,"a"],[1,2,3]))
