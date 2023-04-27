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

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            win.blit(walkLeftt[self.walkCount//3], (self.x,self.y))
            self.walkCount+=1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount+=1
        else:
            win.blit(char, (self.x,self.y))

def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()


# main loop
man = player(300,410,64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screenSize - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
pygame.quit()