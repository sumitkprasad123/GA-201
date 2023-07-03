import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    print("  ")
    
    choices = ["rock", "paper", "scissors"]
    rounds_won = 0
    computer_rounds_won = 0
    draws = 0

    while True:
        player_choice = input("Your turn: ")
        if player_choice == "4":
            print("Thanks for playing. Goodbye!")
            break

        if player_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        player_choice = choices[int(player_choice) - 1]
        computer_choice = random.choice(choices)

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
            draws += 1
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
            rounds_won += 1
        else:
            print("Computer wins!")
            computer_rounds_won += 1
        print("  ")
        print("Score:")
        print("You:", rounds_won)
        print("Computer:", computer_rounds_won)
        print("Draws:", draws)
        print()

play_game()