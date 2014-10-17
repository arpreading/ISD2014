val_1=[]
val_2=[]
val_3=[]
count = 0 # number of primes
#while count < 7:
for limit in range(1,21):
    if (limit == 2 or limit % 2 != 0):        
        prime = True
        for value in range (3,limit,2):
            if (limit % value == 0):
                prime = False
                break
        if prime == True:
            val_1.append(limit)
            val_2.append(limit**2)
            val_3.append(limit**3)
            count += 1
            if count >= 6:
                break

print(val_1)
print(val_2)
print(val_3)
  
