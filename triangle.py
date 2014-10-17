n=int(input("Please enter a value"))
for i in range(n, n):
    n = n-1
    X = 0
    for j in range(n, n+1):
        X = (X*10)+1
    print(X)
