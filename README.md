# Driving Safely

Driving Safely is a game where users attempt to make it successfully through all the scenarios presented, by making the right choice, to reach the destination safely. It is a blend of an interactive story with a quiz to test the user's knowledge of road rules and traffic safety. However, unlike a quiz where you would just receive a score at the end, with this game making the wrong choice can end badly so choose wisely. The game is CLI based so the user would type in the required answer. 

[Link to deployed site](https://driving-safely.herokuapp.com/)

## UX

I've designed the game to function like an interactive story, whereby users will be presented with choices as they progress through the scenarios, and depending on the choice made this will determine whether the story progresses or not. Whether a right or wrong choice is made, the game shows a corresponding answer and so is also educational as well. If the user makes a wrong choice and this causes a game over condition, it will also provide details of the relevant part of The Highway Code that explains this. The game is played from an emulated terminal and so is command line based, input is via keyboard entry. 

The game has functions for the following:
- To handle the game start
- Input for a user name with validation
- Text input with validation when having to make a choice
- Loading of the next scenario
- Displaying of current scenario content and evaluating the choice made
- Handling a game over condition 
- Handling game successful completion
- Asking whether the user would like to play again and validating the choice made 

As shown in the logic flow below, if the user makes the correct choice they progress onto the next scenario but if they don't, then a game over condition occurs. The user is then asked whether they'd like to try again. If the user successfully gets through all scenarios then a well done message is displayed which also asks whether they'd like to play again. 

![Image of flow diagram](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/flow_diagram.JPG)

As the game is command line based, there are no graphics or colour, etc present however I have inserted some ascii art to make the display a bit more visually pleasing for the user. 

To tidy up the look of the run.py file, I moved the scenarios content and ASCII art and messages to the files config.py and constants.py respectively. This was a good suggestion made by my mentor. 

User stories as follows:

### New users:

-	A new driver is looking to test their road safety knowledge<br>
-	An experienced driver is looking to challenge, and possibly brush up on, their knowledge of road safety<br>
-	A non driver is looking to play a game to learn more about driving theory and road safety
 
### Returning users:

-	Users who haven’t successfully made it to the end of the game can try again to see if they’re able to do any better<br>
-	Users will be looking to see if the scenarios have been updated \ changed and if any additional functionality has been added

### Frequent users:

-   As per returning users

## Features

### Existing Features

The game has a button at the top to restart it at any point (initial loading of the page starts the app automatically):

![Image of run button](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/run_button.JPG)

It also has an intro message, welcoming the user to the game and briefly explaining how to play it:

![Image of intro message](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/intro_message.JPG)

Below the intro message is an ascii art image followed by a prompt for the user to enter a name:

![Image of intro graphic](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/intro_image.JPG)

Playing through the game will present different scenarios as the user progresses:

![Image of a scenario](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/scenario.JPG)

Selecting a wrong choice will result in a game over condition:

![Image of game over message](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/game_over.JPG)

If the user successfully makes it through all scenarios, a "well done" message is shown:

![Image of game completion message](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/well_done.JPG)

Upon either a game over condition or successful game completion, the user is presented with an option to play again:

![Image of play again prompt](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/play_again.JPG)

### Features Left to Implement

- Add additional scenarios and \ or choice options 
- Increase the number of paths a user could take through the game to reach the end
- Implement a scoring system 

## Technologies Used

- HTML - Required for the emulated terminal as provided by Code Institute
- CSS - Required for the emulated terminal as provided by Code Institute
- JavaScript - Required for the emulated terminal as provided by Code Institute
- Python - Language that the game is written in
- Gitpod - IDE used for development, incorporates git version control
- GitHub - Repository where code is kept and also git version control
- Heroku - Platform through which the game is deployed
- [fsymbols](https://fsymbols.com/text-art/) - Used for creation of ascii word art
- [Text to ASCII Art Generator](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Used for creation of ascii word art
- [Ascii Art converter](https://manytools.org/hacker-tools/convert-images-to-ascii-art/) - Used for creation of ascii art image

## Testing

-	A new driver is looking to test their road safety knowledge<br><br>
The user will land on the intro message which explains what the game is about:<br>
![Image of intro message](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/intro_message.JPG)<br>
Once they've entered a name, they'll move onto the scenarios to play through:<br>
![Image of a scenario](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/scenario.JPG)<br><br>
-	An experienced driver is looking to challenge, and possibly brush up on, their knowledge of road safety<br><br>
The user has various scenarios to play through, to test their knowledge:<br>
![Image of a scenario](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/scenario.JPG)<br><br>
-	A non driver is looking to play a game to learn more about driving theory and road safety<br><br>
There are various scenarios which are based on actual road safety questions for the user to attempt:<br>
![Image of a scenario](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/scenario.JPG)<br><br>

The game has been tested using the following browsers:<br>
- Google Chrome<br>
- Microsoft Edge<br>
- Mozilla Firefox<br><br>

I played through the game multiple times from beginning to end to ensure the logic flows as expected. I also had my wife test the game to make sure it ran okay for her. 
When tested on a PC, the game displays as expected and functions as required. 

The game was also tested on both Samsung Galaxy S20 FE 5G and Oppo Find X2 Lite handsets and while it is playable on a mobile phone, it is best experienced using a PC browser. This is likely due to the nature of a terminal type interface. 

I tested that when presented with a choice in the game, the text input has to be a valid option as otherwise you are presented with a "Not a valid choice, please try again" message. You are then prompted to input text again, until a valid choice has been entered.

The scenarios are loaded in turn as expected and getting through all of them successfully triggers a game completion condition. If a wrong choice is picked, the game over condition is triggered. 

Upon either game over or game completion, you are prompted as to whether you'd like to play again. If "y" is selected, this restarts the game and if "n" is selected, this ends the program. If an invalid choice is made, you are prompted to choose an option until a valid choice is selected.

### Bugs 

While creating my application, the following bugs popped up:<br>
- Initially when setting up the logic to evaluate the user choices for the scenarios, I tried to use syntax such as "if choice == "a" or "A". This doesn't work, so I rather set input to be made lowercase prior to being evaluated.
- Another issue I encountered was getting text to display correctly when in Heroku, without any wrapping of words being split part way through. This was corrected through carefully limiting how much text is shown per line.
- When initially trying to reference the dictionary keys for the scenario objects, from within the show_scenario function, this wouldn't work due to my forgetting the required "[ ]" characters. Once this was corrected, the scenarios would then load as expected.
- When creating and testing the play_again function, it didn't initially work due to the fact that it wasn't resetting the scenario index each time, so the value was getting out of sync. This was corrected through referencing the global variable for the scenario index and setting it accordingly for a game restart.


### Validator Testing

All three of the Python files (config.py, constants.py, run.py) show no errors or warnings when run through a PEP8 checker:

- config.py:<br><br>
![Image of config.py validation](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/config_py_validation.JPG)<br><br>
- constants.py:<br><br>
![Image of constants.py validation](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/constants_py_validation.JPG)<br><br>
- run.py:<br><br>
![Image of run.py validation](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/run_py_validation.JPG)<br><br>

## Deployment

My game was deployed via Heroku as follows:
- From the terminal in Gitpod, type the following command: "pip3 freeze > requirements.txt"
- Perform a git add, commit and push.
- Navigate to https://dashboard.heroku.com/apps and login.
- Select New > Create new app.
- For app name type "driving-safely" and for region choose "Europe". Click "Create app".
- Once the app has been created, select it from the dashboard and then navigate to Settings > Buildpacks.
- Click "Add buildpack" and then add the following in turn: heroku/python ; heroku/nodejs.
- Browse to the "Deploy" section.
- For "Deployment method" select GitHub. If access hasn't already been configured, do this from Account settings > Applications > Third-party Services. 
- Search for the required repository, in this case "project-driving-safely-game", then once found click "Connect".
- Scroll down to "Automatic deploys", ensure the branch selected is "main" and then click "Enable Automatic Deploys".
- Each time a push is made to the repository "project-driving-safely-game", Heroku deploys an updated version of the app.
- To obtain the deployed link, browse to "Activity" from within the app on Heroku, select "View build log" for the most recent deployment version and find the link at the bottom of the output.  

## Credits 

### Content



### Media


### Acknowledgements




