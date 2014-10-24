### Initialize constant variables for the max ranges.
##NMAX = 4
##XMAX = 10
### Print table header. 
##for n in range(1, NMAX + 1) :
## print("%10d" % n, end="")
##print()
##for n in range(1, NMAX + 1) :
## print("%10s" % "x ", end="")
##print("\n", " ", "-" * 35)
### Print table body.
##for x in range(1, XMAX + 1) : 
## # Print the x row in the table.
## for n in range(1, NMAX + 1) : 
##  print("%10.0f" % x ** n, end="")


def println(number):
    for n in range(1,13):
        print (n*number, end=" ")
    print()

def gen_table(number):
    println(1)
    println(number)

def generate(lst):
    for i in lst:
        gen_table(i)
        print("="*50)

generate([1,3,4])

    
