import random
import math
print "Welcome to Sam's Math Test"
num1= random.randint(1, 10)
num2= random.randint(1, 10)
num3= random.randint(1, 10)
l=[num1, num2, num3]
maxlist = max(l)
minlist = min(l)
print(l)
print(maxlist)
print(minlist)
sqrtOne = math.sqrt(num1)
correct = False
while(correct == False):
    guess3= raw_input("Is the square root of " + str(num1) + " greater than or equal to 2? (y/n): ")
    if sqrtOne >= 2.0 and str(guess3) == "y":
        print("Correct!")
        correct = True
    elif sqrtOne < 2.0 and str(guess3) == "n":
        print("Correct!")
        correct = True
    else:
        print("Incorrect, try again")

