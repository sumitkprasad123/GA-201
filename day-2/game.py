import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the game result
def display_result(user_choice, computer_choice, winner):
    print(f"\nUser's choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("Congratulations! You win!")
    else:
        print("Computer wins!")

# Initialize the scores
user_score = 0
computer_score = 0
draws = 0

# Main game loop
while True:
    # Prompt user for choice
    user_choice = input("\nEnter your choice (rock, paper, scissors), or 'quit' to exit: ").lower()

    # Check if the user wants to quit
    if user_choice == "quit":
        print("\nFinal Score:")
        print(f"User wins: {user_score}")
        print(f"Computer wins: {computer_score}")
        print(f"Draws: {draws}")
        print("Thank you for playing! Goodbye!")
        break

    # Check if the user's choice is valid
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    winner = determine_winner(user_choice, computer_choice)

    # Update the scores
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    else:
        draws += 1

    # Display the result
    display_result(user_choice, computer_choice, winner)
