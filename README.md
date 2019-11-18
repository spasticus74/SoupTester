# SoupTester - Linux executables to help with developing Soup 10 agents.

*souptest provides a simplified, single player version of the soup 10 game*
1) Copy the appropriate version to your Linux machine/VM.
2) Run:
  **./souptest \<path to your agent script\>**
  
souptest will provide some output that is suitable for testing & debugging your script. Some example output below:
```
Starting new game at Mon Nov 18 12:15:34 2019                                                                                                                                                                                                      
                                                                                                                                                                                                                                                   
Player "player4.py" (Ricky Cayley) added at (509, 442).                                                                                                                                                                                            
                                                                                                                                                                                                                                                   
Turn 0:                                                                                                                                                                                                                                            
R507C440T0F0,R507C441T0F0,R507C442T0F0,R507C443T0F0,R507C444T0F0,R508C440T0F0,R508C441T0F0,R508C442T0F0,R508C443T1F0,R508C444T0F0,R509C440T2F0,R509C441T0F1,R509C442T1F0,R509C443T0F0,R509C444T0F0,R510C440T0F0,R510C441T2F0,R510C442T0F0,R510C443T1F0,R510C444T1F0,R511C440T0F0,R511C441T0F0,R511C442T1F0,R511C443T0F1,R511C444T0F0                                                                                                                                                                  
player4.py plans to EAT|DL                                                                                                                                                                                                                         
STEP 0: EAT -   Tried to eat in an empty square.                                                                                                                                                                                                   
STEP 1: DL -    Moved to (510, 441)                                                                                                                                                                                                                
        Landed in a bad square!                                                                                                                                                                                                                    
Failed to eat this turn, starving.                                                                                                                                                                                                                 
Player health at end of turn: 14

Turn 1:
R508C439T0F0,R508C440T0F0,R508C441T0F0,R508C442T0F0,R508C443T1F0,R509C439T1F0,R509C440T2F0,R509C441T0F1,R509C442T1F0,R509C443T0F0,R510C439T0F0,R510C440T0F0,R510C441T2F0,R510C442T0F0,R510C443T1F0,R511C439T0F0,R511C440T0F0,R511C441T0F0,R511C442T1F0,R511C443T0F1,R512C439T1F0,R512C440T0F0,R512C441T0F0,R512C442T2F0,R512C443T3F0
player4.py plans to D|EAT
STEP 0: D -     Moved to (511, 441)
STEP 1: EAT -   Tried to eat in an empty square.
Failed to eat this turn, starving.
Player health at end of turn: 13

Turn 2:
R509C439T1F0,R509C440T2F0,R509C441T0F1,R509C442T1F0,R509C443T0F0,R510C439T0F0,R510C440T0F0,R510C441T2F0,R510C442T0F0,R510C443T1F0,R511C439T0F0,R511C440T0F0,R511C441T0F0,R511C442T1F0,R511C443T0F1,R512C439T1F0,R512C440T0F0,R512C441T0F0,R512C442T2F0,R512C443T3F0,R513C439T0F0,R513C440T0F0,R513C441T2F0,R513C442T0F0,R513C443T0F1
player4.py plans to UL|DL
STEP 0: UL -    Moved to (510, 440)
STEP 1: DL -    Moved to (511, 439)
Failed to eat this turn, starving.
Player health at end of turn: 12

Turn 3:
R509C437T0F0,R509C438T1F1,R509C439T1F0,R509C440T2F0,R509C441T0F1,R510C437T0F0,R510C438T0F0,R510C439T0F0,R510C440T0F0,R510C441T2F0,R511C437T0F0,R511C438T0F0,R511C439T0F0,R511C440T0F0,R511C441T0F0,R512C437T3F0,R512C438T3F0,R512C439T1F0,R512C440T0F0,R512C441T0F0,R513C437T0F0,R513C438T3F0,R513C439T0F0,R513C440T0F0,R513C441T2F0
player4.py plans to DL|EAT
STEP 0: DL -    Moved to (512, 438)
        Landed in a bad square!
STEP 1: EAT -   Tried to eat in an empty square.
        Landed in a bad square!
Failed to eat this turn, starving.
Player health at end of turn: 1

Turn 4:
R510C436T1F0,R510C437T0F0,R510C438T0F0,R510C439T0F0,R510C440T0F0,R511C436T0F0,R511C437T0F0,R511C438T0F0,R511C439T0F0,R511C440T0F0,R512C436T0F1,R512C437T3F0,R512C438T3F0,R512C439T1F0,R512C440T0F0,R513C436T1F0,R513C437T0F0,R513C438T3F0,R513C439T0F0,R513C440T0F0,R514C436T1F0,R514C437T3F0,R514C438T0F0,R514C439T2F0,R514C440T0F0
player4.py plans to UL|EAT
STEP 0: UL -    Moved to (511, 437)
STEP 1: EAT -   Tried to eat in an empty square.
Failed to eat this turn, starving.

!!! player4.py has died on turn 5 at (511, 437).
```

Looking more closely at the first turn:
```
Turn 0:                                                                                                                                                                                                                                            
R507C440T0F0,R507C441T0F0,R507C442T0F0,R507C443T0F0,R507C444T0F0,R508C440T0F0,R508C441T0F0,R508C442T0F0,R508C443T1F0,R508C444T0F0,R509C440T2F0,R509C441T0F1,R509C442T1F0,R509C443T0F0,R509C444T0F0,R510C440T0F0,R510C441T2F0,R510C442T0F0,R510C443T1F0,R510C444T1F0,R511C440T0F0,R511C441T0F0,R511C442T1F0,R511C443T0F1,R511C444T0F0                                                                                                                                                                  
player4.py plans to EAT|DL                                                                                                                                                                                                                         
STEP 0: EAT -   Tried to eat in an empty square.                                                                                                                                                                                                   
STEP 1: DL -    Moved to (510, 441)                                                                                                                                                                                                                
        Landed in a bad square!                                                                                                                                                                                                                    
Failed to eat this turn, starving.                                                                                                                                                                                                                 
Player health at end of turn: 14
```
line by line:
1) The turn described,
2) The environment passed to the agent. This will always be comma separated list of the 25 squares around the agent,
3) The moves that the agent requested to be played, in this case to eat in the current square then move down-left,
4) The results of attempting the first move. In this case the square did not have any food, so this was of no benefit,
5) The results of attempting the second move. The move succeeded (the new coordinates are shown),
6) Unfortunately the square the agent moved into was a bad one (water, desert, etc.),
7) Agents need to eat on every trun or else they lose health. Unfortunately the agent was not successful,
8) The agent has only 14 health points left after this turn (lost 1 point for not eating, 5 points for landing in a bad square)
