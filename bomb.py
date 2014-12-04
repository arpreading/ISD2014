def bomb(n):
    if n != 1:
        print("tick...")
        bomb(n-1)
    else:    
        print("boom")

    
