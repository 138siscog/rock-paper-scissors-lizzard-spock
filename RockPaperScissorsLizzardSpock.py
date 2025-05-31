import random
# Options to choose from
options = ("rock", "paper", "scissors", "lizzard", "spock")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input(
            "Enter a Choice, Rock, Paper, Scissors, Lizzard, Spock\n")

    print(f"player:{player}")
    print(f"player:{computer}")

# Choice Loop
    if player == computer:
        print("It's a Draw!")
    elif player == "rock" and computer == "lizzard":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    elif player == "lizzard" and computer == "spock":
        print("You Win!")
    elif player == "spock" and computer == "scissors":
        print("You Win!")
    elif player == "scissors" and computer == "lizzard":
        print("You Win!")
    elif player == "lizzard" and computer == "paper":
        print("You Win!")
    elif player == "paper" and computer == "spock":
        print("You Win!")
    elif player == "spock" and computer == "rock":
        print("You Win!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    else:
        print("You Lose!")
# Replay Logic
    if not input("play again? (y/n)").lower() == "y":
        running = False
print("Thanks for playing!")
input("press ENTER to exit")
