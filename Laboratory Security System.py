import random 

numbers = random.randint(1,999)
count_Rounds = 5
count_number = 1
rounds = 0

while count_Rounds > 0 :
    print(numbers)
    
    input_number = int(input(f"Enter the number {count_number} : "))

    rounds += 1
    count_Rounds -= 1
    count_number += 1

    if input_number == 0 :

        print("System Locked")
        break

    if input_number == numbers :

        print("Access : Granted")
        print(rounds)
        break

    else :

        print("Wrong Password")
        if input_number > numbers :
            print("Your number is greater than the computer's number.")
        if input_number < numbers :
            print("Your number is less than the computer's number.")
        continue

if count_Rounds == 0 :

    print("Access : Denied")
    print(rounds)