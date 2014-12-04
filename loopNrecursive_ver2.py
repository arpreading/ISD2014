def recursiveLoopN2(n):
    if n > 0:
        print("Hello")
        recursiveLoopN2(n-1)
        print("World")
