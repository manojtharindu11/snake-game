import os
from abc import ABC

class Object(ABC):
    def __init__(self):
        self.SIZE = int(os.getenv("SNAKE_SIZE", 40))
        self.SPEED = float(os.getenv("SPEED", 0.3))
        self.BACKGROUND_COLOR = eval(os.getenv("BACKGROUND_COLOR","(110, 110, 50)"))
        self.WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", 1000))
        self.WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", 800))