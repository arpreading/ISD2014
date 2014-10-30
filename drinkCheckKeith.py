YES = "yes"
LIMIT = 18
response = input("Do you want wine? (please answer 'yes' or 'no')")
if response == YES:
    age = input("Are you over" +str(LIMIT) +  "?(please answer 'yes' or 'no'")
    if age == "yes":
        print("Please have a glass of wine")
    else:
        print("blurb about the law...")
else:
    print("Have an orange juice")
