import random

actions = ['rock', 'paper', 'scissors']

while True:
    user_choice = input('Enter your choice (rock, paper or scissors): ')
    user_count = 0
    computer_count = 0

    program_choice = random.choice(actions)

    print(f"Your choice {user_choice}, computer choice {program_choice}\n")

    if user_choice == program_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
        user_count = user_count+1
        computer_count = computer_count+1
    elif user_choice == "rock":
        if program_choice == "scissors":
            print("You win! because Rock smashes scissors.")
            user_count = user_count+1
        else:
            print("You lose :( Paper covers rock!")
            computer_count = computer_count+1
    elif user_choice == "paper":
        if program_choice == "rock":
            print("You win! because Paper covers rock.")
            user_count = user_count+1
        else:
            print("You lose :( Scissors cuts paper!")
            computer_count = computer_count+1
    elif user_choice == "scissors":
        if program_choice == "paper":
            print("You win! because Scissors cuts paper.")
            user_count = user_count+1
        else:
            print("You lose :( Rock smashes scissors!")
            computer_count = computer_count+1
    if user_count == computer_count :
            print(" Final Match Draw")
            print(" Computer Score",computer_count)
            print(" User Score ", user_count)
    elif user_count > computer_count :
            print(" User Win")
            print(" User Score", user_count)
            print(" Computer Score",computer_count)
    else :
            print(" Computer Win ")
            print(" Computer Score ",computer_count)
            print(" User Score ", user_count)
            
    play_again = input('Play again? (y/n)')
    if (play_again.lower() == 'n'):
        break
