import pygame


pygame.init()


window = pygame.display.set_mode((480, 720))

pygame.display.set_caption("First Window")


x = 100
y = 100
width = 60
height = 100
vel = 5

running = True

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 480 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 720 - height - vel:
        y += vel
    window.fill((0,0,0))
    pygame.draw.rect(window, (100, 255, 0), (x, y, width, height))
    pygame.display.update()
            
