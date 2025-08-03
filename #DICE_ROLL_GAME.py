#DICE_ROLL_GAME
# getting input to start or

import random

def check_for_win():
    if 

def calculator_payout():

    

def generate_wining_number():
    wining_num = ""
    for i in range(8):
        digit = random.randint(1,6)
        wining_num += str(digit)
    return wining_num
# print(generate_wining_number)

def roll_dice():
    dice1 =  random.randint(1,6)
    dice2 =  random.randint(1,6)
    return dice1, dice2

def pattern():
    dices_pattern = str(dice1) + str(dice2)
    return dices_pattern 

wining_number = generate_wining_number()
print("The winning number is : ", wining_number )
# seprator
print("=" * 40)

while True:
    choice = input("Do you want to roll dice? y/n ").lower()
    if choice == "y" :
        combination_number_dice = ""
    
        for j in range(4):
            dice1, dice2 = roll_dice()
            print(f"🎲 Dice Results: {dice1} and {dice2}")
            player_pattern = pattern()
            combination_number_dice += str(player_pattern)

        print("your result number is = " , combination_number_dice)
        print(" the winin number is " ,  wining_number)

    elif choice == "n":
        print("ok lmk when tyou want to roll the dices again thank you for playing 👋 n")
    else:
        print("invalid input try again with y/n")
        
