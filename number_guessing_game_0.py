# Yael Kadosh task 2 day 3: Guess the number
# V Create a file called number_guessing_game_0.py
# V Using the random module the computer "thinks" about a whole number between 1 and 20.
# The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if it was the same.
# The game ends after just one guess.


import random
the_number=random.randint(1, 20)

guess_the_number=input("Guess a whole number between 1 and 20: ")
the_guess=int(guess_the_number)

if the_guess==the_number:
    print("correct")
elif the_guess<the_number:
    print("the number is bigger")
else:
    print("The number is smaller")

print("the number is " + str(the_number))
print("Done")
