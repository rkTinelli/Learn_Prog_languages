userName1 = input("Enter name 1: ")
userAge1 = int(input("Enter age 1: "))
userName2 = input("Enter name 2: ")
userAge2 = int(input("Enter age 2: "))

if userAge1 == userAge2 :
    print(userName1 + " and " + userName2 + " have the same age")
elif(userAge1 > userAge2):
    print(userName1 + " is older than " + userName2)
else:
    print(userName2 + " is older than " + userName1)