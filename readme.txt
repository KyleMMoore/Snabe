Welcome to Snabe!

Snabe is a two player, competitive take on the classic game Snake. The goal is to grow as long as possible before the timer runs out.

Players must eat food pellets to gain length. As with the original game, you must be careful not to run into yourself or the walls, or you will lose points.

However, there is another way to lose points- being attacked by your opponent.

By default, the two players cannot hurt one another. Colliding with your opponent will cause you to freeze in place until they have passed.
In order to deal damage, players must pick up powerups that spawn around the map at random. Each powerup wafer has a chance to award either a sword or a shield.
The sword allows a player to attack their opponent by running into them. If a body segment is hit by a sword, the target player will lose all segments from that point back.
If a player's head is hit by a sword, they automatically lose. A player can also get a shield powerup, which protects from all damage. This allows players to be hit by swords
without taking damage, pass through their own body segments, and bounce off of walls without losing points.

The game is played on a single keyboard, with player one moving with the WASD keys, and player two moving with the arrow keys.

In order to play this game, you must have Python installed. If you do not have the Pygame module installed, it is required for this game to run.
In order to install Pygame, open your command prompt and run the command "python -m pip install --user pygame"

Upon downloading and extracting Snabe.zip, you will find a number of files and subfolders contained within.

To play the game, simply load main.py into your favorite Python environment and run the module.


Below is a breakdown of each directory and source code file and the information contained within.

-The "images" directory contains all of the visual elements used by the game. This folder itself contains many subfolders.
    -The "background" directory holds "background.png", which is rendered into the window behind the action.
    -The "blue" directory holds all files for the blue snabe (player 2). There are separate sprites for each possible rotation that the Snabe can undergo.
     There are 4 plain head sprites, 4 shielded head sprites, 4 sword head sprites, 4 tail sprites, and 2 body sprites.
    -The "green" directory holds all files for the green snabe (player 1). This directory is identical to the "blue" directory, but differently colored.
    -The "items" directory holds the sprites for food pellets and powerup wafers.
    -The "menu" directory holds the sprites for the intro screen animation.
    -The "timer" directory holds the sprites for the timer and the numbers used for both the timer and score objects.
    -The "images" directory also holds a file called "dummy.bmp", which serves as a fallback when an image cannot be loaded.

The main directory also contains a number of .py files that contain all code required to run the game.
    -"body.py" contains all code for the segments of the Snabe bodies. Functions contained within include:
        -__init__: creates an instance of the Body class and sets up various fields and attributes.
        -update: performs updates on the segment's sprite, position, and fields.
        -blitme: blits the sprite to the screen.
        -drawSegment: decides which sprite the game should load for the segment.
        -destroy: removes the segment from the screen and all lists it is a part of.
        -__repr__: allows the object to be called in a "print" statement nicely. Displays object type, position, and index in the global entity list.
        -move: adjusts the segment's centerpoint based on which movement flag is active.
        -turn: uses set_direction to move in the given "new_direction". Also allows the last segment in the Snabe to remove turns from the head's list.
        -set_direction: changes movement flags to match the "new_direction" parameter.
        -connect: matches up adjacent edges between this segment and the preceding segment depending on current orientation.

    -"food.py" contains all code for the food pellets.
        -__init__: creates an instance of the Food class and sets up various fields and attributes.
        -chooseLocation: picks a random location within the playable field to spawn at.
        -setLocation: puts the pellet at the specified coordinate location.
        -getLocation: returns the centerpoint of the pellet as a tuple.
        -blitme: blits the pellet to the screen.
        -destroy: removes the pellet from all lists and the game.
        -__repr__: allows for the instance to be printed. Returns the object type, the centerpoint, and the index in the global entity list.

    -"global_toolbox.py" contains three classes which hold information used by all or most files.
        -GlobalSettings.class: contains several fields of constants that define aspects of the game. These values will never change during runtime.
        -GlobalFunctions.class: contains a couple of functions that are used by the game's core.
            -update_screen: blits all game components to the display window.
            -check_events: checks for events such as keypresses and exits and handles them appropriately.
        -GlobalVars.class: contains fields that will be updated during the game's runtime, and are accessed by all components of the game.
            -food_list: stores all food objects currently on the playing field.
            -wafer_list: stores all powerup wafers currently on the playing field.
            -timer_value: the current amount of time left in the game.
            -entities: a list of all currently active entities on the playing field. Does not include the timer or the scoreboards.

    -"main.py" contains the meat of the game.
        -run_game: creates the players, the timer, and the scoreboard, and then runs the game's main loop.
        -startScreen: plays the intro animation, waits for the player to start the game.
        -endScreen: displays the winning player, allows player to immediately start over or return to the title screen.

    -"readme.txt" contains useful information about the game's operation, concept, and structure. You are here.

    -"Score.py" contains all code for the game's scoreboards. Displays the score for one player (so two instances exist in-game).
        -__init__: creates an instance of the Score class, sets up various fields and attributes.
        -update: changes its appearance based on player score.
        -blitme: blits the scoreboard to the screen.

    -"snabe.py" contains all code for the Snabe heads.
        -__init__: creates the Snabe head, several important fields and attributes, and the Snabe's initial segments.
        -update: updates position, sprite, flags, and other important fields.
        -blitme: blits the head to the screen.
        -drawSnabe: decides which sprite the game should load for the head.
        -move: modifies the centerpoint of the head based on movement flags and current position.
        -bounce_off: sends the player off in a new direction based on position and direction before the bounce.
        -set_direction: sets the movement flags according to the "new_direction" parameter. Adds the location and new direction to the head's dict of turns.
        -check_collisions: checks the global entity list to see if any collisions are occuring.
        -check_powerups: checks to see if any powerups should be expiring.
        -is_moving: returns "True" if the player is not stunned.
        -get_direction: returns the current direction of movement according to the movement flags.
        -first_move: returns "True" if all movement flags and "is_stunned" are False.
        -head_on: returns "True" if the player and the opponent are colliding head on.
        -collision: deals with collisions according to the type of object being collided with.
        -stun: sets "is_stunned" to True, rendering the Snabe immobile.
        -do_powerup: sets powerup flags and stores the time at which they become active.
        -__add__: allows the + operator to add score and length to the Snabe.
        -__sub__: allows the - operator to remove score and length from the Snabe.
        -__repr__: allows for the Snabe to be printed. Returns the object type, centerpoint, and index in the global entity list.

    -"Timer.py" contains all code for the game's timer.
        -__init__: creates an instance of the Timer class and sets up various fields and attributes.
        -tick: advances the timer and chooses the appropriate image for the two digits.
        -switch: a recreation of the switch statement present in other programming languages. Chooses a number sprite based on the number passed in.
        -blitme: blits the timer to the screen.

    -"wafer.py" contains all code for the powerup wafers.
        -__init__: creates an instance of the Wafer class and sets up various fields and attributes.
        -set_type: randomly decides which powerup the wafer represents.
        -get_type: returns the type of powerup that the wafer represents.
        -chooseLocation: determines a spawning location within the playable area.
        -setLocation: sets the wafer's location to the given coordinate position.
        -getLocation: returns the centerpoint as a tuple.
        -blitme: blits the wafer to the screen.
        -__repr__: allows the wafer to be printed. Returns the object type, centerpoint, and index in the global entity list.