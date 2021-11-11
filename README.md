# MinGame

The objective is simple: choose the option that the minority of players choose.

Basic description of game:
  1) Each round, output either 0 or 1
  2) Players in the minority will score a point
  3) First player to reach target score (~6000) wins that match
  4) Many matches will run, keeping track of winners
  5) Game code will be available here indefinitely

Scores for each match will be logged and available

Rules for entry:
  1) Submissions are in the form of python code as a **single** function 
  2) Submissions should be made directly to Ripple_Echo#8557 on Discord as either text or .py
  3) Modules imported limited to *math*  *random*  *numpy*
  4) You may not directly reference any code of other entrants
  5) Limit of one entry per player
  6) This game requires an odd number of players. If even, the host will add an entry.
  7) In event of errors or other issues, I will work with you to fix the code
  8) The host reserves the right to solely decide which entrants are valid
  9) All entrants code will be hosted here (under CC0 licence AKA public domain) after the game
  10) Please give your function a short, fun, descriptive name
  11) Please also leave any contact details you wish in your code, with a reminder that it is public
  
  More on CC0: https://creativecommons.org/share-your-work/public-domain/cc0/

Guide for game:
  1) The input for all entrants will be "*The Table*"
  2) The output should be either 0 or 1 (numbers not strings)
  3) Invalid outputs will be randomized
  4) The Table consists of a 2D list containing all moves by all players for all rounds
  5) Index 0 of *The Table* is a list of current scores for the match
  6) Therefor, index number = round number, so rounds are not zero-indexed.
  7) Every entrant will be given a fixed index, and that list will be made public *before* the code deadline.
  8) For example, "Table [123] [4]" referrences the 123th move of player ID 4 (player IDs will be zero-indexed)
  9) From above, notice each entrant has access to every other's score and move history
  10) As well, players will be able to referrence specific other players in their code
  11) Cooperation, collaboration, and collusion are permitted, publically or privately

Please feel free to ask any questions to me over discord.
Contest is **not** limited to UofBayes members only, invite as you wish.
Submission deadline TBA, but will not be before November 17th 


Further notes about Table data:
```
  [[score_p1, score_p2, score_p3, ...],     Table[0] is scores, initialized to all 0, updated each round to current
   [move_1p1, move_1p2, move_1p3, ...],     Table[n] is moves from turn n (non-zero index)
   [move_2p1, move_2p2, move_2p3, ...],     Table[n][m] references the move from turn n, player m
   [move_3p1, move_3p2, move_3p3, ...],     A new row in Table is added every turn.
   ...]                                     Table[0][n] references the same player as Table[x][n]
                                  
 ```
