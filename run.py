import time  # Module required to add a pause as needed


def game_start():
    """
    Function to control start of game and display opening messages
    """
    print("Welcome to Driving Safely. The aim is to get to your destination"
          " without incident. "
          "\nYou’ll be presented with scenarios along the way, choose wisely"
          " as the wrong choice could end badly. \nEnjoy and have fun!\n")
    time.sleep(1)
    name = input("Please enter your name:- ")
    time.sleep(1)
    print(f"\nWelcome {name}\n"
          "\nYou are going on holiday to your favourite seaside resort and "
          "have been looking forward to the break for the last few months."
          "\nYour car is packed up and you are ready to start your journey.")


game_start()
