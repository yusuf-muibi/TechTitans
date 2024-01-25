"""A game to guess the secret code"""

import random
import time

secret_code = random.randint(1, 9)


while True:
        user_input = int(input("Kindly type in your choice:"))

        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Kindly enter a number")
            continue
        
        bot_choice = random.randint(1, 9)

        print("Bot's choice is %s" % (bot_choice))
        print("Your choice is %s" % (user_input))
        
        if user_input == secret_code:
            print("Congratulations, you won!")
            print("The Secret Code is %s" % (secret_code))
            break
        elif bot_choice == secret_code:
            print("Bot Won")
            break
        else:
            print("You lost. Try again.")