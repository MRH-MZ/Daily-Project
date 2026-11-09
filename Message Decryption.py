import random

Initial_input = int(input("If you want the computer to generate a message , enter 1 . if you want to create a message yourself, enter 2 . : "))
if Initial_input == 1 :
    Alphabet_Bank = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    Number_Bank = [0,1,2,3,4,5,6,7,8,9]
    numbers = 2
    Random_number = 1
    number_random = random.randint(2,10)
    number_random2 = random.randint(1,10)

    for i in range (numbers) :
        if Random_number == 1:
            message = random.choices(Alphabet_Bank,k=number_random)
            Random_number += 1

        elif Random_number == 2:
            message_2 = random.choices(Number_Bank,k=number_random2)

    len_message = len(message)
    number_random3 = random.randint(1,len_message)

    result = []
    count = 0
    i = 1

    while number_random3 > count  :
        number_random4 = random.randint(0,len_message - i) 
        message_3 = message.pop(number_random4)
        result.append(message_3)
        count += 1
        i += 1

    result_string = ""
    for i in range (len(result)):
        result_string += result[i]
    x =result_string.upper()

    list_upper = []
    for i in x:
        list_upper.append(i)


    result_Decryption = message + message_2 + list_upper
    random.shuffle(result_Decryption)

    Message_Decryption = ""
    for i in range (len(result_Decryption)):
        Message_Decryption += str(result_Decryption [i])
    print(Message_Decryption)
    Encrypted_message = ""
    orthers = ["0","1","2","3","4","5","6","7","8","9"," "]
    for i in Message_Decryption :
        if i == i.upper() and i not in orthers:
            ord_variable2 = ord(i)
            variable_subrtaction2 = ord_variable2 - 65
            operations2= (variable_subrtaction2 + 3) % 26
            variable_addition2 = operations2 + 65
            variable_chr2 = chr(variable_addition2)
            Encrypted_message += variable_chr2           
        elif i not in orthers :
            ord_variable = ord(i)
            variable_subrtaction = ord_variable - 97
            operations = (variable_subrtaction + 3) % 26
            variable_addition = operations + 97
            variable_chr = chr(variable_addition)
            Encrypted_message += variable_chr            
        else:
            Encrypted_message += i
            continue

            
    print(f"Received Mesage =  {Message_Decryption}  and Encrypted Message =  {Encrypted_message}  ")
elif Initial_input == 2 :
    print()
    input_message = input("Enter the message decryption : ")
    Encrypted_message = ""
    orthers = ["0","1","2","3","4","5","6","7","8","9"," "]
    for i in input_message :
        if i == i.upper() and i not in orthers:
            ord_variable2 = ord(i)
            variable_subrtaction2 = ord_variable2 - 65
            operations2= (variable_subrtaction2 + 3) % 26
            variable_addition2 = operations2 + 65
            variable_chr2 = chr(variable_addition2)
            Encrypted_message += variable_chr2           
        elif i not in orthers :
            ord_variable = ord(i)
            variable_subrtaction = ord_variable - 97
            operations = (variable_subrtaction + 3) % 26
            variable_addition = operations + 97
            variable_chr = chr(variable_addition)
            Encrypted_message += variable_chr            
        else:
            Encrypted_message += i
            continue

            
    print(f"Received Mesage =  {input_message}  and Encrypted Message =  {Encrypted_message}  ")
else:
    print("error Try again") 