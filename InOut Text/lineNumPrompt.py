from sys import argv
inputName = argv[1]
infile = open (inputName, "r")
line = 0
count = 1
while line != "":
    line = infile.readline()
    if line == "":
        break
    print("/*",count,"*/",line)
    count += 1

infile.close()
 
