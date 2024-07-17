import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Type Rock/Paper/Scissors or Q to Quit: ")
    user_pick = user_pick.lower()
    if user_pick == "q":
        print("Good Bye! Game over!")
        break
    else:
        if user_pick not in options:
            print("Option Not Available!")
            continue

        random_number = random.randrange(3)

        computer_pick = options[random_number]
        print(f"Computer picked {computer_pick}")

        if user_pick == "rock" and computer_pick == "scissors":
            print("You Won!")
            user_wins += 1

        elif user_pick == "scissors" and computer_pick == "paper":
            print("You Won!")
            user_wins += 1

        elif user_pick == "paper" and computer_pick == "rock":
            print("You Won!")
            user_wins += 1

        elif user_pick == computer_pick:
            print("Nobody Won!")

        else:
            print("You Lost!")
            print("Computer Wins")
            computer_wins += 1

    print(f"You won {user_wins} times.")
    print(f"Computer won {computer_wins} times.")
    if computer_wins > user_wins:
        print("Computer Wins.")
    elif computer_wins == user_wins:
        print("The game is a Draw!")
    else:
        print("You Win!")

total_plays = user_wins + computer_wins
user_percentage = (user_wins / total_plays) * 100
print(f"The game was played {total_plays} times and the Player won {user_percentage}% of the times.")
