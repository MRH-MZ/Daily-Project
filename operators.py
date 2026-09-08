print()
print()
print("                        Calculator")
print("---------------------------------------------------------------")
print()
number_1_input = int(input("Enter the Number 1 : "))
number_2_input = int(input("Enter the Number 2 : "))
print()
print("---------------------------------------------------------------")
print()
Addition = number_1_input + number_2_input
Subtraction = number_1_input - number_2_input
Multiplication = number_1_input * number_2_input
Division = number_1_input / number_2_input
Floor_Division = number_1_input // number_2_input
Modulus = number_1_input % number_2_input
Exponentiation = number_1_input ** number_2_input
print("number 1 + number 2 : " ,Addition)
print("number 1 - number 2 : " ,Subtraction)
print("number 1 * number 2 : " ,Multiplication)
print("number 1 / number 2 : " ,Division)
print("number 1 // number 2 : " ,Floor_Division)
print("number 1 % number 2 : " ,Modulus)
print("number 1 ** number 2 : " ,Exponentiation)
print()
print("                        Operators")
print("---------------------------------------------------------------")
print()
print("number 1 > number 2 : ",number_1_input > number_2_input)
print("number 1 < number 2 : ",number_1_input < number_2_input)
print("number 1 <= number 2 : ",number_1_input <= number_2_input)
print("number 1 >= number 2 : ",number_1_input >= number_2_input)
print("number 1 == number 2 : ",number_1_input == number_2_input)
print("number 1 != number 2 : ",number_1_input !=number_2_input)
print()
print("---------------------------------------------------------------")
print()

if number_1_input > number_2_input :
    print(f"number 1 : Max ( {number_1_input} )")
    print(f"number 2 : Min ( {number_2_input} )")
elif number_1_input < number_2_input :
    print(f"number 1 : Min ( {number_1_input} )")
    print(f"number 2 : Max ( {number_2_input} )")
else:
    print("number 1 == number 2  (Equal)")
print()
print("---------------------------------------------------------------")
print()
if number_1_input %2 == 0 :
    print("number 1 = Even ")
else :
    print("number 1 = Odd ")
print()
if number_2_input %2 == 0 :
    print("number 2 = Even ")
else :
    print("number 2 = Odd ")
print()
print("---------------------------------------------------------------")
print()


