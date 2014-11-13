

inputName = input("Enter a file name: ")
checker = open("words.txt", "r")
infile = open (inputName, "r")
aliceSet = set()
for line in infile:
    line = line.rstrip()
    aliceSet.add(line)
        

      

splChk = set()
for line in infile:
    line = line.rstrip()
    splChk.add(line)
        

infile.close()

result = aliceSet.difference(splChk)
print(result)
