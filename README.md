# Treasure-Hunter
## Introduction
Welcome to Treasure Hunter a text based python game where the aim is to have the most money at the end
## Project Overview
I plan to create a text based treasure hunting game which can be played as many times as the user wants due to all rooms generating randomly upon searching the room.
## Challenges and Solutions
while working on thisa program I faced a number of different challenges. 
My first challenge I faced during development was figuring out the map I tested multiple iterations including using 3D lists as well as using embedded lists. My solution to this was to use one 2D list allowing both players to be in the same room as each other without overriding, this also allowed me to randomise room type makng the game more chance based
## Search Algorithms
For my program i have made use of linear search to find specific numbers within my 2D list for the game map. I chose to use Linear Search due to the fact my list will never be ordered as the list if constantly being updated due to this using binary search or interpolation sort would be ineffective due to the fact that they require a sorted list to work.
## Test Evidence
during my testing i had a a few errrors including miss spelt variable names and a few class inheriatance issues however all these issues have been fixed. However the largest error I faced during testing was that my classes would break this was due to adding variable names to the links which did not exist within the method this was fixed by re-arranging where the variable is called. Another problem I had was when it came to text inputs as a result I had to do some research into the keyboard import libary and found that it while using a testing file found that the import resolved my imput problem as i could have it be more responsive than having to press enter after every input was made.
| test        | problem     | resolution  |
|:-----------:|:-----------:|:-----------:|
|classes       | inheritence |changed ordering of classses |
|Classes       | breaking    |removed and relocated missing variable names |
|inputs        | not responcive enough |used keyboard import |
## Conclusions
in conclusion, even though I had multiple errors and issues regarding my code as explaned above 
