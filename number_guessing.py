# imports
import random

# create the guesser function
def num_guesser(max_num):

    random_n = random.randint(1,max_num) # generate a random value in range 1 - N
    count = 0 # counter system to stop limit guesses
    already_used = [] # list to let the player know that a number has already been used

    # while loop to provide multiple attempts with some condition statements
    while count <= 5:

        guess = input("Choose a number 1-{0}: ".format(max_num))
        guess = int(guess)

        if guess != random_n:
            if guess in already_used:
                print("{0} has already been used.".format(guess))
                count -= 1
            else:
                already_used.append(guess)
            print("{0} is not correct.".format(guess))
            count += 1
        elif count >= 5:
            break
        else:
            print("{} is the correct number!".format(guess))
            break
    else:
        print("Too many attempts. The Number was {0}, and you guessed {1}".format(random_n, guess))


# non integer values will trigger the exception.
try:
    num_guesser(max_num = int(input("Choose a max number N from 1-N: ")))
except (NameError, SyntaxError, ValueError):
    print("Invalid Input.")
