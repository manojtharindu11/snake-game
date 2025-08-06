import pygame
import os

class Snake:
    def __init__(self, parent_screen, length):
        self.SIZE = int(os.getenv("SNAKE_SIZE", 40))
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/images/block.jpg").convert()
        self.x = [self.SIZE] * length
        self.y = [self.SIZE] * length
        self.direction = 'down'
        
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        
    def draw(self):
        self.parent_screen.fill((110, 110, 50))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
        
    def move_left(self):
        self.direction = "left"
        
    def move_right(self):
        self.direction = "right"
        
    def move_up(self):
        self.direction = "up"
        
    def move_down(self):
        self.direction = "down"
        
    def walk(self):
        
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        
        if self.direction == "left":
            self.x[0] -= self.SIZE
        if self.direction == "right":
            self.x[0] += self.SIZE
        if self.direction == "up":
            self.y[0] -= self.SIZE
        if self.direction == "down":
            self.y[0] += self.SIZE
            
        self.draw()