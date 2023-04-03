import random, sys

def get_random_number():
    return random.randint(0, 255)

def subtract_numbers(num1, num2):
    return num1 - num2

def play_game():
    correct_guesses = 0
    rounds = 0
    print("Welcome to Math Trainer! Press Q to quit!")
    
    while True:
        num1 = get_random_number()
        num2 = get_random_number()

        # Prevent subtracting a larger number from a smaller one.
        if num1 < num2:
            num1, num2 = num2, num1
        answer = subtract_numbers(num1, num2)
        guess = input(f"What is {num1} - {num2}? ")

        # Allow user to quit the program.
        if guess.lower() == "q":
            print()
            print("Thank you for playing.")
            sys.exit()

        # Input validation, user should only enter numbers.
        while True:
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
                # Ask for the answer to the same question agian.
                guess = input(f"What is {num1} - {num2}? ")

                # Allow user to quit even during input validation.
                if guess.lower() == "q":
                    print()
                    print("Thank you for playing.")
                    sys.exit()
                continue
            else:
                break
        
        if int(guess) == answer:
            correct_guesses += 1
            rounds += 1
            print(f"Correct! Score: {correct_guesses} out of {rounds}")
        else:
            rounds += 1
            print(f"Incorrect. The answer is {answer}.")
            print(f"Score: {correct_guesses} out of {rounds}")
        print()

play_game()