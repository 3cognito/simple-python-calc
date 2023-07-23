# Rock paper sciccors
import random


def get_player_choice() -> str:
    while True:
        print("Enter your choice: rock, paper, or sci - (sci represents scissors)")
        choice = input().lower()
        if choice in {"rock", "paper", "sci"}:
            return choice
        print("Invalid choice. Please try again.")


def get_computer_choice() -> str:
    return random.choice(["rock", "paper", "sci"])


def determine_winner(player_choice: str, computer_choice: str) -> str:
    if player_choice == computer_choice:
        return "It's a tie!"
    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    return "Computer wins!"


def play_game():
    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break


play_game()
