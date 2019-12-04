# SoupTester - Linux executables to help with developing Soup 10 agents.

*souptest provides a simplified, single player version of the soup 10 game*
1) Copy the appropriate version to your Linux machine/VM.
2) Run:
  **./souptest \<path to your agent script\>**
  
souptest will provide some output that is suitable for testing & debugging your script. Some example output below:
```
Starting new game at Thu Dec  5 10:30:37 2019
  
Player "player4.py" (Ricky Cayley) added at (426, 490).

Turn 0:
R424C488T1F0P0,R424C489T1F1P0,R424C490T3F0P0,R424C491T1F0P0,R424C492T3F0P0,R425C488T0F0P0,R425C489T2F0P0,R425C490T1F0P0,R425C491T2F0P1,R425C492T0F0P0,R426C488T2F0P0,R426C489T0F0P0,R426C490T0F0P1,R426C491T3F0P0,R426C492T3F0P0,R427C488T0F0P0,R427C489T3F0P0,R427C490T0F0P0,R427C491T2F0P0,R427C492T0F0P0,R428C488T0F0P0,R428C489T2F0P0,R428C490T0F0P0,R428C491T0F1P0,R428C492T1F0P0
player4.py plans to EAT|UL
STEP 0: EAT -   Tried to eat in an empty square.
STEP 1: UL -    Moved to (425, 489)
        Landed in a bad square!
Failed to eat this turn, starving.
Player health at end of turn: 14

Turn 1:
R423C487T0F0P0,R423C488T0F0P0,R423C489T3F0P0,R423C490T0F0P0,R423C491T3F0P0,R424C487T2F0P0,R424C488T1F0P0,R424C489T1F1P0,R424C490T3F0P0,R424C491T1F0P0,R425C487T0F0P0,R425C488T0F0P0,R425C489T2F0P1,R425C490T1F0P0,R425C491T2F0P0,R426C487T0F0P0,R426C488T2F0P0,R426C489T0F0P0,R426C490T0F0P0,R426C491T3F0P0,R427C487T0F0P0,R427C488T0F0P0,R427C489T3F0P0,R427C490T0F0P0,R427C491T2F0P0
player4.py plans to L|UR
STEP 0: L -     Moved to (425, 488)
STEP 1: UR -    Moved to (424, 489)
Failed to eat this turn, starving.
Player health at end of turn: 13

Turn 2:
R422C487T0F0P0,R422C488T0F0P0,R422C489T0F0P0,R422C490T0F0P0,R422C491T2F0P1,R423C487T0F0P0,R423C488T0F0P0,R423C489T3F0P0,R423C490T0F0P0,R423C491T3F0P0,R424C487T2F0P0,R424C488T1F0P0,R424C489T1F1P1,R424C490T3F0P0,R424C491T1F0P0,R425C487T0F0P0,R425C488T0F0P0,R425C489T2F0P0,R425C490T1F0P0,R425C491T2F0P0,R426C487T0F0P0,R426C488T2F0P0,R426C489T0F0P0,R426C490T0F0P0,R426C491T3F0P0
player4.py plans to EAT|UR
STEP 0: EAT -   Ate at (424, 489)
STEP 1: UR -    Moved to (423, 490)
Player health at end of turn: 14

Turn 3:
R421C488T1F1P0,R421C489T0F0P0,R421C490T0F0P0,R421C491T1F0P0,R421C492T2F0P0,R422C488T0F0P0,R422C489T0F0P0,R422C490T0F0P0,R422C491T2F0P1,R422C492T0F0P0,R423C488T0F0P0,R423C489T3F0P0,R423C490T0F0P1,R423C491T3F0P0,R423C492T0F0P0,R424C488T1F0P0,R424C489T1F0P0,R424C490T3F0P0,R424C491T1F0P0,R424C492T3F0P0,R425C488T0F0P0,R425C489T2F0P0,R425C490T1F0P0,R425C491T2F0P0,R425C492T0F0P0
player4.py plans to U|R
STEP 0: U -     Moved to (422, 490)
STEP 1: R -     Moved to (422, 491)
        Landed in a bad square!
        FIGHT! Player WON.
Failed to eat this turn, starving.
Player health at end of turn: 8

Turn 4:
R420C489T3F0P0,R420C490T0F0P0,R420C491T1F0P0,R420C492T0F0P0,R420C493T3F0P0,R421C489T0F0P0,R421C490T0F0P0,R421C491T1F0P0,R421C492T2F0P0,R421C493T1F0P0,R422C489T0F0P0,R422C490T0F0P0,R422C491T2F0P2,R422C492T0F0P0,R422C493T3F0P0,R423C489T3F0P0,R423C490T0F0P0,R423C491T3F0P0,R423C492T0F0P0,R423C493T1F0P0,R424C489T1F0P0,R424C490T3F0P0,R424C491T1F0P0,R424C492T3F0P0,R424C493T3F0P0
player4.py plans to DL|UR
STEP 0: DL -    Moved to (423, 490)
STEP 1: UR -    Moved to (422, 491)
        Landed in a bad square!
        FIGHT! Player LOST the fight and suffered 6 points of damage.

!!! player4.py has died on turn 5 at (422, 491).
```

Looking more closely at the 4th turn:
```
Turn 4:
R420C489T3F0P0,R420C490T0F0P0,R420C491T1F0P0,R420C492T0F0P0,R420C493T3F0P0,R421C489T0F0P0,R421C490T0F0P0,R421C491T1F0P0,R421C492T2F0P0,R421C493T1F0P0,R422C489T0F0P0,R422C490T0F0P0,R422C491T2F0P2,R422C492T0F0P0,R422C493T3F0P0,R423C489T3F0P0,R423C490T0F0P0,R423C491T3F0P0,R423C492T0F0P0,R423C493T1F0P0,R424C489T1F0P0,R424C490T3F0P0,R424C491T1F0P0,R424C492T3F0P0,R424C493T3F0P0
player4.py plans to DL|UR
STEP 0: DL -    Moved to (423, 490)
STEP 1: UR -    Moved to (422, 491)
        Landed in a bad square!
        FIGHT! Player LOST the fight and suffered 6 points of damage.

!!! player4.py has died on turn 5 at (422, 491).
```
line by line:
1) The turn described,
2) The environment passed to the agent. This will always be comma separated list of the 25 squares around the agent. In this latest version there is a new value indicating the presence of a player or predator. Note that this includes your agent, so the 13th square will ALWAYS be at least 'P1',
3) The moves that the agent requested to be played, in this case to move down-left then move up-right,
4) The results of attempting the first move. The move succeeded (the new coordinates are shown),
5) The results of attempting the second move,
6) Unfortunately the square the agent moved into was a bad one (water, desert, etc.). The agent loses 5 health points,
7) Unfortunately the square also contained a predator which beat the agent in a fight, costing the agent another 6 health points,
8) Agents need to eat on every turn or else they lose health. Unfortunately the agent was not successful and loses another 1 health point,
9) The agent started the turn with 8 health points and lost 12 during this turn meaning it is now dead.
