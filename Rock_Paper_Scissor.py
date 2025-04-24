#This program is created by Aniket Ullewar.
 
import random


emojis={'r':'🪨','p':'📃','s':'✂️'}
choices=['r','s','p']

while True:
    user_choice=(input("Rock, Paper or Scissors?(r/p/s):")).lower()
    machine_choice=random.choice(choices)

    if user_choice in choices:
        print(f"you chosen {emojis[user_choice]}")
        print(f"PC has chosen {emojis[machine_choice]}")
        if user_choice == machine_choice:
            print("Tie")
        elif (user_choice=="r" and machine_choice=="s")or(user_choice=="s" and machine_choice=="p")or(user_choice=="r" and machine_choice=="r"):
            print("You win")
        else:
            print("You lose")
    else:
        print("Invalid choice!")
    
    again=(input("Countinue? (y/n):")).lower()
    if again=="y":
        True
    elif again=="n":
        break
    else:
        print("invalid choice")
        break




