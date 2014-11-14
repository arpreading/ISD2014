##inputName = input("Enter a file name: ")
##infile = open (inputName, "r")
##record = {}
##line = infile.readline()
##for value in line:  
##    fields = line.split(":")
##    record["country"] = fields[0]
##    record["population"] = fields[1]
##
##
##print(record)
##infile.close

##infile = open ("populations.txt")
##newDict={}
##for line in infile:
##    countryName, population = line.split(";")
##    newDict[countryName] = int[population]
##
##infile.close    



infile = open ("populations.txt")
line = infile.readline()
newDict = {}
while line != '':
    words = line.split(":")
    newDict[words[0]] = int(words[1])
    #print(words)
    line = infile.readline()

   
infile.close()
