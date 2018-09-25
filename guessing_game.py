"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
  #1. Display an intro/welcome message to the player.
  print("""
        Welcome to the Number Guessing Game!
        ____________________________________

        You will be asked to choose a number from 1 - 100.
        You will want to guess the number correctly as quickly as possible to get a high score.
        (Don't worry, we will give you some hints)
        Like golf, the lower the number of guesses the better your score is!
        """)
  #2. Store a random number as the answer/solution.
  random_number = random.randint(1, 100)
  #variable setup
  playing = True
  retry = False
  guess_number = 1
  #3. Continuously prompt the player for a guess.
  while playing:
    guess_input = input('Your guess #{}: '.format(guess_number))
    try:
      guess_input = int(guess_input)
    except ValueError:
      print('You must input a number when guessing. Try again.')
    else:
      #EC: If the guess is out of the number range - tell use to try again
      if guess_input > 100 or guess_input < 1:
        print('Please choose a number from 1 - 100. Try again.')
      #a. If the guess greater than the solution, display to the player "It's lower".
      elif guess_input > random_number:
        print("It's lower.")
        guess_number += 1
      #b. If the guess is less than the solution, display to the player "It's higher".
      elif guess_input < random_number:
        print("It's higher.")
        guess_number += 1
      #4. Once the guess is correct, inform the user they "Got it"
      elif guess_input == random_number:
        print('You got it! It was {}!'.format(random_number))
        #and show how many attempts it took them to get the correct number.
        print('It took you {} tries to guess the number.'.format(guess_number))
        #EC: set current high score
        #if this is not the first attempt then check against the high score
        if retry:
          if guess_number < high_score:
            high_score = guess_number
            print('You got a new high score! High Score: {}'.format(high_score))
          else:
            print("You didn't beat the high score. Better luck next time!")
        #if this is the first attempt then initial score is the current high score
        else:
          high_score = guess_number
        #EC: ask the user if they would like to play again
        play_again = input('Would you like to play again? Y/N ')
        if play_again.upper() == 'Y':
          #EC: display current high score if playing again
          print("""
        Here we go again!
        The current high score to beat is {} guesses!
                """.format(high_score))
          #get a new random number
          random_number = random.randint(1, 100)
          #reset the guess_number
          guess_number = 1
          retry = True
        #5. Let the player know the game is ending, or something that indicates the game is over.
        else:
          print('Thanks for playing!')
          playing = False





if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
