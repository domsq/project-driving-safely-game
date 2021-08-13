# Driving Safely

Driving Safely is a game where users attempt to make it successfully through all the scenarios presented, by making the right choice, to reach the destination safely. It is a blend of an interactive story with a quiz to test the user's knowledge of road rules and traffic safety. However, unlike a quiz where you would just receive a score at the end, with this game making the wrong choice can end badly so choose wisely. The game is CLI based so the user would type in the required answer. 

[Link to deployed site](https://driving-safely.herokuapp.com/)

## UX

I've designed the app to function like an interactive story, whereby users will be presented with choices as they progress through the scenarios, and depending on the choice made this will determine whether the story progresses or not. Whether a right or wrong choice is made, the game shows a corresponding answer and so is also educational as well. If the user makes a wrong choice and this causes a game over condition, it will also provide details of the relevant part of The Highway Code that explains this. The game is played from an emulated terminal and so is command line based, input is via keyboard entry. 

The app has functions for the following:
- To handle the game start
- Text input with validation when having to make a choice
- Loading of the next scenario
- Displaying of current scenario content and evaluating the choice made
- Handling a game over condition 
- Handling game successful completion 

As shown in the logic flow below, if the user makes the correct choice they progress onto the next scenario but if they don't, then a game over condition occurs. The user is then asked whether they'd like to try again. If the user successfully gets through all scenarios then a game completion message is displayed.


![Image of flow diagram](https://raw.githubusercontent.com/domsq/project-driving-safely-game/main/screenshots/flow_diagram.JPG)

As the app is command line based, there are no graphics or colour, etc present however I have inserted some ascii art to make the display a bit more visually pleasing for the user. 

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

The app has a button at the top to restart it at any point (initial loading of the page starts the app automatically):

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

### Features Left to Implement

- Add additional scenarios and \ or choice options 
- Increase the number of paths a user could take through the game to reach the end
- Implement a scoring system 

## Technologies Used


## Testing



### Bugs 


### Validator Testing


## Deployment


## Credits 

### Content



### Media


### Acknowledgements




