import pygame

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/images/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = 'down'
        
    def draw(self):
        self.parent_screen.fill((110, 110, 50))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
    def move_left(self):
        self.x -= 10
        self.draw()
        
    def move_right(self):
        self.x += 10
        self.draw()
        
    def move_up(self):
        self.y -= 10
        self.draw()
        
    def move_down(self):
        self.y += 10
        self.draw()
        
    def walk(self):
        pass