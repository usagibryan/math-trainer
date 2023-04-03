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
        if num1 < num2:
            num1, num2 = num2, num1
        answer = subtract_numbers(num1, num2)
        guess = input(f"What is {num1} - {num2}? ")
        if guess.lower() == "q":
            print("Thank you for playing.")
            sys.exit()
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if int(guess) == answer:
            correct_guesses += 1
            rounds += 1
            print(f"Correct! Score: {correct_guesses} out of {rounds}")
        else:
            rounds += 1
            print(f"Incorrect. The answer is {answer}.")
        print()

play_game()