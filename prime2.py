val_1=[]
val_2=[]
val_3=[]
for limit in range(1,21):
    prime = True
    for value in range (2,limit):
        if (limit % value == 0):
            prime = False
    if prime == True:
        val_1.append(limit)
        val_2.append(limit**2)
        val_3.append(limit**3)
   
        

print(val_1)
print(val_2)
print(val_3)
    #print(val_2)
    #print(prime,end="\t")    

