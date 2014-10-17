x = int(input("ENTER NUMBER: "))
temp = []
a = 0
cs = []
for w in range(1,x+1):
    cs.append(str(w))
    temp.append(str(w))
print("LATIN SQUARE OF %s" % (x) + "\n")
print("  ".join(cs))
for y in range(x-1):
    temp.append(cs[0])
    temp.pop(0)
    cs = temp
    print("  ".join(cs))
