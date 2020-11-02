import pygame

#Initaliising Pygame
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Hangman Game")

#Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH -(RADIUS *2 + GAP)* 13)/2)
starty = 400

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i%13))
    y = starty + ((i // 13)*(GAP + RADIUS * 2))
    letters.append([x, y])
 
#Loading Images
images = []
for i in range(7):
    image = pygame.image.load('images\hangman' + str(i) + '.png')
    images.append(image)

#Game variables
hangman_status = 0

#Colours
WHITE = ( 255,255,255)
BLACK = (0,0,0)


#Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():  
    win.fill(WHITE)

    #Drawing letters
    for letter in letters:
        x, y = letter
        pygame.draw.circle(win, BLACK,(x, y), RADIUS, 3)
    
    
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()
     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
        
