# Function to print Tic Tac Toe
def draw_board(values):
    board = (f"\n"
             f"  |   |\n"
             f"{values[1]} | {values[2]} | {values[3]}\n"
             f"__|___|__\n"
             f"  |   | \n"
             f"{values[4]} | {values[5]} | {values[6]}\n"
             f"__|___|__\n"
             f"  |   | \n"
             f"{values[7]} | {values[8]} | {values[9]}\n"
             f"  |   | \n"
             f"\n")
    print(board)
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
    player = list(score_board.keys())
    print("\t   ", player[0] , "\t    ", score_board[player[0]])
    print("\t   ", player[1] , "\t    ", score_board[player[1]])
    print("\t--------------------------------\n")
# Function to check if any player has won
def  check_win(dict):
    if(values[1] == values[2] == values[3]) or (values[4] == values[5] == values[6]) or (values[7] == values[8] == values[9]) or (values[1] == values[4] == values[7]) or (values[2] == values[5] == values[8]) or (values[3] == values[6] == values[9]) or (values[9] == values[5] == values[1] or (values[7] == values[5] == values[3])):
        return True
    else:
        return False
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False
# Function to switch player moves
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
# Declare all the variables we're going to need
player_pos = {'X':[], 'O':[]} # Stores the positions occupied by X and O
print("Welcome to the Tic Tac Toe Game!\nRules: Player 1 and player 2, represented by X and O,\ntake turns marking the spaces in a 3*3 grid.\nThe player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins.\n")
score_board = {'player1': 0, 'player2': 0} # Stores the scoreboard
print_scoreboard(score_board)
complete = False
turn = 0
prev_turn = -1
play_again = "yes"
while play_again == "yes":
    game_setting = input("You could choose to play against the computer or against another player: ").lower()
    values = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    draw_board(values)
    if game_setting == "computer":
        player1 = str(input("please enter your name: "))
        player2 = "Computer"
        print_scoreboard(score_board)
    else:
        player1 = str(input("please enter player 1 name: "))
        player2 = str(input("please enter player 2 name: "))
        # Stores the player who chooses X and O
        cur_player = player1
        while True: # Game Loop with another player
            draw_board(values) # Draw the current Game Board
            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ", end="")
                move = int(input())
            except ValueError:
                print("Wrong Input!!! Try Again")
                continue
            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print("Wrong Input!!! Try Again")
                continue
            # Check if the box is not occupied already
            if values[move - 1] != ' ':
                print("Invalid spot selected, please pick another.")
                continue
            # Update game information
            # Updating grid status
            values[move - 1] = cur_player
            # Updating player positions
            player_pos[cur_player].append(move)
            # Function call for checking draw game
            if check_draw(player_pos):
                draw_board(values)
                print("Game Drawn")
                print("\n")

            # Switch player moves
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'
            # Stores the player who chooses X and O
            cur_player = player1
            # Stores the choice of players
            player_choice = {'X': "", 'O': ""}
            # Stores the options
            options = ['X', 'O']
            # Stores the scoreboard
            score_board = {player1: 0, player2: 0}
            print_scoreboard(score_board)
            # Game Loop for a series of Tic Tac Toe
            while True:
                # Player choice Menu
                print("Turn to choose for", cur_player)
                print("Enter 1 for X")
                print("Enter 2 for O")
                print("Enter 3 to Quit")
                # Try exception for CHOICE input
                try:
                    choice = int(input()) # Get input and make sure it's valid
                except ValueError:
                    print("Invalid spot selected\n")
                    continue
                    # Conditions for player choice
                    if choice == 1:
                        player_choice['X'] = cur_player
                        if cur_player == player1:
                            player_choice['O'] = player2
                        else:
                            player_choice['O'] = player1

                    elif choice == 2:
                        player_choice['O'] = cur_player
                        if cur_player == player1:
                            player_choice['X'] = player2
                        else:
                            player_choice['X'] = player1

                    elif choice == 3:
                        print("Final Scores")
                        print_scoreboard(score_board)
                        break

                    else:
                        print("Wrong Choice!!!! Try Again\n")
            if check_win(values):
                complete =  True    # Check if the game has ended (and if someone won)
            if complete:   # If there was a winner, say who won
                if check_turn(turn) == 'X':
                    print(player1 ," Wins!")
                    player_won = player1
                else:
                    print(player2 ," Wins!")
                    player_won = player2
                score_board[player_won] +=  1
                print_scoreboard(score_board)
                print("Thanks for playing!")
                break
            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1
    play_again = input("Do you want to play again? (Yes/No): ")
print("Thanks for playing!\nEnd Game!")