import pygame, random, sys, os, time

from pygame.locals import *

WINDOWWIDTH = 800

WINDOWHEIGHT = 600

TEXTCOLOR = (255, 255, 20)

BACKGROUNDCOLOR = (100,100,100)


MOMOMANMINSIZE = 500

MOMOMANMAXSIZE = 500

MOMOMANMINSPEED = 8

MOMOMANMAXSPEED = 10

ADDNEWMOMOMANRATE = 6

PLAYERMOVERATE = 6

count = 3
topScore=0

def terminate():
    pygame.quit()

def waitForPlayerToPressKey():

    while True:

        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:

                    terminate()

                return

def playerHasHitMomoman(playerRect, momomans):

    for b in momomans:

        if playerRect.colliderect(b['rect']):

            return True

    return False

def drawText(text, font, surface, x, y):

    textobj = font.render(text, 1 , TEXTCOLOR)

    textrect = textobj.get_rect()

    textrect.topleft = (x, y)

    surface.blit(textobj, textrect)

pygame.init()

mainClock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('momo escape race')


momoImage = pygame.image.load('momo.png')

man1 = pygame.image.load('man1.png')

man2 = pygame.image.load('man2.png')

man3 = pygame.image.load('man3.png')

playerRect = momoImage.get_rect()

sample = [man1 , man2, man3 ]

wallLeft = pygame.image.load('left.png')

wallRight = pygame.image.load('right.png')

font = pygame.font.SysFont(None, 42)

drawText('PRESS ANY KEY TO START THE GAME!', font , windowSurface , (WINDOWWIDTH / 3) - 137, (WINDOWHEIGHT / 3)+80)

pygame.display.update()

waitForPlayerToPressKey()

zero = 0

while (count > 0):

    momomans = []

    score = 0

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)

    moveLeft = moveRight = moveUp = moveDown = False

    slowCheat = False

    momomanAddCounter = 0

    while True:

        score += 1

        for event in pygame.event.get():

            if event.type == QUIT:

                terminate()

            if event.type == KEYDOWN:

                if event.key == K_LEFT or event.key == ord('a'):


                    moveRight = False

                    moveLeft = True

                if event.key == K_RIGHT or event.key == ord('d'):

                    moveLeft = False

                    moveRight = True

                if event.key == K_UP or event.key == ord('w'):

                    moveDown = False

                    moveUp = True

                if event.key == K_DOWN or event.key == ord('s'):

                    moveUp = False

                    moveDown = True

            if event.type == KEYUP:


                if event.key == K_ESCAPE:

                    terminate()

                if event.key == K_LEFT or event.key == ord('a'):

                    moveLeft = False

                if event.key == K_RIGHT or event.key == ord('d'):

                    moveRight = False

                if event.key == K_UP or event.key == ord('w'):

                    moveUp = False

                if event.key == K_DOWN or event.key == ord('s'):

                    moveDown = False

        if not slowCheat :

            momomanAddCounter += 1

        if momomanAddCounter == ADDNEWMOMOMANRATE:

            momomanAddCounter = 0

            momomanSize = 30

            newMomoman = {'rect': pygame.Rect(random.randint(140, 485), 0 - momomanSize, 23, 47),

                         'speed': random.randint(MOMOMANMINSPEED, MOMOMANMAXSPEED),

                         'surface': pygame.transform.scale(random.choice(sample), (23, 47)),

                         }

            momomans.append(newMomoman)

            sideLeft = {'rect': pygame.Rect(0, 0, 125 , 600),

                        'speed': random.randint(MOMOMANMINSPEED, MOMOMANMAXSPEED),

                        'surface': pygame.transform.scale(wallLeft, (126, 599)),

                        }

            momomans.append(sideLeft)

            sideRight = {'rect': pygame.Rect(510 ,0,0, 600),

                         'speed': random.randint(MOMOMANMINSPEED, MOMOMANMAXSPEED),

                         'surface': pygame.transform.scale(wallRight, (303, 599)),

                         }

            momomans.append(sideRight)

        if moveLeft and playerRect.left > 0:

            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)

        if moveRight and playerRect.right < WINDOWWIDTH:

            playerRect.move_ip(PLAYERMOVERATE, 0)

        if moveUp and playerRect.top > 0:

            playerRect.move_ip(0, -1 * PLAYERMOVERATE)

        if moveDown and playerRect.bottom < WINDOWHEIGHT:

            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in momomans:

                b['rect'].move_ip(0, b['speed'])

        for b in momomans[:]:

            if b['rect'].top > WINDOWHEIGHT:

                momomans.remove(b)

        font = pygame.font.SysFont(None, 40)

        windowSurface.fill(BACKGROUNDCOLOR)

        drawText('Score: %s' % (score), font, windowSurface, 128, 0)

        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 21)

        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 41)

        windowSurface.blit(momoImage, playerRect)

        for b in momomans:

            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        if playerHasHitMomoman(playerRect, momomans):

            if score > topScore:

                topScore = score

            break

    count = count - 1

    time.sleep(1)

    font = pygame.font.SysFont(None, 52)

    if (count == 0):

        drawText('Game Over', font, windowSurface, (WINDOWWIDTH / 3)+40, (WINDOWHEIGHT / 3)+70)

        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH /3) - 110, (WINDOWHEIGHT / 3) + 95)

        pygame.display.update()

        waitForPlayerToPressKey()

        count = 3