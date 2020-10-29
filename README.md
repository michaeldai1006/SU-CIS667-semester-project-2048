# SU CIS667 Semester Project 2048 Game AI
## About
Command line 2048 game, written in Python. With slight modification to the original game rule: the agent can also choose to rotate the tiles in the 2x2 square in the middle of the board by +/- 90 degrees.

## Dependencies
Python 3.4 or above is required. Make sure following Python dependencies are installed before executing the game:
1. [numpy](https://numpy.org/)

## Execution
1. Clone project to local
```
git clone https://github.com/michaeldai1006/SU-CIS667-semester-project-2048.git
```
2. Change directory to project home directory
```
cd ./SU-CIS667-semester-project-2048
```
3. Run main game file
```
python3 ./game/2048_game.py
```

## Game Play
Provide game board size when seeing following command line prompt:
```
Enter game board size (4, 6 or 8): 
```
At the beginning of each turn the current game state will be printed. You will also be provided a list of valid actions in [], type in your next move accordingly.
```
Current state:
   16    2    0    4

    8    0    0    0

    0    4    0    0

    0    0    0    0
['u = Slide Up', 'd = Slide Down', 'l = Slide Left', 'r = Slide Right', 'rc = Rotate Center Clockwise', 'rcc = Rotate Center Counterclockwise']
Enter an action: 
```

## Credits
tdai06, kkha, dyzheng, ztanruan all rights reserved.