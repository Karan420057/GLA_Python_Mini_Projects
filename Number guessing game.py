# Make a number guessing game

import random as r

n = int(input("Enter a range: "))
c = r.randrange(1, n)
y = int(input("Enter Your number: "))

if (y == 0):
    print("Game Over, player quite the game")
elif (y == c):
    print("Congrulations you are right. The random number was:", c)
else:
    print("Better luck next time")
