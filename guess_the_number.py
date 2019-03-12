
import random

print("Hi.  Welcome to Guess the Number.")

max_guesses = 5

min = 1
max = 20
print("I'm thinking of a number from %d to %d" % (min, max))
the_number = random.randint(min, max)

guess_count = 0

print("Take a guess:")
while True:
    guess_string = input()
    guess_count = guess_count + 1
    guess = int(guess_string)
    if guess == the_number:
        print("You guessed the number in %d guesses." % guess_count)
        break
    if guess < the_number:
        print("Your guess, %d, is too low.  Guess again:" % guess)
    elif guess > the_number:
        print("Your guess, %d, is too high.  Guess again:" % guess)


