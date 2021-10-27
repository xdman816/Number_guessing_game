"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random as r 
import statistics as stats

saved_attempt_list = []

def guessing_game():

  answer = r.randint(1, 100)
  attempt_no = 1
  attempt_list = []
  while True: 
      try:
          current_guess = int(input("Guess a number: "))
          if current_guess < 1 or current_guess > 100: 
            print("That guess is out of the range! Pick a number between 1 and 100")
            continue
          elif current_guess == answer:
            saved_attempt_list.append(len(attempt_list))
            break
          elif current_guess > answer:
            print("Too high! Try again")
            attempt_no += 1
            attempt_list.append(attempt_no)
            continue
          elif current_guess < answer:
            print("Too low! Try again")
            attempt_no += 1
            attempt_list.append(attempt_no)
            continue 
      except ValueError:
          print("That is not a valid number. Please pick a number between 1 and 100")
          continue   


  print(f"""You got it! The number was {answer}.

                =====>STATS<======

        Number of guesses: {len(attempt_list)}
        Average number of guesses: {stats.mean(saved_attempt_list)}
        50th percentile of guesses: {stats.median(saved_attempt_list)}
        Most common number of guesses: {stats.mode(saved_attempt_list)}
        All-time high score: {min(saved_attempt_list)} guesses
        """)


def start_game():

    print("Hello, and welcome to the Number Guessing Game!")
    player_name = input("What is your name? ")
    print(f"Hi {player_name}! The rules of this game are simple: we have a number in mind between 1 and 100, and you have to guess what it is!")
    
    while True:
        guessing_game()
        restart_game = input("Would you like to play again? Y/N   ")
        if restart_game.lower() == "n":
            print("Thanks for playing!")
            break
        elif restart_game.lower() == "y":
            print("Great! The game has reset with a new number \n")
            continue
      




start_game()

          


  
"""Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
#start_game()