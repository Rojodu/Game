import pygame
import pygame.image as img
pygame.init()


screenSize = 500
win = pygame.display.set_mode((screenSize, screenSize-20))

pygame.display.set_caption("First Game")

walkRight = [img.load('R1.png'), img.load('R2.png'), img.load('R3.png'),img.load('R4.png'), img.load('R5.png'), img.load('R6.png'),img.load('R7.png'), img.load('R8.png'), img.load('R9.png')]
walkLeftt = [img.load('L1.png'), img.load('L2.png'), img.load('L3.png'),img.load('L4.png'), img.load('L5.png'), img.load('L6.png'),img.load('L7.png'), img.load('L8.png'), img.load('L9.png')]
bg = img.load('bg.jpg')
char = img.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    
    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        win.blit(walkLeftt[walkCount//3], (x,y))
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    else:
        win.blit(char, (x,y))

    pygame.display.update()


# main loop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenSize - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
pygame.quit()