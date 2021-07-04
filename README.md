# Python_RPG_Game
Text based role playing game which reads and writes information from a text file

This program implements a text based RPG using Python's object oriented methodologies. It allows user to interact
with the game world through command line. It allows the user to select from different characters and then take them
to a wonderland where the player get a chance to collect different valuable items. It also provides a conflict 
scenario where the player either attacks or get attacked by diffenet enemy characters in the game world.

The aim for player is to explore all the places in the game world, collect as much valaubles as it ca keeping safe 
or attacking the opponenets in a way that at the end the player has a health level above a threshold. If a player
is able to do so, success is declared otherwise it ends up in a failure.

Upon completion of game following details are provided to the player and a copy of which is saved as a record,

* the details of valubale objects collected by the player.
* the details of conflicts either attack or trap in which player get indulged.
* the health level of the player.
* the program also provided a re-loading functionality where player can resume from an unfinished level.
* this is achieved by storing the key information in a text file at each step.
* the character and room description is stored in a text file which this program reads.

Last but not the least, the player is also provided with a summary of personal detials like the name, favourite
number and the time at which game was played.