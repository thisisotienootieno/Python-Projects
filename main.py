import random

top_of_range = input("Enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    random_number = random.randrange(top_of_range)

else:
    print("Enter a number!")

guess = 0

while True:
    guess += 1
    guess_number = input("Guess a number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Enter a number!")
        continue

    if guess_number == random_number:
        print("Great! Correct Guess")

        if guess == 1:
            print(f"You got it after {guess} guess.")
        else:
            print(f"You got it after {guess} guesses.")

        break

    elif guess_number > random_number:
        print("Your guess is higher than the number.")

    else:
        print("Your guess is lower than the number.")
