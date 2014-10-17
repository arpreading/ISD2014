def digit_present_and_position():
    string = input("Please enter string to check? ")
    noDigit = 0
    position = 0
    while position < len(string) :
       if string[position].isdigit() :
          noDigit += 1
          print("A digit is present and occurs at position", position)
          position += 1
       else:
          position += 1 
    if noDigit == 0:
        print("The string does not contain a digit.")

digit_present_and_position()
