# 🎮 Tic Tac Toe Game

A simple and fun Tic Tac Toe game developed in Python using the Tkinter module for the GUI.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a graphical implementation of the classic Tic Tac Toe game, built to enhance my Python skills and explore GUI development with Tkinter. It's a two-player game where players take turns marking the spaces in a 3×3 grid with "X" or "O".

## Features

- Interactive GUI using Tkinter
- Two-player mode
- Real-time updates of the game state
- Win and draw detection with alert messages

## Installation

To run this game on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/tic-tac-toe.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd tic-tac-toe
    ```
3. **Run the game:**
    ```bash
    python tic_tac_toe.py
    ```

## Usage

1. **Starting the game:**
   - Run the `tic_tac_toe.py` file.
   - A window will open with a 3x3 grid and a label indicating whose turn it is ("X" or "O").

2. **Playing the game:**
   - Players take turns clicking on the buttons in the grid to place their mark ("X" or "O").
   - The game will automatically detect a win or a draw and display a message.

## Code Overview

### Main Components

- **Initialization:**
  - The main window and frame are set up using Tkinter.
  
- **Game State:**
  - `xstate` and `zstate` lists keep track of the positions marked by "X" and "O" respectively.
  - `turn` variable to keep track of the current player's turn.
  
- **Functions:**
  - `checkplace(xstate, zstate, p)`: Returns "X", "O", or "" depending on the state of the position `p`.
  - `checkwin(state)`: Checks if the given state has a winning combination.
  - `game_end(winner)`: Displays the winner or draw message and ends the game.
  - `checkdraw(xstate, zstate)`: Checks if the game is a draw.
  - `fillboard(p)`: Updates the game state based on the position clicked and switches turns.
  - `update_board()`: Updates the UI to reflect the current game state.

For the complete code, check the [tic_tac_toe.py](tic_tac_toe.py) file.

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
