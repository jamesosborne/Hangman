import pygame

#Initaliising Pygame
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Hangman Game")

#Loading Images
images = []
for i in range(7):
    image = pygame.image.load('images\hangman' + str(i) + '.png')
    images.append(image)

#Game variables
hangman_status = 0

#Colours
WHITE = ( 255,255,255)


#Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True


while run:
    clock.tick(FPS)

    win.fill(WHITE)
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()
     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
        
