import random

low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True

print("--- Number Guessing Game ---")
print(f"Select a Number Between {low_num} and {high_num}")

while is_running:
    guess = input("Enter Your Guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low_num or guess > high_num:
            print("That Number is Out of Range")
            print(f"Please Select a Number Between {low_num} and {high_num}")
        elif guess < answer:
             print("Too low! Try again!")
        elif guess > answer:
             print("Too high! Try again!")
        else:
            print()
            print(f"CORRECT! the answer was {answer}")
            print(f"Number of guess: {guesses}\n")

    else:
        print("Please Input a digit Number !!\n")    
