import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

#######    Your code here    #######
# Variables
score = 100
play_cost = 5
payout = 20

print("Welcome to the Simple Slot Machine!")
print(f"You start with: {score}")

while score >= play_cost:
    print(f"\nYour score: {score}")

    # Keep asking until a valid input is given
    while True:
        spin = input("Do you want to spin? (yes/no): ").strip().lower()
        if spin in ["yes", "no"]:
            break
        print("Please type 'yes' or 'no'.")

    if spin == "no":
        print(f"Thanks for playing! Your final score: {score}")
        break

    # Pay for playing
    score -= play_cost

    # Roll 9 numbers
    slots = [randint(0, 9) for _ in range(9)]

    # Print them in a 3x3 layout
    print(f"|{slots[0]}|{slots[1]}|{slots[2]}|")
    print(f"|{slots[3]}|{slots[4]}|{slots[5]}|")
    print(f"|{slots[6]}|{slots[7]}|{slots[8]}|")

    # Check wins
    win = 0

    # Horizontal wins
    if slots[0] == slots[1] == slots[2]:
        win += payout
    if slots[3] == slots[4] == slots[5]:
        win += payout
    if slots[6] == slots[7] == slots[8]:
        win += payout

    # Diagonal wins
    if slots[0] == slots[4] == slots[8]:
        win += payout
    if slots[6] == slots[4] == slots[2]:
        win += payout

    if win > 0:
        print(f"You WIN! +{win}")
        score += win
    else:
        print("No win this time.")

    sleep(1)  # Slow down output

if score < play_cost:
    print(f"You're out of points! Final score: {score}")
#my friend helped with this quite a bit
