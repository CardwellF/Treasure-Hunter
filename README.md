# Treasure-Hunter
## Introduction
Welcome to Treasure Hunter a text based adventure stratergy game built using python, where the aim is to have the most money at the end at the end of the game while avoiding traps along the way
## Project Overview
I plan to create a text based treasure hunting game which can be played as many times as the user wants due to all rooms generating randomly upon searching the room. For this program I intend to have treasure be money and have the player with the most money be the winner of the game this is to stop the game from randomly generating the treasure on the first tile the user or enemy visits, finishing the game straight away before the rest of the map is explored.
## Challenges and Solutions
while working on thisa program I faced a number of different challenges. 
My first challenge I faced during development was figuring out the map I tested multiple iterations including using 3D lists as well as using embedded lists. My solution to this was to use one 3D list were positiion was calucated useding the row and column number excluding the depth and using that to locate the next unidentified room.
## Search Algorithms
For my program i have made use of linear search to find specific numbers within my 3D list for the game map. I chose to use Linear Search due to the fact my list will never be ordered as the list if constantly being updated due to this using binary search or interpolation sort would be ineffective due to the fact that they require a sorted list to work. In addition Depth First search to find the fastest path to the nearest unidentified room.
## Psudocode
## Test Evidence
during my testing i had a a few errrors including miss spelt variable names and a few class inheriatance issues however all these issues have been fixed. However the largest error I faced during testing was that my classes would break this was due to adding variable names to the links which did not exist within the method this was fixed by re-arranging where the variable is called. Another problem I had was when it came to text inputs as a result I had to do some research into the keyboard import libary and found that it while using a testing file found that the import resolved my imput problem as i could have it be more responsive than having to press enter after every input was made.
| test type       | problem     | resolution  |
|:-----------:|:-----------:|:-----------:|
|classes       | inheritence |changed ordering of classses |
|Classes       | breaking    |removed and relocated missing variable names |
|inputs        | not responcive enough |used keyboard import |
|rooms         | being able to search multiple times |make the room change from an power up room or treasure room to being an empty room|
## Conclusions
in conclusion, even though I had multiple errors and issues regarding my code as explaned above, my program runs well and can be played as many times as the user likes with the locations of rooms completely random each time granting a new experience. While the opponent can not be played by a second person it was made to move arround the rooms and search for treasure and is capable of avoiding traps if the tile is already descovered opting to avoid it unless the opponent is surrounded by traps. As a result this game becomes a stratergy adventure game like cluedo due to the nature of the traps not being de-activated making the user have to remember what tiles have traps on and which do not.
