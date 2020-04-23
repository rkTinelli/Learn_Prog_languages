for x in range(1,10):
    print(str(x) + " ", end='')
    x=x+1

print("\n"+"For Loop finished")
print("------------------------")

interactions = int(input("Give me a number "))

print("----- Normal count -----")
for x in range(0,interactions):
    x=x+1
    print(str(x) + " ", end='')
print("\n")

print("----- Squared reverse count -----")
for x in range(0,interactions):
    print(str((interactions - x)*(interactions - x)) + " ", end='')
    x=x+1
print("\n")