# 



# make a random number
import random
random_number = random.randint(1, 10)

# ask the user to guess a number
guess = int(input("Guess a number between 1 and 10: "))

# compare the user's guess to the random number
if guess == random_number:
    print("You got it!")
else:
    print("Nope. The number I was thinking of was {}".format(random_number))

