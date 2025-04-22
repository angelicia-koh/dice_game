import random

def dice_game():

    while True:
        x = input("\nRoll the dice? (y/n):")

        if x.lower() != "y" and x.lower() != "n": #make it case-insensitive by using .lower()
            print("You have key in an invalid input")
            
        elif x.lower() == "n":
            print("Okay. Bye!")
            break

        else:
            rollingNUM1 = random.randrange(1,7)
            rollingNUM2 = random.randrange(1,7)
            print("You've rolled:", (rollingNUM1), "and", (rollingNUM2))

            while True:
                y = input("Want to play again? (y/n): ")

                if y.lower() != "y" and y.lower() != "n": #make it case-insensitive by using .lower()
                    print("You have key in an invalid input")

                elif y.lower() == "n":
                    print("Okay. Bye bye for real now!")
                    return # Exit the entire function/game
                else: 
                    print("Alright, lets roll!")
                    break # Break out of inner loop and restart outer loop


dice_game()