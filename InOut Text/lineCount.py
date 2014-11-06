inputName = input("Enter a file name: ")
infile = open (inputName, "r")
line = infile.readline()
count = 0
while line != "":
    line = infile.readline()
    count += 1

infile.close()
print("The number of lines in the file", inputName,"is: ",count)    
