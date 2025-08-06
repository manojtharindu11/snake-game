from dotenv import load_dotenv
from app.Game import Game

load_dotenv()

if __name__ == "__main__":
    game = Game()
    game.run()