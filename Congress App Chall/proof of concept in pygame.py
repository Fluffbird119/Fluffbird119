# proof of concept in pygame
import pygame

screen_size_x = 800
screen_size_y = 600

pygame.init()
screen = pygame.display.set_mode((screen_size_x,screen_size_y))
pygame.display.set_caption("POC")

run = True
box = "red"

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            box = "green"
        if event.type == pygame.MOUSEBUTTONUP:
            box = 'blue'
    
    pygame.draw.rect(screen, box, pygame.Rect(50,45,400,35))

    pygame.display.flip()