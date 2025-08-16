import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption("My first game screen")

pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 350 // 2, HEIGHT // 2 - 200 // 2, 350, 200))

a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
    
    font = pygame.font.SysFont("Times New Roman", 36)
    text_color = (100, 100, 100)
    text_surface = font.render("Hello", True, text_color)
    text_rect = text_surface.get_rect()

    screen.blit(text_surface, (40, 40), text_rect)
    pygame.display.update()
