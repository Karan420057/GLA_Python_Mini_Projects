# write a python program which accept the name from the user and marks of 5 subjects . Calculate the percentage grade on the basis of their percentage. if user enter any subject marks more than 100 or less than 0 print "wrong input". if user enter string in place of marks print "wrong input". Print the percentage only when the marks are above 0 and below 100 otherwise stop the code

name = input("Enter your name: ")

try:
    sub1 = float(input("Enter marks for subject 1: "))
    sub2 = float(input("Enter marks for subject 2: "))
    sub3 = float(input("Enter marks for subject 3: "))
    sub4 = float(input("Enter marks for subject 4: "))
    sub5 = float(input("Enter marks for subject 5: "))
    
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total) / 5

    if (0 <= sub1 <= 100 and 0 <= sub2 <= 100 and 0 <= sub3 <= 100 and 0 <= sub4 <= 100 and 0 <= sub5 <= 100):

        print(f"\n{name}, your percentage is: {percentage}%")
        if(percentage >= 90):
            print("Your grade = A")
        elif(percentage >= 85):
            print("Your grade = B+")
        elif(percentage >= 80):
            print("Your grade = B")
        elif(percentage >= 75):
            print("Your grade = C+")
        elif(percentage >= 70):
            print("Your grade = C")
        elif(percentage >= 65):
            print("Your grade = D+")
        elif(percentage >= 50):
            print("Your grade = D")
        elif(percentage < 50):
            print("Your grade = F")
    else:
        print("Wrong input. Marks should be between 0 and 100.")

except ValueError:
    print("Wrong input. Please enter valid numbers for marks.")