def digit(str):
    counter = 0
    for char in str:
        if char.isdigit():
            #print(char, "was found at position",counter)
            return True, counter
        else:
            counter += 1
    return False, -1        
