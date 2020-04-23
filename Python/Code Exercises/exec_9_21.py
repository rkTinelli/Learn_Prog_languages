x = 0
while x<= 10:
    print(str(x) + " ", end='')
    x=x+1

print("\n"+"While Loop finished")
print("------------------------")

loopCounter = 0
userAnswer = True

while (userAnswer):
    loopCounter = loopCounter +1
    print("Loop interaction number " + str(loopCounter))
    answerText = input("Run loop again? [Y/N]").upper()
    if answerText == "Y":
        userAnswer = True
    else:
        userAnswer = False #No need for this since the break will exit the loop
        break

print("\n"+"While Loop finished")
print("------------------------")