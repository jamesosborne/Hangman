import pygame

#Initaliising Pygame
pygame.init()
WIDTH = 800
HEIGHT = 500
pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Hangman Game")

FPS = 60
clock = pygame.time.Clock()
run = True

#Game Loop
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
        
