n = int(input("Please enter the number of rounds in the game:"))
print()
x = int(input("Please enter the number you want to perform the operation on:"))
print()
print("description : If the number is even, divide it by 2. If the number is odd, multiply it by 2 and subtract 1.")
print()
for i in range(n) :
    if x %2 == 0:
        x = x // 2
    elif x %2 != 0 :
        x = (x * 2) - 1
print(x)