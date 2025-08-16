import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Control Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

rect_width, rect_height = 60, 40
sp1 = pygame.Rect(100, 100, rect_width, rect_height)  
sp2 = pygame.Rect(400, 300, rect_width, rect_height)   

speed = 1

clock = pygame.time.Clock()
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.x -= speed
    if keys[pygame.K_RIGHT]:
        sp1.x += speed
    if keys[pygame.K_UP]:
        sp1.y -= speed
    if keys[pygame.K_DOWN]:
        sp1.y += speed

    sp1.x = max(0, min(WIDTH - rect_width, sp1.x))
    sp1.y = max(0, min(HEIGHT - rect_height, sp1.y))

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, sp1)  
    pygame.draw.rect(screen, RED, sp2)    
    
    pygame.display.flip()

pygame.quit()