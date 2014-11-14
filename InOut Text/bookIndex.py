infile = open ("indexdata.txt")
line = infile.readline()
pgNum = {}
for line in infile:
    pageNum, words = line.split(":")
    print (pageNum, words)
    word = word.strip
    if word not in pgNum:
        pgNum[word] = {int(pagenum)}
    else:
        pgNum[word].add(int(pageNum))
    #pgNum[words] = int(pageNum)
   
    

print(pgNum)

infile.close()
