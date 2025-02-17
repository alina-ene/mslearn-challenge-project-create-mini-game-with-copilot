import random

# write 'hello world' to the console
print('hello world')
# write a Rock - Paper - Scissors python game which should fulfill the following requirements:
# 1. The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# 2. At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent
# 3. By the end of each round, the player can choose whether to play again.
# 4. Display the player's score at the end of the game.
# 5. Display the player's score at the end of the game.
# 6. The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def main():
    score = {'win': 0, 'lose': 0, 'tie': 0}
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)
        score[result] += 1

        print(f"You {result} this round!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Final score: Wins: {score['win']}, Losses: {score['lose']}, Ties: {score['tie']}")

if __name__ == "__main__":
    main()
