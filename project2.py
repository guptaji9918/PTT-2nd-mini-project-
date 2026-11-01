print("1. veg Sandwitch:- Rs.60")
print("2. Masala DOsa:- RS.80")
print("3. Chole Rice:- RS.90")
print("4. Tea:- Rs.20")
print("5. Paneer roll:- Rs.100")

total = 0

while True:
    choice = int(input("\choose item number: "))
    quantity = int(input("Enter quantity: "))

    if choice == 1:
        name = "Veg Sandwich"
        price = 60

    elif choice == 2:
        name = "Masala Dosa"
        price = 80

    elif choice == 3:
        name = "Chole Rice"
        price = 90

    elif choice == 4:
        name = "Paneer Roll"
        price = 100

    elif choice == 5:
        name = "tea"
        price = 20

    else:
        print("invalid item number")
        continue

    if quantity <= 0:
        print("invalid quantity")
        continue

    cost = price * quantity
    subtotal = total + cost

    print(name,"x",quantity, "=", cost)


    again = input("Add another item? (y/n): ")

    if again == "n":
        break

print("total:", total)

if total >= 500:
    discount = total * 10 / 100

elif total >= 250:
    discount = total * 5 / 100

else:
    discount = 0

final_total = total - discount

print("Discount:", discount)
print("Final Total:", final_total)

print("Thank You!")