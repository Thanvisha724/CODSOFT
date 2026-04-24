import random
import time

def get_user_choice():
    """
    Get the user's choice: rock, paper, or scissors.
    Validates input and makes it case-insensitive.
    """
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """
    Randomly select the computer's choice.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on game rules.
    Returns 'win', 'lose', or 'draw'.
    """
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, computer_choice, result):
    """
    Display the choices and the result.
    """
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    if result == 'win':
        print("You win!")
    elif result == 'lose':
        print("You lose!")
    else:
        print("It's a draw!")

def main():
    """
    Main function to run the Rock Paper Scissors game.
    """
    user_score = 0
    computer_score = 0

    print("Welcome to Rock Paper Scissors!")

    while True:
        # Get user's choice
        user_choice = get_user_choice()

        # Simulate delay for computer choice
        print("Computer is choosing...")
        time.sleep(1)

        # Get computer's choice
        computer_choice = get_computer_choice()

        # Determine winner
        result = determine_winner(user_choice, computer_choice)

        # Update scores
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        # Display result
        display_result(user_choice, computer_choice, result)

        # Display current score
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing! Final Score - You: {user_score} | Computer: {computer_score}")
            break

# Run the main function
if __name__ == "__main__":
    main()