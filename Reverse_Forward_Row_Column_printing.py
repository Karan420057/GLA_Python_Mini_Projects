# Make a mini project on printing the number according to user input in which firstly take choice for reverse order and forward order then take choice for printing in row or column by taking starting point, ending point, updation

sp = int(input("Enter the starting point: "))

ep = int(input("Enter the ending point: "))
up = int(input("Enter the updation: "))

choice1 = input("Enter your choice for forward printing or reverse printing: ")
choice2 = input("Enter your choice for row printing or column printing: ")

if choice1 == "forward":
    if choice2 == "row":
        for i in range(sp, ep, up):
            print(i, end=", ")
    elif choice2 == "column":
        for i in range(sp, ep, up):
            print(i)
    else:
        print("Second choice is not correct. Enter a valid choice.")
elif choice1 == "reverse":
    if choice2 == "row":
        for i in range(ep, sp, -up):
            print(i, end=", ")
    elif choice2 == "column":
        for i in range(ep, sp, -up):
            print(i)
    else:
        print("Second choice is not correct. Enter a valid choice.")
else:
    print("Your both choices are wrong.")
