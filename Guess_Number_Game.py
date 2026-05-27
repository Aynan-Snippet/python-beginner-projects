import random

secret_number = random.randint(1, 10)
chances = 3

print("Guess The Number Between 1-10")

while chances > 0:
    guess = int(input("Enter Your Guess: "))

    if guess == secret_number:
        print("You guessed correct, You won!")
        break

    elif guess < secret_number:
        print("Too low")

    else:
        print("Too high")

    chances = chances - 1
    print("Remaining chances:", chances)

    if chances == 0:
        print("You lost!")
        print("The Number Was:", secret_number)