import pygame
import time
from pygame.locals import *
from .Snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((110, 110, 50))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()

    def run(self):
        running = True
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        running = False
                    
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()
                        
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        
                elif event.type == QUIT:
                    running = False
                    
            self.snake.walk()
            time.sleep(0.2)