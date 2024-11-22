import random

def guessing_game():
    """
    This function implements a number guessing game where the user has to guess a randomly generated number between 0 and 10.

    The function performs the following steps:
    1. Generates a random number between 0 and 10 (inclusive) that the user needs to guess.
    2. Continuously prompts the user to enter their guess.
    3. Compares the user's guess with the generated number and provides feedback:
       - If the guess is correct, it prints a congratulatory message and exits the loop.
       - If the guess is too low, it informs the user that their guess is too low.
       - If the guess is too high, it informs the user that their guess is too high.
    4. Repeats this process until the user correctly guesses the number.

    Example:
    -------
    If the generated number is 42 and the user guesses 35, the function will output:
    'Your guess of 35 is too low!'

    If the user then guesses 45, the function will output:
    'Your guess of 45 is too high!'

    When the user eventually guesses 42, the function will output:
    'Right! The answer is 42' and terminate.
    """    
    answer = random.randint(0, 10)  # Generate a random number between 0 and 10

    # Complete your code implementation here ... 
    import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Try to guess it.")
    while True:
        user_guess = input("Enter your guess: ")
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        user_guess = int(user_guess)
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

# Call the function to start the game
guessing_game()

    

# Test your code:
guessing_game()