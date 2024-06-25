import os
print("Welcome to the Tic Tac Toe Game!\nRules: Player 1 and player 2, represented by X and O, take turns marking the spaces in a 3*3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins.\n")
game_setting = input("You could choose to play against the computer or against another player: ")
# Function to print Tic Tac Toe
def draw_board(spots):
    board = (f"\n"
             f"  |   |\n"
             f"{spots[1]} | {spots[2]} | {spots[3]}\n"
             f"__|___|__\n"
             f"  |   | \n"
             f"{spots[4]} | {spots[5]} | {spots[6]}\n"
             f"__|___|__\n"
             f"  |   | \n"
             f"{spots[7]} | {spots[8]} | {spots[9]}\n"
             f"  |   | \n"
             f"\n")
    print(board)
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
    players = list(score_board.keys())
    print("\t   ", player1 , "\t    ", score_board[player1])
    print("\t   ", player2 , "\t    ", score_board[player2])
    print("\t--------------------------------\n")
# Function to check if any player has won
def  check_win(dict):
    if(spots[1] == spots[2] == spots[3]) or (spots[4] == spots[5] == spots[6]) or (spots[7] == spots[8] == spots[9]) or (spots[1] == spots[4] == spots[7]) or (spots[2] == spots[5] == spots[8]) or (spots[3] == spots[6] == spots[9]) or (spots[9] == spots[5] == spots[1] or (spots[7] == spots[5] == spots[3])):
        return True
    else:
        return False
# Function to switch player moves
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
# Declare all the variables we're going to need
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5' , 6 : '6', 7 : '7',  8 : '8', 9 : '9'}
playing, complete = True, False
turn = 0
prev_turn = -1

if game_setting == "computer":
    player1 = input("please enter your name: ")
else:
    player1 = input("please enter player 1 name: ")
    player2 = input("please enter player 2 name: ")
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
    while playing: # Game Loop with another player
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots) # Draw the current Game Board
        if prev_turn == turn: # If an invalid turn occurred, let the player know
            print("Invalid spot selected, please pick another.")
        prev_turn = turn
        print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit: ")
        choice = input() # Get input and make sure it's valid
        if choice == 'q': # The game has ended,
            playing = False
        elif str.isdigit(choice) and int(choice) in spots:
            if not spots[int(choice)] in {"X", "O"}:   # Check if the spot is already taken.
                turn += 1  # If not, update board and increment the turn
                spots[int(choice)] = check_turn(turn)
        if check_win(spots):
            playing, complete = False, True    # Check if the game has ended (and if someone won)
        if turn > 8: playing = False
        player1 = player1
        player2 = player2
        draw_board(spots)
        if complete:   # If there was a winner, say who won
            if check_turn(turn) == 'X':
                player_won = player1
                print(f"{player_won} Wins!")
            else:
                player_won = player2
                print(f"{player_won} Wins!")
            score_board[player_won] = score_board[player_won] + 1
            print_scoreboard(score_board)

        else:
            # Tie Game
            print("Game Draw")
            score_board = {player1: 0, player2: 0}
            print_scoreboard(score_board)
        print("Thanks for playing!")
#count = 0
#           for i in values.values():
#              if i == 'X':
#                 count += 1
#              elif i == 'O':
#                   count += 1
#           if count == 9:
#               # Tie Game
#               print("Game Draw")
#               score_board = {player1: 0, player2: 0}
#               print_scoreboard(score_board)
#               print("Thanks for playing!")
#               break
#print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")
