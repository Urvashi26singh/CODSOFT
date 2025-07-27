import random
def get_user_choice():
    choice = input("Choose Rock,Paper, or Scissors: ").lower()
    while choice not in ["rock","paper","scissors"]:
        print("INVALID INPUT.")
        choice = input("choose Rock ,Paper ,or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def determine_winner(user , computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer =="scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
    
def play_game():
    user_score = 0
    computer_score = 0

    print("\nWELCOME TO ROCK, PAPER, SCISSORS GAME!!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n You chose: {user_choice.capitalize()}")
        print(f"Computer chose:{computer_choice.capitalize()}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
                print("It's a tie!")
        elif winner == "user":
                print("You win this round!")
                user_score += 1
        else:
                print("Computer wins this round!")
                computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\n Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n Thanks for playing!")
            break

#start the game
play_game()