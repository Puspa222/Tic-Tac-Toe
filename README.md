🎮 Tic Tac Toe Game
A simple and fun Tic Tac Toe game developed in Python using the Tkinter module for the GUI.

Table of Contents
Introduction
Features
Installation
Usage
Code Overview
Contributing
License
Introduction
This project is a graphical implementation of the classic Tic Tac Toe game, built to enhance my Python skills and explore GUI development with Tkinter. It's a two-player game where players take turns marking the spaces in a 3×3 grid with "X" or "O".

Features
Interactive GUI using Tkinter
Two-player mode
Real-time updates of the game state
Win and draw detection with alert messages
Installation
To run this game on your local machine, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/tic-tac-toe.git
Navigate to the project directory:
bash
Copy code
cd tic-tac-toe
Run the game:
bash
Copy code
python tic_tac_toe.py
Usage
Starting the game:

Run the tic_tac_toe.py file.
A window will open with a 3x3 grid and a label indicating whose turn it is ("X" or "O").
Playing the game:

Players take turns clicking on the buttons in the grid to place their mark ("X" or "O").
The game will automatically detect a win or a draw and display a message.
Code Overview
Main Components
Initialization:
The main window and frame are set up using Tkinter.
Game State:
xstate and zstate lists keep track of the positions marked by "X" and "O" respectively.
turn variable to keep track of the current player's turn.
Functions:
checkplace(xstate, zstate, p): Returns "X", "O", or "" depending on the state of the position p.
checkwin(state): Checks if the given state has a winning combination.
game_end(winner): Displays the winner or draw message and ends the game.
checkdraw(xstate, zstate): Checks if the game is a draw.
fillboard(p): Updates the game state based on the position clicked and switches turns.
update_board(): Updates the UI to reflect the current game state.
For the complete code, check the tic_tac_toe.py file.

Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
