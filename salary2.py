number=0
salary=0
total=0
while salary != -1:
    salary=float(input("Please enter a salary (type -1 to finish): "))
    while salary == -1 and number == 0:
        print("That is not a valid salary")
        salary=float(input("Please enter a salary (type -1 to finish): "))
    if salary == -1:
        break
    else:
        total += salary
        number += 1

print("Average salary is: ", total/number)
print("Total Salary: ", total)
if total == 0:
    number = 0
print("# of salaries: ",number)
