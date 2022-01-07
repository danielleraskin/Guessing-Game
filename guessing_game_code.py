#Danielle Raskin 20936398

import random

def guessing_game():

    answer = random.randint(0,100)
    while True:
        guess = input('Guess a number between 0 and 100: ')

        try:
            guess = int(guess)
        except:
            print("Guess must be a number")
            continue

        if guess < 0 or guess > 100:
            print("Guess between 0 and 100")
        elif guess == answer:
            print("You guessed right!")
            return 
        elif guess > answer:
            print('Too high')
        else:
            print ('Too low')


guessing_game()




