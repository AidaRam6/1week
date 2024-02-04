import random

def guess_the_number():

  secret_number = random.randint(1, 20)

  name = input("Hello! What is your name? ")

  print(f"Well, {name}, I am thinking of a number between 1 and 20.")

  num_guesses = 0

  while True:
    num_guesses += 1
    guess = int(input("Take a guess: "))

    if guess == secret_number:
      print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
      break
    elif guess < secret_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")

guess_the_number()
