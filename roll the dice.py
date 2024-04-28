import random as r

i = 1
s1 = s2 = 0
while (i < 7):
    c = r.randint(1, 6)
    y = int(input("Enter a number between 1 to 6: "))
    choice = input("If you quite type 'quite' otherwise type 'no': ")
    s1 += c
    s2 += y
    if (choice == 'quite'):
        break
    elif (choice == 'no'):
        continue
    else:
        print("Wrong choice")
        break

print("\n")
print("Your scour is:", s2)
print("The computer's score is:", s1)

print("\n")

if (s1 > s2):
    print("Computer won with the score of:", s1)
else:
    print("You won with the score of:", s2)