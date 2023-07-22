from random import randint
from typing import Union

MAX_GUESSES = 5
VALID_RANGE = range(1, 11)


def get_user_guess() -> Union[int, None]:
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
            if user_guess in VALID_RANGE:
                return user_guess
            else:
                print("That is not a number between 1 and 10, try again!")
        except ValueError:
            print("That's not a number! Try again!")


def check_guess(user_guess: int, random_guess: int) -> bool:
    if user_guess == random_guess:
        print("You guessed it! You won🥳🥳🥳🥳!")
        return True
    elif user_guess < random_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    return False


def play_game():
    random_guess = randint(1, 10)
    print("Welcome to the Number Guessing Game!")
    print(
        f"I am thinking of a number between 1 and 10. You have {MAX_GUESSES} attempts to guess the number."
    )

    for attempt in range(MAX_GUESSES):
        user_guess = get_user_guess()
        if check_guess(user_guess, random_guess):  # type: ignore
            return True
        remaining_attempts = MAX_GUESSES - attempt - 1  # attempt starts from 0
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts left.")
    print(
        f"Sorry, you've reached the maximum attempts. The correct number was {random_guess}."
    )
    return False


def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break
    print("Thank you for playing the Number Guessing Game!")


main()
# def guess() -> None:
#     max_guesses: int = 10
#     attempts: int = 0
#     random_guess: int = randint(1, 10)

#     print("Welcome to the Number Guessing Game!")
#     print(
#         f"I am thinking of a number between 1 and 10. You have {max_guesses} attempts to guess the number."
#     )
#     while attempts < max_guesses:
#         try:
#             user_guess = int(input("Guess a number between 1 and 10: "))
#             attempts += 1

#             if 1 <= user_guess <= 10:
#                 pass
#             else:
#                 print(
#                     f"That is not a number between 1 and 10, try again !. You have {max_guesses - attempts} guesses left!"
#                 )
#                 continue

#             if user_guess == random_guess:
#                 print("You guessed it! You won🥳🥳🥳🥳!")
#                 choice: str = input("Do you want to play again? (y/n): ")
#                 if choice != "y":
#                     return
#                 else:
#                     guess()

#             elif user_guess < random_guess:
#                 print(
#                     f"Too low! Try again. You have {max_guesses - attempts} guesses left!"
#                 )
#             else:
#                 print(
#                     f"Too high! Try again. You have {max_guesses - attempts} guesses left!"
#                 )

#         except ValueError:
#             print("That's not a number! Try again!")
#             continue
#     if attempts == max_guesses:
#         print(
#             f"Sorry, you've reached the maximum attempts. The correct number was {random_guess}."
#         )

#     print(
#         'If you will like to play again, input "y" to play again or any other key to exit.'
#     )
#     choice: str = input("Do you want to play again? (y/n): ")
#     if choice != "y":
#         return
#     else:
#         guess()
#     print("Thank you for playing the Number Guessing Game!")


# guess()
