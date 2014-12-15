diamond = int(input("Please input length of side: "))
for y in range (0, diamond+1):
    print(""*(diamond-y) + "*"*(2*y -1))

for y in range (diamond-1,0,-1):
    print(""*(diamond-y) + "*"*(2*y -1))
        
