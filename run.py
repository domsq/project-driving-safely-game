import time  # Module required to add a pause as needed

invalid_choice = ("\nNot a valid choice, please try again\n")
current_scenario_index = -1

# Scenario content moved to list as discussed with mentor
SCENARIOS = [
  {
    "question": "\nYou start the drive to your holiday accommodation and " +
                "after driving\nfor a few miles " +
                "you encounter some slow traffic. " +
                "\nThe driver behind you seems to be following a bit too " +
                "closely\nwhat should you do?\n" +
                "\nA: Slow down gradually, building more of a gap " +
                "between you\nand the car in front\n" +
                "\nB: Move over towards a position a bit left " +
                "of the centre line of the road\n",
    "correct_answer": "\nWell done, this is the safe way to handle " +
                      "the situation.",
    "wrong_answer": "\nSorry, this is the wrong answer. " +
                    "The driver behind attempts " +
                    "\nto undertake you and collides " +
                    "with you in the process.\n" +
                    "\nRule #151 of the Highway Code " +
                    "(pg. 50, 2015 Edition) states: " +
                    "\nNever get so close to the vehicle in front " +
                    "that you cannot stop safely.",
    "correct_choice": "a"
  },
  {
    "question": "\nThe traffic improves but it starts to rain quite heavily." +
                " You are \ntravelling behind another vehicle, how much of a" +
                " time gap should you allow?\n" +
                "\nA: Three Seconds\n" +
                "\nB: Four Seconds\n",
    "correct_answer": "\nCorrect - you need to allow extra distance on " +
                      "slippery and wet roads.",
    "wrong_answer": "\nNo, you have selected the wrong answer. " +
                    "The vehicle ahead " +
                    "brakes \nsuddenly and despite your best " +
                    "efforts, you’re unable " +
                    "to stop in time \nand collide with it.\n\n" +
                    "Rule #227 of the Highway Code (pg. 76, 2015 " +
                    "Edition) states: \n" +
                    "In wet weather, stopping distances will be " +
                    "at least double " +
                    "those \nrequired for stopping on dry roads.",
    "correct_choice": "b"
  },
  {
    "question": "\nThe weather improves and it becomes dry and warm. " +
                "You are driving" +
                "\non a 50mph road at the speed limit and you spot " +
                "some stationary " +
                "traffic \nup ahead. What’s the minimum safe distance to " +
                "allow for stopping?\n" +
                "\nA: 53m / 175 ft\n" +
                "\nB: 36m / 120 ft\n",
    "correct_answer": "\nWell done, this is the average stopping " +
                      "distance from 50 mph." +
                      " Of course\nit’s always better to allow more " +
                      "than you think.",
    "wrong_answer": "\nSorry, this is not the right answer. You " +
                    "misjudge the " +
                    "distance to the \nvehicles ahead and are " +
                    "unable to stop in " +
                    "time and crash into the \nstationary traffic. \n" +
                    "\nPg. 42 of the Highway Code (2015 Edition) shows " +
                    "that the stopping \ndistance to allow when " +
                    "travelling at 50mph " +
                    "on a dry road in good \ncondition is at least " +
                    "53m / 175 ft.",
    "correct_choice": "a"
   },
  {
    "question": "\nYou are now travelling on a dual carriageway. There is " +
                "a slow vehicle \nin front of you and you are " +
                "considering overtaking" +
                " them on the left. \nIs this allowed?\n" +
                "\nA: Yes, it’s okay to overtake a slower vehicle in the " +
                "right-hand lane of a \ndual carriageway\n" +
                "\nB: No, you can only do this on a one-way street\n",
    "correct_answer": "\nCorrect, it is okay to overtake on the left" +
                      " when on a one-way street.",
    "wrong_answer": "\nIncorrect - as you attempt to pass the " +
                    "vehicle the driver" +
                    " has started \nmoving over to the left to allow " +
                    "you past and" +
                    " you crash into the other car.\n\n" +
                    "Rule #268 of the Highway Code (pg. 89, 2015 " +
                    "Edition) states:" +
                    "\nWhen travelling on a motorway, do not overtake " +
                    "on the left or" +
                    " move \nto a lane on your left to overtake.",
    "correct_choice": "b"
    },
  {
    "question": "\nYou are now driving through some countryside on a " +
                "road that has " +
                "some high \nhedges on either side of it." +
                " You come up to a left-hand bend" +
                " and are \nconcerned about the lack of visibility of " +
                "the road ahead" +
                " caused\nby the hedges. What should you watch out for?\n" +
                "\nA: Pedestrians coming towards you\n" +
                "\nB: No sign to warn of the bend\n",
    "correct_answer": "\nCorrect, if the road has no footpaths " +
                      "or pavements\n" +
                      "pedestrians will need to walk facing traffic.",
    "wrong_answer": "\nThis is not quite the right answer. You don’t " +
                    "see some " +
                    "pedestrians \napproaching and collide with them, " +
                    "injuring them as a result.\n" +
                    "\nRule #154 of the Highway Code (pg. 51, 2015 Edition) " +
                    "advises to approach\ncountry roads with extra caution, " +
                    "particularly when approaching\nbends as your " +
                    "visibility of" +
                    " pedestrians, etc. may be obscured. ",
    "correct_choice": "a"
    },
  {
    "question": "\nThe road visibility improves but you need to " +
                "make a right turn into a \nside road and have a " +
                "queue of traffic " +
                "behind you. Why is it a good idea to \ncheck your " +
                "side mirror on " +
                "the right before you turn?\n" +
                "\nA: To see if anyone is trying to overtake you\n" +
                "\nB: To see whether the side road is clear\n",
    "correct_answer": "\nCorrect, you may have a driver trying to " +
                      "overtake you, even " +
                      "though \nthey should go around you on the left" +
                      " if you’re " +
                      "turning right...",
    "wrong_answer": "\nNo, this is the wrong answer. You start turning and " +
                    "out of nowhere" +
                    "\na car who was trying to overtake you (even " +
                    "though this " +
                    "wouldn’t be safe \nto do) collides with you.\n" +
                    "\nRule #180 of the Highway Code (pg. 62, 2015 " +
                    "Edition) advises" +
                    "\nto check your mirrors and blind spot to " +
                    "ensure you’re not " +
                    "being \novertaken before making the turn.",
    "correct_choice": "a"
    },
  {
    "question": "\nYou notice that it has started raining again. You spot " +
                "a hazard ahead \nthat you need to slow down for and " +
                "attempt to brake " +
                "but your \nanti-lock brakes don’t seem to be working. " +
                "Your car starts to skid. \nWhat should you do next?\n"
                "\nA: Use the handbrake to see if this helps\n"
                "\nB: Release the brake pedal\n",
    "correct_answer": "\nCorrect, you’d need to initially release the " +
                      "brake pedal to stop the skid \nand then try " +
                      "carefully applying it again.",
    "wrong_answer": "\nWrong, this causes your car to go into a sideways " +
                    "slide and you \ncollide with another car.\n" +
                    "\nRule #119 of the Highway Code (pg.38, 2015 " +
                    "Edition) states: \nIf skidding occurs, remove the " +
                    "cause by releasing the brake pedal fully \nor " +
                    "easing off the accelerator. ",
    "correct_choice": "b"
    }
]


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
    load_next_scenario()


# Function to load scenarios as discussed with mentor
def load_next_scenario():
    """
    Function to load next scenario from list "SCENARIOS".
    Will also finish game if all scenarios completed.
    """
    global current_scenario_index
    current_scenario_index = current_scenario_index + 1
    if current_scenario_index == len(SCENARIOS):
        print("You won!")
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
        time.sleep(1)
        load_next_scenario()
    else:
        print(scenario["wrong_answer"])
        time.sleep(1)
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
