file = open("scores.txt")
file_read = file.readlines()

len_file = 0
sum_number  = 0
file_list = []


for j in file_read:
    i = int(j)
    len_file += 1
    sum_number += i
    file_list.append(i)


Min_number = file_list[0]
Max_number = 0


for i in file_list:
    if Max_number < i :
        Max_number = i
    if Min_number > i :
        Min_number = i 
avrage = sum_number / len_file


file = open ("result_scores.txt","w")
file.writelines([f"Total = {sum_number}\n"
                    f"Avrage = {avrage}\n"
                    f"Max = {Max_number}\n"
                    f"Min = {Min_number}\n"
                    ])

file.close()