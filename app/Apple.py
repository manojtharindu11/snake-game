import pygame
import os
import random

class Apple:
    def __init__(self, parent_screen):
        self.SIZE = int(os.getenv("SNAKE_SIZE", 40))
        self.image = pygame.image.load("resources/images/apple.jpg")
        self.parent_screen = parent_screen
        self.x = self.SIZE * 3
        self.y = self.SIZE * 3
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(0, 24) * self.SIZE
        self.y = random.randint(0, 19) * self.SIZE