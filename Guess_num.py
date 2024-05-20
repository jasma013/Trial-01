import random

# Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)
max_attempts = 3

def welcome_message():
    """
    Prints the welcome message and the number of attempts the player has.
    """
    print("\nWelcome to the Number Guessing Game.")
    print(f"You have {max_attempts} attempts to guess the correct number.")

def guess_recursive(attempts_left):
    """
    Recursively handles the guessing process until the player either guesses correctly or runs out of attempts.
    
    :param attempts_left: int, the number of attempts left for the player
    """
    try:
        guess = int(input("\nGuess the number (between 1 to 10): "))
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 10.")
        return guess_recursive(attempts_left)
    
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        return guess_recursive(attempts_left)
    
    if guess == secret_number:
        print("Congratulations! You have guessed the correct number!")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left - 1}")
        if attempts_left > 1:
            guess_recursive(attempts_left - 1)
        else:
            print(f"\nSorry, you could not guess the number. The correct number was {secret_number}.")

# Main code calling the function
welcome_message()
guess_recursive(max_attempts)

# Using id() to get memory addresses
print(f"Memory address of Secret Number {secret_number} is: {id(secret_number)}")
