import time  # Module required to add a pause as needed
# Scenario content moved to config.py file as discussed with mentor
from config import SCENARIOS
# Moved ascii art and message text to constants.py,
# as discussed with mentor
from constants import (GAME_LOGO, WELCOME_MESSAGE, INTRO_IMAGE,
                       INTRO_TEXT, WELL_DONE, GAME_OVER)

invalid_choice = ("\nNot a valid choice, please try again\n")
current_scenario_index = -1
name = None


def enter_name():
    """
    Function to accept and validate name input
    """
    name_entry = input("Please enter your name:- (Min 3 characters)\n")
    if len(name_entry) < 3:
        return enter_name()
    else:
        return name_entry


# Amended following discussion with mentor
def text_input():
    """
    Function to accept input when user needs to make a choice
    """
    choice = input("Please choose an option:- (A/B)\n")
    choice_lc = choice.lower()
    if choice_lc not in ['a', 'b']:
        print(invalid_choice)
        return text_input()

    return choice_lc


def game_start():
    """
    Function to control start of game and display opening messages
    """
    print(GAME_LOGO)
    print(WELCOME_MESSAGE)
    time.sleep(1)
    print(INTRO_IMAGE)
    time.sleep(1)
    global name
    name = enter_name()
    time.sleep(1)
    print(f"\nWelcome {name}\n")
    print(INTRO_TEXT)
    time.sleep(1)
    load_next_scenario()


# Function to load scenarios as discussed with mentor
def load_next_scenario():
    """
    Function to load next scenario from list "SCENARIOS".
    Will also finish game if all scenarios completed.
    """
    print("\n+++++++++++++++++++++++++++++++++++++"
          "+++++++++++++++++++++++++++++++++++++")
    global current_scenario_index
    current_scenario_index = current_scenario_index + 1
    if current_scenario_index == len(SCENARIOS):
        print(WELL_DONE)
        play_again()
    else:
        scenario = SCENARIOS[current_scenario_index]
        show_scenario(scenario)


# Function to display current scenario, as discussed with mentor
def show_scenario(scenario):
    """
    Function for displaying of current scenario
    """
    print(scenario["question"])
    selection = text_input()
    if selection == scenario["correct_choice"]:
        print(scenario["correct_answer"])
        time.sleep(3)
        load_next_scenario()
    else:
        print(scenario["wrong_answer"])
        time.sleep(3)
        game_over()


def game_over():
    """
    Displays game over message and asks whether user would like to try again
    """
    print(GAME_OVER)
    time.sleep(1)
    play_again()


# Added function as a way to restart game upon game over or completion
# following discussion with mentor
def play_again():
    """
    Asks whether user would like to play again and restarts game if required,
    upon game over or game completion
    """
    continue_choice = input(f"Want to play again {name}? Y/N\n")
    if continue_choice in ["y", "Y"]:
        global current_scenario_index
        current_scenario_index = -1
        game_start()
    elif continue_choice in ["n", "N"]:
        print(f"\nNo worries {name}, see you later!")
    else:
        print(invalid_choice)
        return play_again()


game_start()
