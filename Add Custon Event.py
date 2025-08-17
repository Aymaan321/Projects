import pygame
import random

pygame.init()

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Addition and Color Change")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color

    def new_color(self):
        self.image.fill(random.choice((white, red, green, blue)))


sprite1 = MySprite(red, 50, 50, 100, 100)
sprite2 = MySprite(blue, 50, 50, 200, 150)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Post the color change event
                pygame.event.post(pygame.event.Event(COLOR_CHANGE_EVENT))
        if event.type == COLOR_CHANGE_EVENT:
            # Change the color of the sprites
            sprite1.new_color()
            sprite2.new_color()


    screen.fill((0, 0, 0)) 
    all_sprites.draw(screen)  
    pygame.display.flip()  

    clock.tick(60)

pygame.quit()