import pygame
pygame.init()

screen_width, screen_height = 500, 500

screen = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("My first game screen!")

image = pygame.transform.scale(pygame.image.load('jack_fire.png').convert_alpha(),(300, 300))

image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

a = False
while not a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = True
    screen.fill((58, 58, 58))
    screen.blit(image, image_rect)
    pygame.display.flip()
