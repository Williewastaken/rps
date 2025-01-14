import random

choices = ["rock", "paper", "scissors"]

score : int = 0
computer_choice = None


error_codes = {
    "INVALID_COMPUTER_CHOICE": 101,
    "INVALID_PLAYER_CHOICE": 201,
    "INVALID_SCORE": 301,
    "UNKNOWN_EROR": 777
}



def check_score():
    if score < 0:
        print(f"An error occoured: code {error_codes['INVALID_SCORE']}")
        try: 
            score = 0
        except Exception as e:
            print(f"An error occurred: {e}, error_code: {error_codes['UNKNOWN_ERROR']}")

def initialize_game():
    global score
    global choices
    global computer_choice

# Add points to the score
def add_points(points: int):
    try:
        print("You win!")
        score += points
        check_score()
        print(f"Score: {score}")
    except Exception as e:
        print(f"An error occurred: {e}, error_code: {error_codes['UNKNOWN_ERROR']}")

# Remove points from the score
def remove_points(points: int):
    print("You lose!")
    if score > 0:
        score -= 1
        check_score()
        print(f"Score: {score}")
    else:
        score = 0
        check_score()
        print(f"Score: {score}")
    

def computer_choice():
    try:
        computer_choice = random.choice(choices)
        
    except Exception as e:
        print(f"An error occurred: {e}, error_code: {error_codes['INVALID_COMPUTER_CHOICE']}")
        computer_choice()

def player_choice():
    computer_choice()
     = print(input("Enter your choice: ")) # FIX ME
      # FIX ME
       # FIX ME
        # FIX ME
         # FIX ME
    if player_choice not in choices:
        print(f"An error occurred: code {error_codes['INVALID_PLAYER_CHOICE']}")
        player_choice()
    
    if computer_choice != None:
        if computer_choice == player_choice:
            print("It's a tie!")
            check_score()
            print(f"Score: {score}")
        
        elif computer_choice == "rock" and player_choice == "scissors":
            remove_points(1)
        
        elif computer_choice == "rock" and player_choice == "paper":
            add_points(1)
        
        elif computer_choice == "paper" and player_choice == "scissors":
            add_points(1)
          
    

player_choice()