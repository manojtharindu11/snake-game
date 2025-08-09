import pygame
import time
from pygame.locals import *
from .Snake import Snake
from .Apple import Apple
from .Object import Object

class Game(Object):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption("Snake and Apple Game")
        
        pygame.mixer.init()
        self.play_background_music()
        
        self.surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.surface.fill(self.BACKGROUND_COLOR)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        # snake collide with an apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()
            
        # snake colliding with it self
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game over"
            
        # snake colliding with boundaries
        # for i in range(0, self.WINDOW_WIDTH + 1):
        #     for j in range(0, self.WINDOW_HEIGHT + 1):
                
        #         if i == 0 or i == self.WINDOW_WIDTH:
        #             print(f"({i},{j})")
                    
        #         elif j == 0 or j == self.WINDOW_HEIGHT:
        #             print(f"({i},{j})")
        
            
    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (self.WINDOW_WIDTH * 0.8, self.WINDOW_HEIGHT * 0.0125))
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + self.SIZE:
            if y1 >= y2 and y1 <= y2 + self.SIZE:
                return True
        return False
    
    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/sounds/{sound}.mp3")
        pygame.mixer.Sound.play(sound)
        
    def play_background_music(self):
        pygame.mixer.music.load("resources/sounds/bg_music.mp3")
        pygame.mixer.music.play()
        
    def render_background(self):
        bg = pygame.image.load("resources/images/background.jpg")
        self.surface.blit(bg, (0, 0))
    
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (self.WINDOW_WIDTH * 0.2, self.WINDOW_HEIGHT * 0.375))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (self.WINDOW_WIDTH * 0.2, self.WINDOW_HEIGHT * 7 / 16))
        
        pygame.display.flip()
        pygame.mixer.music.pause()
        
        
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
                        pygame.mixer.music.unpause()
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
                   
            time.sleep(self.SPEED)