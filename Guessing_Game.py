import random
import math

# accepting input of higher number
low = int(input("Enter Low bound:- "))

# accepting input of lower number
high = int(input("Enter High bound:- "))

# creating a random number between the two
x = random.randint(low, high)
print("\n\tYou got ",
      round(math.log(high - low + 1, 2)),
      " trys to guess the number!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(high - low + 1, 2):
    count += 1

    # guess is an input here
    guess = int(input("Guess the number:- "))

    # Testing
    if x == guess:
        print("Nice!!!! you guessed it in ",
              count, " try")
        # If it equals the correct number, game ends
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# if they try too many guesses it shows this
if count >= math.log(high - low + 1, 2):
    print("\nThe number is %d" % x)
    print("\tNice Try Tho!!!")
