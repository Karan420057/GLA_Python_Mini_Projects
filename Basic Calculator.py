# Make a basic calculator using if else

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
choice = input("Enter the choice from 'add, sub, multiply or division': ")
if (choice == 'add'):
    c = a + b
    print("The addition of your numbers is:", c)
elif (choice == 'sub'):
    c = a - b
    print("The subtraction of your numbers is:", c)
elif (choice == 'multiply'):
    c = a * b
    print("The multiplication of your numbers is:", c)
elif (choice == 'division'):
    c = a // b
    print("The division of your numbers is:", c)
else:
    print("You give the wrong choice")