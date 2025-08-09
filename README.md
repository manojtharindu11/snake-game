# Snake Game

A classic Snake game implemented in Python. Eat apples, grow your snake, and avoid crashing into yourself or the walls!

## Features

- Classic snake gameplay
- Score tracking
- Sound effects and background music
- Custom graphics for snake, apple, and background

## Requirements

- Python 3.11 or higher
- See `requirements.txt` for dependencies
- (Optional) `.env` file for environment variables

## Installation

1. Clone this repository or download the source code.
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. (Optional) Copy `.env.example` to `.env` and edit as needed to configure environment variables:

```powershell
copy .env.example .env
# Then edit .env in your text editor
```

## Environment Variables

You can configure game settings using a `.env` file in the project root. An example is provided in `.env.example`.

**Example variables:**

```
SNAKE_SIZE=40
BACKGROUND_COLOR=(110, 110, 50)
SPEED=0.5
WINDOW_WIDTH=1000
WINDOW_HEIGHT=800
```

Add or modify variables as needed for your game.

## How to Run

Run the game using the following command:

```powershell
python main.py
```

Alternatively, you may find a compiled executable `main.exe` for Windows users.

## Project Structure

```
main.py            # Entry point for the game
app/
  Apple.py         # Apple logic
  Game.py          # Game logic
  Snake.py         # Snake logic
resources/
  images/          # Game images (apple, background, block)
  sounds/          # Sound effects and music
requirements.txt   # Python dependencies
.env.example       # Example environment variables
README.md          # Project documentation
```

## Controls

- Arrow keys: Move the snake
- Enter: Restart after game over
- Esc: Quit the game
