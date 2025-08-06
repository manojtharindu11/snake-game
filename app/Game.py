import pygame
import time
import os
from pygame.locals import *
from .Snake import Snake
from .Apple import Apple

class Game:
    def __init__(self):
        self.SIZE = int(os.getenv("SNAKE_SIZE", 40))
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((110, 110, 50))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            
    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 10))
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + self.SIZE:
            if y1 >= y2 and y1 <= y2 + self.SIZE:
                return True
        return False
        

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
            
            self.play()        
            time.sleep(0.3)