import pygame
import random
from .Object import Object

class Apple(Object):
    def __init__(self, parent_screen):
        super().__init__()
        self.image = pygame.image.load("resources/images/apple.jpg")
        self.parent_screen = parent_screen
        self.x = self.SIZE * 3
        self.y = self.SIZE * 3
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(0, self.WINDOW_WIDTH / self.SIZE - 1) * self.SIZE
        self.y = random.randint(0, self.WINDOW_HEIGHT / self.SIZE - 1) * self.SIZE