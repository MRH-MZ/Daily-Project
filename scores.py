file = open("scores.txt")
file_read = file.readlines()
for i in file_read:
    file_int = int(i)
    print(file_int)