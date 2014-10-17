num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
if num1 > num2:
    large = num1
    if num1 >num3:
        large = num1
elif num2 > num3:
    large = num2
else:
    large = num3

print(large)    
    
