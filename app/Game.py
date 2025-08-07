import pygame
import time
import os
from pygame.locals import *
from .Snake import Snake
from .Apple import Apple

class Game:
    def __init__(self):
        self.SIZE = int(os.getenv("SNAKE_SIZE", 40))
        self.BACKGROUND_COLOR = eval(os.getenv("BACKGROUND_COLOR","(110, 110, 50)"))
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill(self.BACKGROUND_COLOR)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        # snake collide with an apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            
        # snake colliding with it self
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"
    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 10))
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + self.SIZE:
            if y1 >= y2 and y1 <= y2 + self.SIZE:
                return True
        return False
    
    def show_game_over(self):
        self.surface.fill(self.BACKGROUND_COLOR)
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()
        
    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        running = False
                        
                    if event.key == K_RETURN:
                        pause = False
                    
                    if not pause:
                    
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
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
                   
            time.sleep(0.3)