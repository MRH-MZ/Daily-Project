money = int(input("Enter the Money Items : "))
if money > 50000:
    Discount = money * 20/ 100
    result = money - Discount
    print()

    print(f"Your payable amount after the discount is : {result:.0f}")

elif 50000 >= money >= 20000 :
    Discount = money * 10 / 100
    result = money - Discount
    print()
    print(f"Your payable amount after the discount is : {result:.0f}")

elif money == 0 :
    print()
    print("You did not select any products.")

elif money < 20000 :
    print()
    print("You are not eligible for a discount.")
    print(f"Your payable amount : {money}")

