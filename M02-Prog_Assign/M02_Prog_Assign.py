# 4.1 - Number Guessing Game.
print("----4.1----")
# Secret number and guesser's number variables.
secret_number = 8
guess = 6
# Compares the guesser's number to the Secret Number. Prints outcome.
if guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Congratulations!")

# 4.2 - Vegetation Match Game.
print("----4.2----")
# Boolean values for variables.
small = False
green = False
# Creates different possible outcomes.
if small == True:
    if green == True:
        print("It's a pea!")
    else:
        print("It's a cherry!")
else:
    if green == True:
        print("It's a watermelon!")
    else:
        print("It's a pumpkin!")

# 6.1 - Print list using "For" loop.
print("----6.1----")
# List of numbers.
list = [3, 2, 1, 0]
# Loop for printing numbers in list.
for number in list:
    print(number)

# 6.2 - Guessing Game using "While Loop".
print("----6.2----")
# Secret number and guesser's number variables.
guess_me = 7
number = 1
# Compares number and guess_me variable.  With every loop, number incremented.
while number:
    if number < guess_me:
        print("Too low!")
        number += 1
    elif number == guess_me:
        print("You found it!")
        number += 1
    else:
        # Ends program once number has surpassed guess_me.
        print("Oops!")
        break

# 6.3 - For loop counter in range of 10.
print("----6.3----")
#Hidden number.
guess_number = 5
# Loop that searches the range for correct answer.
for number in range(0, 10):
    if number < guess_number:
        print("Too low!")
    elif number == guess_number:
        print("Found it!")
    else:
        # Message to alert user that the number is too high.
        print("Oops!")


