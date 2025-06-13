print("🏀 Life of LeBron Simulator\n")

# Intro
name = input("Tell me your name, bum: ").strip().lower()
print(f"\nWho would name their kid {name}? Doesn't matter — you're LeBron now.\n")

# GOAT Meter (just for flavor)
goat_meter = 100

# ● DECISION 1
choice1 = input("Do you get out of bed or go back to sleep? (get out/sleep): ").strip().lower()

if choice1 == "get out":
    goat_meter += 5
    print("\n✅ You get up. Savannah James is next to you.")
    print(f"GOAT Meter: {goat_meter}%")

    # ● DECISION 2
    choice2 = input("Do you go downstairs or go to the bathroom? (downstairs/bathroom): ").strip().lower()

    if choice2 == "downstairs":
        goat_meter += 5
        print("\n✅ You go downstairs. Bryce is eating cereal.")
        print("Your game vs. the Warriors is in 30 minutes.")
        print(f"GOAT Meter: {goat_meter}%")

        # ● DECISION 3
        choice3 = input("Do you head to the game or stay home? (game/home): ").strip().lower()

        if choice3 == "game":
            goat_meter += 10
            print("\n✅ You pull up to the arena on time.")
            print(f"GOAT Meter: {goat_meter}%")

            # ● DECISION 4
            choice4 = input("Do you go to the court or watch TikTok? (court/tiktok): ").strip().lower()

            if choice4 == "court":
                goat_meter += 10
                print("\n✅ You're on the court. Final quarter. 10 seconds left.")
                print("Luka passes you the ball. Time slows down...")
                print(f"GOAT Meter: {goat_meter}%")

                # ● DECISION 5 (final)
                choice5 = input("Do you shoot a three or go for the dunk? (three/dunk): ").strip().lower()

                if choice5 == "three":
                    goat_meter += 20
                    print("\n🎯 YOU NAIL THE THREE! Lakers win 105-104.")
                    print("LeBron nods in approval from the rafters.")
                    print(f"🏆 FINAL GOAT Meter: {goat_meter}%")
                    print("YOU WIN.")
                else:
                    print("\n💥 You dunk to tie the game.")
                    print("But Curry hits a three in OT. You lose.")
                    print("GAME OVER.")

            else:
                print("\n📱 You doomscroll TikTok and miss the game.")
                print("Adam Silver suspends you for 'goofy behavior.'")
                print("GAME OVER.")

        else:
            print("\n🥣 You stayed home and missed the game.")
            print("You get benched for the season.")
            print("GAME OVER.")

    else:
        print("\n🚿 You slipped on a towel in the bathroom.")
        print("Concussion. Season's over.")
        print("GAME OVER.")

else:
    print("\n😴 You stayed in bed and never became LeBron.")
    print("You wake up and you're just... you.")
    print("GAME OVER.")