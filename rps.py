import random


name = input("What is your name?")
print( "Hello " + name +"!")

#list of choices for the computer
my_random_list = ["rock", "paper", "scissors"]
win_count = 0
loss_count = 0
tie_count = 0

while True:
    #get the player's choice
    player_choice = input ("Please choose 'rock', 'paper', or 'scissors' (enter 'quit' to exit): ").lower().strip()
    player_choice = "".join(player_choice.split())

    if player_choice == "quit":
        break

    #get the computer's choice
    computer_choice = random.choice(my_random_list)
    print("\nThe computer chose\t" + " " + computer_choice + " and you chose " + player_choice)

    #Determine the winner
