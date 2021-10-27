import random as rand 
import statistics as stats

saved_attempt_list = []

def guessing_game():

  answer = rand.randint(1, 100)
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
          print("That is not a valid number! Please pick a number between 1 and 100.")
          continue   

  print(f"""You got it! The number was {answer}.

                =====>STATS<======

        Number of guesses: {len(attempt_list)}
        Average number of guesses: {stats.mean(saved_attempt_list)}
        50th percentile of guesses: {stats.median(saved_attempt_list)}
        Most common number of guesses: {stats.mode(saved_attempt_list)}
        All-time best score: {min(saved_attempt_list)} guesses
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

          


  
