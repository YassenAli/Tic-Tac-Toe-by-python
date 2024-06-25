# Tic Tac Toe Game

This repository contains two versions of the Tic Tac Toe game implemented in Python. Each version allows players to compete against each other or against a computer AI.

## Tic Tac Toe Game.py

### Description
This version of the Tic Tac Toe game allows players to choose between playing against another player or against the computer. The game features a 3x3 grid where players take turns marking their chosen spot with 'X' or 'O'. The first player to align three of their marks horizontally, vertically, or diagonally wins the game.

### Features
- Player vs Player (PvP) mode.
- Player vs Computer (PvC) mode.
- Scoreboard to track wins for each player.
- Interactive console interface.

### How to Play
1. Run the `Tic Tac Toe Game.py` script.
2. Choose between playing against the computer or another player.
3. Follow the on-screen prompts to make your move by entering the position number where you want to place your mark ('X' or 'O').
4. The game ends when one player achieves three marks in a row or when all spots are filled without a winner.
5. The scoreboard updates after each game. Players can choose to play again.

### Example Gameplay
```plaintext
Welcome to the Tic Tac Toe Game!
Rules: Player 1 and player 2, represented by X and O,
take turns marking the spaces in a 3*3 grid.
The player who succeeds in placing three of their marks in a
horizontal, vertical, or diagonal row wins.

You could choose to play against the computer or against another player: player
please enter player 1 name: Alice
please enter player 2 name: Bob

   SCOREBOARD       
--------------------------------
    Alice          0
    Bob            0
--------------------------------

  |   |
1 | 2 | 3
__|___|__
  |   | 
4 | 5 | 6
__|___|__
  |   | 
7 | 8 | 9
  |   | 

Player Alice's turn. Which box? : 1
...
```

## XO Game.py

### Description
This version of the Tic Tac Toe game also offers PvP and PvC modes. It features a similar gameplay experience to Tic Tac Toe Game.py but with a different implementation structure.

### Features
- Player vs Player (PvP) mode.
- Player vs Computer (PvC) mode.
- Clear screen functionality for enhanced user experience.
- Updated score tracking and win detection.

### How to Play
1. Run the XO Game.py script.
2. Choose between playing against the computer or another player.
3. Enter your move by typing the position number (1-9) where you want to place your mark ('X' or 'O').
4. The game ends when one player achieves three marks in a row or when all spots are filled without a winner.
5. The scoreboard updates after each game. Players can choose to play again.

### Example Gameplay
```plaintext
Welcome to the Tic Tac Toe Game!
Rules: Player 1 and player 2, represented by X and O,
take turns marking the spaces in a 3*3 grid.
The player who succeeds in placing three of their marks in a
horizontal, vertical, or diagonal row wins.

You could choose to play against the computer or against another player: computer
please enter your name: Alice

   SCOREBOARD       
--------------------------------
    Alice          0
    Computer       0
--------------------------------

  |   |
1 | 2 | 3
__|___|__
  |   | 
4 | 5 | 6
__|___|__
  |   | 
7 | 8 | 9
  |   | 

Player Alice's turn. Pick your spot or press q to quit: 1
...
```

## Repository Structure

#### The repository structure includes:

- `Tic Tac Toe Game.py`: Implementation of the Tic Tac Toe game.
- `XO Game.py`: Alternative implementation of the Tic Tac Toe game.
- `README.md`: This file, providing instructions and information about the game.

## Getting Started

#### To play the game:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the directory containing the game script you want to play (Tic Tac Toe Game.py or XO Game.py).
4. Run the script using Python (python Tic Tac Toe Game.py or python XO Game.py).
5. Follow the on-screen instructions to start playing.

## Acknowledgements
- Developed by [Yassin Ali].
- Inspired by classic board games and Python programming challenges.
