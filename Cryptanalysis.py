message = input("Please enter your message : ")
others = [1,2,3,4,5,6,7,8,9,"!","@","#","$","%","^","&","*",]
keys = 1
for i in message :
    result_message = ''
    while True:
        if keys > 3 :
            break
        if i not in others:
            ord_message = ord(i)
            variable_subrtaction = ord_message - 97
            Operation = (variable_subrtaction - keys) % 26
            variable_sum = Operation + 97
            chr_message = chr(variable_sum)
            result_message += chr_message
            break
            
    keys += 1
    print(result_message)
        