# Take the name, age and id proof from the user and by compare hir/her age make a voting sysment for that

name = input("Enter your name: ")
age = int(input("Enter your age: "))
id = int(input("Enter your adhar number: "))
if (age >= 18):
    print("You are eligible for vote.")
    choice = input("Enter your voting prty form BJP, Congress, NDA, Nota: ")
    if(choice == "BJP"):
        print("BJP")
    elif (choice == "Congress"):
        print("Congress")
    elif(choice == "NDA"):
        print("NDA")
    else:
        print("Nota")
else:
    print("You are not eligible for vote.")