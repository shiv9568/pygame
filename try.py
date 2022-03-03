import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('space invaders')
icon = pygame.image.load('Cartoon_space_rocket.png')
pygame.display.set_icon(icon)

running = True
while running:
  for event in pygame.event.get() :
    if event.type == pygame.QUIT   :
      running = False
  screen.fill((255,0,0))
  pygame.display.update()
