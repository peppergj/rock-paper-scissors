import random
user_action = input("rock, paper, or scissors? ")

while True:
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {computer_action}")

    if user_action == computer_action:
        print(f"we both selected {user_action}. its a tie... this time.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock beats scissors mate.... you win.")
        else:
            print("paper wraps rock. YOU LOOOOSE.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper wraps around rock. you win...")
        else:
            print("scissors cuts paper. you lose ONCE AGAIN")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper!!!!!!! you WIN")
        else:
            print("rock breaks scissors. you LOSEEEE HAHA")

    play_again = input("would you like to play again?")
    if play_again.lower() != "y":
        break