import random

#player's name input
name = input("How should I address you?")
print( "Hello " + name +"!" + " Welcome to the Rock, Paper, Scissors Game!")

#list of selection for the computer
random_selection = ["rock", "paper", "scissors"]
win_count = 0
loss_count = 0
tie_count = 0

while True:
    #get the player's choice
    player_decision = input ("Please choose 'rock', 'paper', or 'scissors' (enter 'quit' to exit): ").lower().strip()
    player_decision = "".join(player_decision.split())

    if player_decision == "quit":
        break

    #get the computer's choice
    computer_pick = random.choice(random_selection)
    print("\nThe computer chose " + computer_pick + " and you chose " + player_decision)

    #determine the winner
    if player_decision == computer_pick:
        print("It's a tie! " + "You are two peas in a pod!\n")
        tie_count += 1
    elif (player_decision == "rock" and computer_pick == "scissors") or \
         (player_decision == "scissors" and computer_pick == "paper") or \
         (player_decision == "paper" and computer_pick == "rock"):
        print("Boom! Congrats, " + name + "! "
              "\n You won & you are smarter than computer!\n")
        win_count += 1
    else:
        print("Ouch! You lost. Better luck next time!")
        loss_count += 1


print(f"Your current scorecard: | {str(win_count)} + Win | + {str(loss_count)} +  Loss |  + {str(tie_count)}+ Tie | \n")

print("Thanks for playing, " + name + "! You are a true Ranger of Rock, Paper, Scissors Game!")


