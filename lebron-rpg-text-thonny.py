# Text-Based RPG: Lebron Simulator
# Simulating the life of LeBron James using simple Python

print("Life of Lebron Simulator\n")

# Ask User for their name and greet them
name = input("Tell me your Name Bum: ").lower().strip()

print(f"\nWho would name their kid {name}? Doesn't matter you’re gonna be LeBron anyways.\n")


# ------------------------- Game Start -------------------------

# Initialize GOAT Meter (Starts at 100%)
goat_meter = 100


# You First Wake up

print("\nYou wake up in LeBron's bed. You seem to be trapped in his body.")
print("You forget everything about your past. What do you do?\n")


# DECISION 1: Get out of bed or sleep
decision1 = input("Do you get out of bed or go back to sleep? (get out/sleep) ").strip().lower()

if decision1 == "sleep":
    goat_meter -= 50  
    print("\nYou fall asleep and wake up in your normal body. Boring loser.\n")
    print(f"GOAT Meter: {goat_meter}%\n")
    exit()
elif decision1 == "get out":
    print("\nYou look around and see Savannah James lying next to you.\n")
    goat_meter += 5  
    print(f"GOAT Meter: {goat_meter}%\n")




# DECISION 2: Head downstairs or go to the bathroom
decision2 = input("Do you head downstairs or go to the bathroom? (downstairs/bathroom) ").strip().lower()

if decision2 == "bathroom":
    print("\nYou slip on a wet towel, fall on the hard tile floor, and crack your skull.")
    print("You're lowkey bad at making decisions.\n")
    goat_meter -= 25  
    print(f"GOAT Meter: {goat_meter}%\n")
    exit()
elif decision2 == "downstairs":
    print("\nYou head downstairs and see Bryce James eating cereal.")
    print("Your NBA game vs. the Warriors starts in 30 minutes.\n")
    goat_meter += 5  
    print(f"GOAT Meter: {goat_meter}%\n")




# DECISION 3: Go to game or stay home
decision3 = input("Do you go to your game or stay home? (game/home) ").strip().lower()

if decision3 == "home":
    print("\nYou finish your food but end up late and missing the game.")
    print("If your decisions in the game are this bad, I can’t imagine real life.\n")
    goat_meter -= 50  
    print(f"GOAT Meter: {goat_meter}%\n")
    exit()
elif decision3 == "game":
    print("\nYou head to your car and drive to Crypto Arena.")
    print("Thankfully, you arrive on time.\n")
    goat_meter += 10  
    print(f"GOAT Meter: {goat_meter}%\n")


 

# DECISION 4: Head to the court or watch TikTok
decision4 = input("Do you head to the court or watch TikTok in the locker room? (court/TikTok) ").strip().lower()

if decision4 == "tiktok":
    print("\nYou end up missing the game as you doom scroll for an hour.")
    print("Just go play Candy Crush at this point.\n")
    goat_meter -= 50  
    print(f"GOAT Meter: {goat_meter}%\n")
    exit()
elif decision4 == "court":
    print("\nFans and Players greet you as you make your way onto the court for tip-off.\n")
    goat_meter += 10  
    print(f"GOAT Meter: {goat_meter}%\n")


# Final Choice

# DECISION 5: Three-pointer or dunk
decision5 = input("Last quarter, 10 seconds left! Do you go for A three-pointer or a dunk? (three/dunk) ").strip().lower()

if decision5 == "three":
    print("\nYou hit a satisfying Three-pointer and win the game (105-104)!")
    print("Your teammates throw you up in the air.\n")
    goat_meter += 20  
    print(f"GOAT Meter: {goat_meter}%\n")
    print("You wake up in your sad old life, but at least you kept LeBron's legacy alive.\n")

elif decision5 == "dunk":
    print("\nYou make a poster dunk and tie the score (104-104).")
    print("But you end up losing in overtime from a three by Curry.\n")
    goat_meter += 10  
    print(f"GOAT Meter: {goat_meter}%\n")


#  Game End 

print("\nGame over. Thanks for playing!\n")

