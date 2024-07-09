# Trevor Loth
# 7-8-24

import pygame
import time
from sys import exit

# Surfaces display visual information, Rectangles store computational information, Sprite class mixes these two
# Rectangles can be used for collisions, positioning, and sometimes drawing via pygame.draw
# _s means surface
# _r means rectangle

display = (800, 600)
pygame.init()                                               # Initializes the game
screen = pygame.display.set_mode(display)                   # Creates a display window which is assigned to variable screen
pygame.display.set_caption("FishingGame Demo")                   # Set the window title to the given string
clock = pygame.time.Clock()                                 # Create a variable clock to keep track of game time
          
# ==========================================================================

gameOver= False
catchRange = (160, 180)
meterRange = (0, 300)
meterDimensions = (30, 300)
mouseButtonDown = False
xoffset = 600
yoffset = abs(display[1]/2 - meterDimensions[1]/2)


low     = (catchRange[0]-meterRange[0])/2 + yoffset #50
high    = (catchRange[1]+meterRange[1])/2 + yoffset #275
midlow  = catchRange[0] + yoffset
midhigh = catchRange[1] + yoffset
middle = (meterRange[1]-meterRange[0])/2

catchMeter = (midhigh+midlow)/2-yoffset
caughtThreshold = 300
catchFactor = caughtThreshold/2

# ==========================================================================

idle_bg = pygame.image.load("FishingGame-BG-idle.png").convert()
pull_bg = pygame.image.load("FishingGame-BG-pull.png").convert()
fish_bg = pygame.image.load("FishingGame-BG-fish.png").convert()


test_font = pygame.font.Font("PixelType.ttf", 50)                  # defines font using Font(type, size)
wintext_s = test_font.render("YOU WIN!", False, "Black")
losetext_s = test_font.render("You Lose", False, "Black")

black_s = pygame.Surface((meterDimensions[0]+10, meterDimensions[1]+10))
black_s.fill("Black")
black_r = black_s.get_rect(center = (xoffset, display[1]/2))

red_s = pygame.Surface((meterDimensions[0], meterDimensions[1]))
red_s.fill("Red")
red_r = red_s.get_rect(center = (xoffset, display[1]/2))

orange_s = pygame.Surface((meterDimensions[0], (midhigh - midlow)+50))
orange_s.fill("Orange")         
orange_r = orange_s.get_rect(center = (xoffset, (midhigh+midlow)/2))

green_s = pygame.Surface((meterDimensions[0], midhigh - midlow))
green_s.fill("Green")           
green_r = green_s.get_rect(center = (xoffset, (midhigh+midlow)/2))


lineDisplay_s = pygame.Surface((200, 5))
lineDisplay_s.fill("White")           

# ==========================================================================

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        # Looks for the quit event, closes the game if found
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonDown = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            mouseButtonDown = False
      
# ==========================================================================
    if not gameOver:
        if mouseButtonDown: screen.blit(pull_bg, (0, 0))
        else:               screen.blit(idle_bg, (0, 0))
    
        screen.blit(black_s, black_r)
        screen.blit(red_s, red_r)
        screen.blit(orange_s, orange_r)
        screen.blit(green_s, green_r)
        
        lineDisplay_r = lineDisplay_s.get_rect(center = (xoffset, catchMeter+yoffset))
        screen.blit(lineDisplay_s, lineDisplay_r)
    
# ==========================================================================

        if not catchMeter+yoffset >= meterRange[1]+yoffset:
            if mouseButtonDown:
                catchMeter += 1.5
        if not catchMeter+yoffset <= meterRange[0]+yoffset:
            if not mouseButtonDown:
                catchMeter -= 1.5
                
        if lineDisplay_r.colliderect(green_r):
            print("green")
            catchFactor += 1
        elif lineDisplay_r.colliderect(orange_r):
            print("orange")
            catchFactor -= 1
        elif lineDisplay_r.colliderect(red_r):
            print("red")
            catchFactor -= 3
        else:
            RuntimeError("LineDisplay is misplaced")
                
    
    
    # if catchMeter+yoffset <=  low or catchMeter+yoffset >= high:            # compare the meter to the lowest and highest thresholds, if it is past these
    #     if catchFactor > 0:# catchFactor -= 3
    #         print("red")
    # elif catchMeter+yoffset >= midlow and catchMeter+yoffset <= midhigh:    # compare the meter to the catch thresholds, add to caught value if inside
    #     if catchFactor < caughtThreshold:# catchFactor += 1
    #         print("green")
    # else:                                                   # if not in the catch range but neither in the critical range, subtract only 1
    #     if catchFactor > 0:# catchFactor -= 1
    #         print("orange")
    
    print(catchFactor)
    
    if catchFactor >= caughtThreshold:
        gameOver = True
        print("YOU WIN")
        screen.blit(fish_bg, (0, 0))
        screen.blit(wintext_s, (display[0]/2, display[1]/4))
    
    if catchFactor <= 0:
        gameOver = True
        print("YOU LOSE")
        screen.blit(losetext_s, (display[0]/2, display[1]/4))
        pygame.quit()
        exit()

        
# ==========================================================================

    pygame.display.update()
    clock.tick(60)                                          # limit ticks to 60 (ie. Cap the framerate to 60fps)










