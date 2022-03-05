def game():
    print("\nWelcome to the game!")
    print("1. Play")
    print("2. Exit")
    choice = input("\nPlease choose an option: ")
    if choice == "1":
        print("\nYou have chosen to play the game.")
        game_play()
    elif choice == "2":
        exit()
    else:
        print("\nInvalid option. Please try again.")
        game()

def game_play():
    # generate a random number between 1 and 10
    import random
    random_number = random.randint(1, 10)
    # ask user to guess a number between 1 and 10
    guess = input("\nGuess a number between 1 and 10: ")
    # check if the guess is the same as the random number
    if guess == random_number:
        print("\nYou guessed correctly!")
        game()
    else:
        print("\nYou guessed incorrectly.")
        game_play()

game()