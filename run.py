import time  # Module required to add a pause as needed
# Scenario content moved to config.py file as discussed with mentor
from config import SCENARIOS

invalid_choice = ("\nNot a valid choice, please try again\n")
current_scenario_index = -1


# Amended following discussion with mentor
def text_input():
    """
    Function to accept input when user needs to make a choice
    """
    choice = input("Please choose an option:- \n")
    choice_lc = choice.lower()
    if choice_lc not in ['a', 'b']:
        print(invalid_choice)
        return text_input()

    return choice_lc


def game_start():
    """
    Function to control start of game and display opening messages
    """
    print("███████████████████████████████████████▀███\n"
          "█▄─▄▄▀█▄─▄▄▀█▄─▄█▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄███\n"
          "██─██─██─▄─▄██─███▄▀▄███─███─█▄▀─██─██▄─███\n"
          "▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀\n"
          "█████████████████████████████████████\n"
          "█─▄▄▄▄██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄███▄─█─▄█\n"
          "█▄▄▄▄─██─▀─███─▄████─▄█▀██─██▀██▄─▄██\n"
          "▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀\n")
    print("Welcome to Driving Safely. The aim is to get to your "
          "destination\nwithout incident. "
          "You’ll be presented with scenarios along the way\nso choose wisely"
          " as the wrong choice could end badly.\n\nEnjoy and have fun!\n")
    time.sleep(1)
    print("                                                            \n"
          "                      ,,,,,,,,,,,,,,,,,                     \n"
          "                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,                \n"
          "             ,,,,,,,,,                 ,,,,,,,,,            \n"
          "           ,,,,,,,                         ,,,,,,,          \n"
          "         ,,,,,,                               ,,,,,,        \n"
          "       .,,,,,,                                  ,,,,,,      \n"
          "      .......                                   .,,,,,,     \n"
          "     .....                                         .....    \n"
          "     #*&               @@@&@@@&@@@&@@@               &*#    \n"
          "    ......       .@@@@@@@&.........##@@@@@&..      ......   \n"
          "    .............@@@@@@##..       ..#%@@@@@&.............   \n"
          "    ............*@@@@@@##..      ...#%@@@@&&.............   \n"
          "    ........         ,@@##........%&&@,           ......    \n"
          "     .....              *@@@@@#@@%@@               .....    \n"
          "     .....                @@@@@@@@@                ....     \n"
          "       .....              &&&&&&@&               .....      \n"
          "         ....,             &@&&&@&             .....        \n"
          "          ...*%...        ........         ...%*..          \n"
          "              ........   ..........    ........             \n"
          "                 ...........................                \n"
          "                                                            \n")
    time.sleep(1)
    name = input("Please enter your name:- \n")
    time.sleep(1)
    print(f"\nWelcome {name}\n"
          "\nYou are going on holiday to your favourite seaside resort and "
          "have \nbeen looking forward to the break for the last few months."
          "\nYour car is packed up and you are ready to start your journey.")
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
        print("\n██     ██ ███████ ██      ██          \n"
              "██     ██ ██      ██      ██          \n"
              "██  █  ██ █████   ██      ██          \n"
              "██ ███ ██ ██      ██      ██          \n"
              " ███ ███  ███████ ███████ ███████     \n"
              "\n"
              "\n"
              "██████   ██████  ███    ██ ███████ ██ \n"
              "██   ██ ██    ██ ████   ██ ██      ██ \n"
              "██   ██ ██    ██ ██ ██  ██ █████   ██ \n"
              "██   ██ ██    ██ ██  ██ ██ ██         \n"
              "██████   ██████  ██   ████ ███████ ██ \n")
        return
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
    print("\n░██████╗░░█████╗░███╗░░░███╗███████╗  \n"
          "██╔════╝░██╔══██╗████╗░████║██╔════╝  \n"
          "██║░░██╗░███████║██╔████╔██║█████╗░░  \n"
          "██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  \n"
          "╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  \n"
          "░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  \n"
          "\n"
          "░█████╗░██╗░░░██╗███████╗██████╗░\n"
          "██╔══██╗██║░░░██║██╔════╝██╔══██╗\n"
          "██║░░██║╚██╗░██╔╝█████╗░░██████╔╝\n"
          "██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗\n"
          "╚█████╔╝░░╚██╔╝░░███████╗██║░░██║\n"
          "░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n")
    time.sleep(1)
    print("Want to play again? Click on 'Run Driving Safely'")


game_start()
