import pygame

# Připravíme PyGame
pygame.init()
pygame.display.set_caption(".....")
size = (800, 360)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Připravíme si obrázek
background = (255, 0, 255)
turtle = pygame.image.load("turtle.png")
turtle = pygame.transform.scale(turtle, (0, 0))
rotated_turtle = pygame.transform.rotate(turtle, 0)

WIDTH = 11
HEIGHT = 5

zx = 2
zy = 1

def game_to_screen(x, y):
    return (x * 70, y * 70)

def animate(nx, ny):
    global zx, zy

    duration = 10000
    t = 0
    # Obrazovkové souradnice
    sx, sy = game_to_screen(zx, zy)
    ex, ey = game_to_screen(nx, ny)
    while t < duration:
        # ......
        new = t / duration # 0...1
        old = 1 - new
        x = old * sx + new * ex
        y = old * sy + new * ey
        screen.fill(background)
        draw_grid()
        screen.blit(rotated_turtle, (x, y))
        pygame.display.update()
        t = t + clock.tick()
        
    zx = nx
    zy = ny

def draw_grid():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = (255, 255, 0)
            rect = (x * 70, y * 70, 65, 65)
            pygame.draw.rect(screen, color, rect)

rotated_turtle = pygame.transform.rotate(turtle, 0)
while True: 
  # Vykreslíme
    screen.fill(background)
    draw_grid()
    screen.blit(rotated_turtle, (zx * 70, zy * 70))
    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            rotated_turtle = pygame.transform.rotate(turtle, 270)
            if zx < WIDTH - 1:
               animate(zx + 1, zy)
        elif event.key == pygame.K_UP:
            rotated_turtle = pygame.transform.rotate(turtle, 0)
            if zy > 0:
                animate(zx, zy - 1)
        elif event.key == pygame.K_LEFT:
            rotated_turtle = pygame.transform.rotate(turtle, 90)
            if zx > 0:
                animate(zx - 1, zy)
        elif event.key == pygame.K_DOWN:
            rotated_turtle = pygame.transform.rotate(turtle, 180)
            if zy < HEIGHT - 1:
                animate(zx, zy + 1)
