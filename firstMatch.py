def digit_present_and_position():
    string = input("Please enter string to check? ")
    found = True
    position = 0
    while found and position < len(string) :
       if string[position].isdigit() :
          found = False
       else :
          position += 1
    if not found :
       print("The digit is present and occurs at position", position)
    else :
       print("The string does not contain a digit.")

digit_present_and_position()
