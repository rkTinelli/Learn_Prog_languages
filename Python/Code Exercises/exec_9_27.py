daysWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

indexRequired = int(input("Give me a number: "))
print(daysWeek[indexRequired])
print("------------------------")

listLikedThings = []

userName = input("Enter your name: ")

for x in range(0,5):
    listLikedThings.insert(x,input("Enter a thing you like: "))

print(userName + " likes ",end='')
for x in range(0,5):
    print(listLikedThings[x] + " ",end='')