#ISD2014 Coursework 1. Andrew Reading-Legh (areadi01@mail.bbk.ac.uk) ID#12930317
#String formatting learnt from Python Docs & StackOverflow

rVal = 0 #Richter Scale Value
qList=[1,5,9.1,9.2,9.5]#List containing example Richter Scale Values
qList_len = len(qList)
for i in range (0,qList_len):
    rVal = qList[i]
    joules = 10**((1.5*rVal)+4.8)#Energy in Joules released for a particular Richter scale measurement
    tnt = joules/(4.184*10**9)#One ton of exploded TNT yields 4.184e9 joules
    print('Richter Scale Value: {:<4.1f} Joules: {:<15.8e} TNT: {:<10.8e}'.format(rVal, joules, tnt))
print()

def quake():
    rVal=float(input("Please enter a Richter Scale Value: "))
    joules = 10**((1.5*rVal)+4.8) 
    tnt = joules/(4.184*10**9) 
    print("Richter Scale Value: ", rVal)
    print("Equivalence in Joules: {:15.8e}".format(joules))
    print("Equivalence in tons of TNT: {:10.8e}".format(tnt))

quake()
