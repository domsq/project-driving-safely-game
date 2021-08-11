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
    print("Welcome to Driving Safely. The aim is to get to your "
          "destination\nwithout incident. "
          "You’ll be presented with scenarios along the way\nchoose wisely"
          " as the wrong choice could end badly.\n\nEnjoy and have fun!\n")
    time.sleep(1)
    name = input("Please enter your name:- \n")
    time.sleep(1)
    print(f"\nWelcome {name}\n"
          "\nYou are going on holiday to your favourite seaside resort and "
          "have \nbeen looking forward to the break for the last few months."
          "\nYour car is packed up and you are ready to start your journey.")
    time.sleep(1)
    scenario_one()


def scenario_one():
    """
    Function for controlling scenario one
    """
    print("\nYou start the drive to your holiday accommodation and "
          "after driving\nfor a few miles "
          "you encounter some slow traffic. "
          "\nThe driver behind you seems to be following a bit too "
          "closely\nwhat should you do?\n"
          "\nA: Slow down gradually, building more of a gap "
          "between you\nand the car in front\n"
          "\nB: Move over towards a position a bit left "
          "of the centre line of the road\n")
    selection = text_input()
    if selection == "a":
        print("\nWell done, this is the safe way to handle the situation.")
        time.sleep(1)
        scenario_two()
    elif selection == "b":
        print("\nSorry, this is the wrong answer.  The driver behind attempts "
              "\nto undertake you and collides with you in the process.\n"
              "\nRule #151 of the Highway Code (pg. 50, 2015 Edition) states: "
              "\nNever get so close to the vehicle in front "
              "that you cannot stop safely.")
        time.sleep(1)
        game_over()
    else:
        print(invalid_choice)
        time.sleep(1)
        scenario_one()


def scenario_two():
    """
    Function for controlling scenario two
    """
    print("\nThe traffic improves but it starts to rain quite heavily. "
          "You are \ntravelling behind another vehicle, how much of a "
          "time gap should you allow?\n"
          "\nA: Three Seconds\n"
          "\nB: Four Seconds\n")
    selection = text_input()
    if selection == "b":
        print("\nCorrect - you need to allow extra distance on "
              "slippery and wet roads.")
        time.sleep(1)
        scenario_three()
    elif selection == "a":
        print("\nNo, you have selected the wrong answer.  The vehicle ahead "
              "brakes \nsuddenly and despite your best efforts, you’re unable "
              "to stop in time \nand collide with it.\n\n"
              "Rule #227 of the Highway Code (pg. 76, 2015 Edition) states: \n"
              "In wet weather, stopping distances will be at least double "
              "those \nrequired for stopping on dry roads.")
        time.sleep(1)
        game_over()
    else:
        print(invalid_choice)
        time.sleep(1)
        scenario_two()


def scenario_three():
    """
    Function for controlling scenario three
    """
    print("\nThe weather improves and it becomes dry and warm. You are driving"
          "\non a 50mph road at the speed limit and you spot some stationary "
          "traffic \nup ahead. What’s the minimum safe distance to "
          "allow for stopping?\n"
          "\nA: 53m / 175 ft\n"
          "\nB: 36m / 120 ft\n")
    selection = text_input()
    if selection == "a":
        print("\nWell done, this is the average stopping distance from 50 mph."
              " Of course\nit’s always better to allow more than you think.")
        time.sleep(1)
        scenario_four()
    elif selection == "b":
        print("\nSorry, this is not the right answer. You misjudge the "
              "distance to the \nvehicles ahead and are unable to stop in "
              "time and crash into the \nstationary traffic. \n"
              "\nPg. 42 of the Highway Code (2015 Edition) shows "
              "that the stopping \ndistance to allow when travelling at 50mph "
              "on a dry road in good \ncondition is at least 53m / 175 ft.")
        time.sleep(1)
        game_over()
    else:
        print(invalid_choice)
        time.sleep(1)
        scenario_three()


def scenario_four():
    """
    Function for controlling scenario four
    """
    print("\nYou are now travelling on a dual carriageway. There is "
          "a slow vehicle \nin front of you and you are considering overtaking"
          " them on the left. \nIs this allowed?\n"
          "\nA: Yes, it’s okay to overtake a slower vehicle in the "
          "right-hand lane of a \ndual carriageway\n"
          "\nB: No, you can only do this on a one-way street\n")
    selection = text_input()
    if selection == "b":
        print("\nCorrect, it is okay to overtake on the left"
              " when on a one-way street.")
        time.sleep(1)
        scenario_five()
    elif selection == "a":
        print("\nIncorrect - as you attempt to pass the vehicle the driver"
              " has started \nmoving over to the left to allow you past and"
              " you crash into the other car.\n\n"
              "Rule #268 of the Highway Code (pg. 89, 2015 Edition) states:"
              "\nWhen travelling on a motorway, do not overtake on the left or"
              " move \nto a lane on your left to overtake.")
        time.sleep(1)
        game_over()
    else:
        print(invalid_choice)
        time.sleep(1)
        scenario_four()


def scenario_five():
    """
    Function for controlling scenario five
    """
    print("\nYou are now driving through some countryside on a road that has "
          "some high \nhedges on either side of it."
          " You come up to a left-hand bend"
          " and are \nconcerned about the lack of visibility of the road ahead"
          " caused\nby the hedges. What should you watch out for?\n"
          "\nA: Pedestrians coming towards you\n"
          "\nB: No sign to warn of the bend\n")
    selection = text_input()
    if selection == "a":
        print("\nCorrect, if the road has no footpaths or pavements\n"
              "pedestrians will need to walk facing traffic.")
    elif selection == "b":
        print("\nThis is not quite the right answer. You don’t see some "
              "pedestrians \napproaching and collide with them, injuring"
              " them as a result.\n"
              "Rule #154 of the Highway Code (pg. 51, 2015 Edition) "
              "advises to approach\ncountry roads with extra caution, "
              "particularly when approaching\nbends as your visibility of"
              " pedestrians, etc. may be obscured. ")
        time.sleep(1)
        game_over()
    else:
        print(invalid_choice)
        time.sleep(1)
        scenario_five()


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
