my_list=[1,3,5,55,37,54,21,33,65,98,89,11,10,5,8,64,73,24,28,66]
Max_Number = 0
Min_Number = my_list[0]
even_number= []
odd_number = []
Total = 0
for i in my_list :
    if i > Max_Number :
        Max_Number = i

    if i < Min_Number :
        Min_Number = i 

for i in my_list :
    Total += i 
Avrage_number = Total / len(my_list)
for i in my_list:
    if i %2 == 0 :
        even_number.append(i)
    else :
        odd_number.append(i)


print("max number =", Max_Number)
print("min number =", Min_Number)
print("total number = ",Total)
print("avrage number =",Avrage_number)
print("even number =",even_number)
print("odd number =",odd_number)