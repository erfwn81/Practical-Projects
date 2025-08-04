#DICE_ROLL_GAME_GAMBLE

import random

def check_for_win(player_number, winning_number):
    """Check how much player wins based on matching digits"""
    win_rate = 0
    
    if player_number == winning_number:  # All 8 digits match
        win_rate = 2.0
        print("JACKPOT! All 8 digits match! You win 2x your deposit!")
    elif player_number[0:6] == winning_number[0:6]:  # First 6 match
        win_rate = 1.5
        print("Great! First 6 digits match! You won 1.5x your deposit!")
    elif player_number[0:4] == winning_number[0:4]:  # First 4 match
        win_rate = 1.2
        print("Good! First 4 digits match! You won 1.2x your deposit!")
    else:
        win_rate = 0
        print(" No matches. You lose this round.")
    
    return win_rate

def calculate_payout(win_rate, deposit):
    """Calculate final payout amount"""
    if win_rate > 0:
        payout = int(win_rate * deposit)
        profit = payout - deposit
        print(f"Your payout is : ${payout} (profit: ${profit})")
    else:
        payout = 0
        print(f"You lost your deposit of ${deposit}")
    
    return payout

def generate_wining_number():
    wining_num = ""
    for i in range(8):
        digit = random.randint(1,6)
        wining_num += str(digit)
    return wining_num

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2

def create_player_pattern():
    # Roll dice 4 times and create 8-digit pattern to match
    combination_number = ""
    
    for j in range(4):
        dice1, dice2 = roll_dice()
        print(f"🎲 Roll {j+1}: {dice1} and {dice2}")
        pattern = str(dice1) + str(dice2)
        combination_number += pattern
    
    return combination_number

# Generate winning number once
winning_number = generate_wining_number()
print("The winning number is:", winning_number)
print("=" * 50)

# Game loop
while True:
    try:
        # Get deposit amount
        deposit = int(input("💵 How much money are you depositing? $"))
        if deposit <= 0:
            print("❌ Deposit must be positive!")
            continue
            
    except ValueError:
        print("❌ Please enter a valid number!")
        continue
    
    choice = input("🎲 Do you want to roll dice? (y/n): ").lower().strip()
    
    if choice == "y":
        # Create player's 8-digit number
        player_number = create_player_pattern()
        
        print(f"\n RESULTS:")
        print(f" Winning number: {winning_number}")
        print(f"Your number:    {player_number}")
        print("=" * 30)
        
        # Check for win and calculate payout
        win_multiplier = check_for_win(player_number, winning_number)
        final_payout = calculate_payout(win_multiplier, deposit)
        
        print("=" * 30)
        
    elif choice == "n":
        print("Thanks for playing! Come back anytime!")
        break
        
    else:
        print(" Invalid input! Please enter 'y' or 'n'")