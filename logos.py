import pygame, random
from shcts import *

pygame.init()

images = [pygame.image.load('content\\.PNG\\C_ICON.png'),
        pygame.image.load('content\\.PNG\\C#_icon.png'),
        pygame.image.load('content\\.PNG\\C++_ICON.png'),
        pygame.image.load('content\\.PNG\\CSS.png'),
        pygame.image.load('content\\.PNG\\HTML5.png'),
        pygame.image.load('content\\.PNG\\JS.png'),
        pygame.image.load('content\\.PNG\\python_icon.png')]

names = ['C', 'C#', 'C++', 'CSS', 'HTML5', 'JavaScript', 'Python']

n = random.randint(0, 6)

python_logo = pygame.image.load('content\.PNG\python_icon.png')
logo = images[n]
width, height = 800, 500
wn = pygame.display.set_mode((width, height))
title = pygame.display.set_caption(names[n] + " Logo Bouncing")
clock = pygame.time.Clock()

py_width = logo.get_width()
py_height = logo.get_height()
x = random.randint(0 + py_width, 800 - py_width)
y = random.randint(0 + py_height, 500 - py_height)
vx = 6
vy = 6

r = random.randint(1, 225)
g = random.randint(1, 225)
b = random.randint(1, 225)
bg = (r, g, b)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    wn.fill(bg)

    score = text()

    score.write(font='poppins', size=100, text=str(names[n]), 
                color=(r - 30, g - 30, b - 30), surface=wn, x=400, y=250)

    wn.blit(logo, ((x, y)))

    icon = pygame.display.set_icon(logo)
    title = pygame.display.set_caption(names[n] + " Logo Bouncing")

    if x >= 800 - py_width or x <= 0:
        r = random.randint(30, 225)
        g = random.randint(30, 225)
        b = random.randint(30, 225)
        vx *= -1
        bg = (r, g, b)
        n = random.randint(0, 6)
        logo = images[n]

    if y <= 0 or y >= 500 - py_height:
        r = random.randint(30, 225)
        g = random.randint(30, 225)
        b = random.randint(30, 225)
        vy *= -1
        bg = (r, g, b)
        n = random.randint(0, 6)
        logo = images[n]

    x += vx
    y += vy

    pygame.display.update()
    clock.tick(60)
pygame.quit()

