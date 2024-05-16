import pygame

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Flappy Bird')  # Sửa lỗi nhỏ ở đây
running = True
GREEN = (0, 200, 0)
RED=(255,0,0)
clock = pygame.time.Clock()
rect_x = 100
rect_y = 200

while running:
    clock.tick(60)
    screen.fill(GREEN)

    rect_x += 1
    rect_y += 1
    pygame.draw.rect(screen,RED,(100, 200, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
