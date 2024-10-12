
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
def randDice(a,b):
    # Write your logic to generate 2 numbers between 1 and 6 here
    print(a+b)

    # Sum 2 numbers

    # return sum to calling function
sum = 0
for x in range(100):
    sum = sum + dice1 + dice2
    randDice(dice1,dice2)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
print(sum)
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
