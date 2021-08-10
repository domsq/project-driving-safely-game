import time  # Module required to add a pause as needed

invalid_choice = ("\nNot a valid choice, please try again")


def text_input():
    """
    Function to accept input when user needs to make a choice
    """
    choice = input("Please choose an option:- \n")
    choice_lc = choice.lower()

    return choice_lc


def game_start():
    """
    Function to control start of game and display opening messages
    """
    print("Welcome to Driving Safely. The aim is to get to your destination"
          " without incident. "
          "\nYou’ll be presented with scenarios along the way, choose wisely"
          " as the wrong choice could end badly. \nEnjoy and have fun!\n")
    time.sleep(1)
    name = input("Please enter your name:- \n")
    time.sleep(1)
    print(f"\nWelcome {name}\n"
          "\nYou are going on holiday to your favourite seaside resort and "
          "have been looking forward to the break for the last few months."
          "\nYour car is packed up and you are ready to start your journey.")
    time.sleep(1)
    scenario_one()


def scenario_one():
    """
    Function for controlling scenario one
    """
    print("\nYou start the drive to your holiday accommodation and "
          "after driving for a few miles "
          "you encounter some slow traffic. "
          "\nThe driver behind you seems to be following a bit too "
          "closely, what should you do?\n"
          "\nA: Slow down gradually, building more of a gap "
          "between you and the car in front\n"
          "\nB: Move over towards a position a bit left "
          "of the centre line of the road\n")
    selection = text_input()
    if selection == "a":
        print("Well done, this is the safe way to handle the situation.")
    elif selection == "b":
        print("Sorry, this is the wrong answer.  The driver behind attempts to"
              " undertake you and collides with you in the process."
              "\nRule #151 of the Highway Code (pg. 50, 2015 Edition) states: "
              "Never get so close to the vehicle in front "
              "that you cannot stop safely.")
    else:
        print(invalid_choice)
        time.sleep(1)
        scenario_one()


game_start()
