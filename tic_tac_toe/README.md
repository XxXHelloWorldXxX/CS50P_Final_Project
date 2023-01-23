Tic Tac Toe

Video Demo: https://youtu.be/7SFa2LxwPy0

Description:
When running the code you first are asked if you want to play with two players, to which you then either reply yes for a two player game or no for a single player game against a bot

Two Player Game:

Player 1 Is X
Player 2 Is O

It's 50/50 which player starts.
You then get printed a Tic Tac Toe field
(A bit bigger than this)
    |
    |
    V
----------
|  |  |  |
----------
|  |  |  |
----------
|  |  |  |
----------

You now get to enter a number from 1 - 9,
to select one of the squares
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------

Then it's the next players turn and this cycle repeats until somebody
got a row or all squares are filled in and it's a tie.


One Player Game:

Player 1 is X
Bot is O

This is pretty much the same as two player. 

The Bot will be going for corner-edges more often than the center, but 
more often for the center than any normal edges (Better squares).
It will first look if it could win in his turn and after that if you the player
could win on your next turn. This I did of course because if the Bot can win in his turn 
then you will never get your turn. After checking for these two cases the bot go 
for a square.


My reason for coding this Tic Tac Toe game was, that I thought that it could be a little challenging but not too much, so that I can show it to my friend (Who just started learning python) and explain to him how it works.

I already at the start decided, that I wanted a one player and two player. I first did the two player part and then went over to the one player. Creating the bot was defenitly the more challenging part. At first I thought of just taking all of the free spaces each turn and just letting the random.choice decide one of the squares, but that would've made the bot utterly terrible and so I created my first own little bot.

After I was "done" with the bot and started a match with him, I actually lost the first round. This not only made me realise that I'm really bad at Tic Tac Toe but also that I want to really start doing some machine learning.

Overall this was a pretty fun project to do. 
I'm very thankfull to the CS50 team for putting together all of these awesome courses (I did the CS50 course prior and plan to do the other ones too).

This was my CS50P final project.