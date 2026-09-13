print()
print("Magic Laboratory")
print()
input_range_number = int(input("How many numbers? "))
count= 1
List_number = []
print()

for i in range(input_range_number) :
    numbers = int(input(f"Number {count} : "))
    List_number.append(numbers)
    count += 1

Total = 0
Even_number = 0
Odd_number = 0
Max_number = List_number[0]
Min_number = List_number[0]
for i in List_number:

    Total += i 
    if i %2 == 0 :
        Even_number += 1
    elif i %2 != 0 :
        Odd_number += 1
    if i < Min_number:
        Min_number = i
    elif i > Max_number :
        Max_number = i 

print()
print(f"Total = {Total}")
print(f"Even = {Even_number}")
print(f"Odd = {Odd_number}")
print(f"Max number = {Max_number}")
print(f"Min number = {Min_number}")
print()


