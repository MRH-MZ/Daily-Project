Count_number = 0
Total_number = 0
Maxmum_number = 0
Count = 1
input_number = None
print()
print("Enter numbers one by one.")
print("Enter 0 to finish.")
print("-------------------------------------------")
print()

while input_number != 0 :
    input_number = int(input(f"Enter the number {Count} : "))
    Count += 1
    if input_number < 0 :
        continue
    if input_number > 1000 :
        break
    if input_number > 0 :
        Count_number += 1 
        Total_number += input_number
        if input_number > Maxmum_number :
            Maxmum_number = input_number 


print(f"count = {Count_number}")
print(f"total = {Total_number}")
print(f"Maxmum = {Maxmum_number}")