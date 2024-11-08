from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
#function to check users guess against  actual answer
def check_answer(user_guess, actual_answer, turns):
    """Check answer against guess, return the number of turns remaining """
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")

#function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty . Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    #choosing a random number between 1 and 100
    print("Welcome to Number Guessing Game!")
    print("I'a Thinking of a number between 1 and 100")
    answer = randint(1,100)
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    #Repeat the guessing functionality
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out, you lose!")
            return
        elif guess != answer:
            print("Guess Again!")


game()





