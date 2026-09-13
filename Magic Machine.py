n = int(input("Enter the Number : "))
print(n)
while n != 1 :
    if n %2 == 0 :
        n = n // 2
        print(n)
    elif n %2 != 0 :
        n = (n * 3) + 1
        print(n)
