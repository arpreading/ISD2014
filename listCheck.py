yal = ['Katy B', 'fudgebar', 2, 'AW', 'Kate Nash']
newlst = ['slts',[yal],'I have no idea']

def member (item, lst):
    found = False
    for x in lst:
        if == x item:
            found = True
            break

    return found

#for a in list(lst):
#    if a == True:
#        print("List win")
#    else:
#        print("List boo)

#tests
print(member("a",[]))
print(member("a",["a",2,3,4]))
print(member("a",[1,2,3,"a"]))
print(member("a",[1,2,3]))

#"""refactor the above code to use a while loop, no break, no multi return"""
