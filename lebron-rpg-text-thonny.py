#  Life of LeBron Simulator 

print("Life of LeBron Simulator\n")

# Ask for name and greet player
name = input("Tell me your name, bum: ").strip().lower()
print(f"\nWho would name their kid {name}? Doesn't matter — you're LeBron now.\n")

goat_meter = 100

# ● DECISION 1
decision1 = input("Do you get out of bed or go back to sleep? (get out/sleep): ").strip().lower()
if decision1 == "sleep":
    goat_meter -= 50
    print("\nYou fall asleep and wake up in your normal body. Boring loser.")
    print(f"GOAT Meter: {goat_meter}%")
else:
    goat_meter += 5
    print("\nYou get up and see Savannah James lying next to you.")
    print(f"GOAT Meter: {goat_meter}%")

    # ● DECISION 2
    decision2 = input("Do you head downstairs or go to the bathroom? (downstairs/bathroom): ").strip().lower()
    if decision2 == "bathroom":
        goat_meter -= 25
        print("\nYou slip on a wet towel, hit your head, and it's game over.")
        print(f"GOAT Meter: {goat_meter}%")
    else:
        goat_meter += 5
        print("\nYou go downstairs and see Bryce eating cereal.")
        print("Your NBA game vs. the Warriors starts in 30 minutes.")
        print(f"GOAT Meter: {goat_meter}%")

        # ● DECISION 3
        decision3 = input("Do you go to your game or stay home? (game/home): ").strip().lower()
        if decision3 == "home":
            goat_meter -= 50
            print("\nYou stay home, eat cereal, and miss the game. Trash decision.")
            print(f"GOAT Meter: {goat_meter}%")
        else:
            goat_meter += 10
            print("\nYou drive to Crypto Arena and make it on time.")
            print(f"GOAT Meter: {goat_meter}%")

            # ● DECISION 4
            decision4 = input("Do you head to the court or watch TikTok? (court/tiktok): ").strip().lower()
            if decision4 == "tiktok":
                goat_meter -= 50
                print("\nYou doom scroll for an hour and miss the game.")
                print("You might as well play Candy Crush.")
                print(f"GOAT Meter: {goat_meter}%")
            else:
                goat_meter += 10
                print("\nFans and teammates welcome you onto the court for tip-off.")
                print("Final quarter. 10 seconds left. Lakers 102 - Warriors 104.")
                print("Luka passes the ball to you.")
                print(f"GOAT Meter: {goat_meter}%")

                # ● DECISION 5 (path A)
                decision5 = input("Do you go for a three-pointer or a dunk? (three/dunk): ").strip().lower()
                if decision5 == "three":
                    goat_meter += 20
                    print("\nYou sink a beautiful three! Lakers win 105 - 104!")
                    print("Standing ovation. LeBron would be proud.")
                    print(f"GOAT Meter: {goat_meter}%")
                elif decision5 == "dunk":
                    goat_meter += 10
                    print("\nYou slam it to tie the game 104 - 104.")
                    print("But Curry hits a three in OT. You lose.")
                    print(f"GOAT Meter: {goat_meter}%")
