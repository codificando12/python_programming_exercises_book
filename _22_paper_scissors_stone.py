"""Exercise Description

Write a rpsWinner() function with parameters player1 and player2. These parameters are passed one of the strings 'rock', 'paper', or 'scissors' 
representing that player’s move. If this results in player 1 winning, the function returns 'player one'. If this results in player 2 winning, the function returns 
'player two'. Otherwise, the function returns 'tie'.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. 
Your solution is correct if the following assert statements’ conditions are all True:

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: Boolean operators, elif statements"""

def rpsWinner(player_1, player_2):

    if player_1 == player_2:
        return 'tie'
    elif player_1 == 'paper' and player_2 == 'scissors':
        return 'player two'
    elif player_1 == 'scissors' and player_2 == 'rock':
        return 'player two'
    elif player_1 == 'rock' and player_2 == 'paper':
        return 'player two'
    else:
        return 'player one'
    
assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'