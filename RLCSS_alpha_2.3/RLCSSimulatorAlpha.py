#Import pygame & other functions
from pickletools import string4
import pygame, sys
import buttonClass
import playerClass

#Setup pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("RLCS Simulator Alpha")
WIN_WIDTH = 1280
WIN_HEIGHT = 720
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#Set up the basic text font
basicFont = pygame.font.SysFont(None,64)
smallFont = pygame.font.SysFont(None,32) #Fits about 150 characters per line at 32 font size

#Import Images
backgroundimg = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\blackvectorbackground.jpg')
buttonimg = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\blankbutton.png')
button2img = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\blankbutton2.png')
trophyimg = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\rltrophy2.png')
helptxt1img = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\helpText1.png')
helptxt2img = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\helpText2.png')

#resize images
trophyimg = pygame.transform.scale(trophyimg, (319, 400))
helptxt1img = pygame.transform.scale(helptxt1img, (1100, 77))
helptxt2img = pygame.transform.scale(helptxt2img, (1100, 77))

#Create gamestate
gameState = ['save1', 'start']

#####################
# F U N C T I O N S #
#####################

#get mouse position
def mouse():
    mosX, mosY = pygame.mouse.get_pos()
    #print('mosX: ', mosX, ' - ', 'mosY: ', mosY)
    return(mosX, mosY)

#get image length and height
def imgDim(img):
    imgWid = img.get_width()
    imgHei = img.get_height()
    return imgWid, imgHei

#test if mouse is hovering over a button
def imgHover(btn):
    #get mouse position
    mosX, mosY = mouse()
    #check if mouse x is within image width
    if (mosX>btn.getX()) and (mosX<btn.getX() + btn.getW()):
        insideX = True
    else:
        insideX = False
    #check if mouse y is within image height
    if (mosY>btn.getY()) and (mosY<btn.getY() + btn.getH()):
        insideY = True
    else:
        insideY = False
    #check if both x and y are true
    if (insideX == True) and (insideY == True):
        hover = True
    else:
        hover = False
    #print (hover)
    return hover 

#display start menu
def startMenu(gameState):

    #Create Strings
    title = basicFont.render('Rocket League Championship Series Simulator', False, (255, 255, 255))

    #create buttons (button image, image x, image y, font, string, text x offset, text y offset)
    btn1 = buttonClass.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 150, basicFont, 'Save 1', 75, 15)
    btn1H = buttonClass.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 150, basicFont, 'Save 1', 75, 15)
    btn2 = buttonClass.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2), basicFont, 'Save 2', 75, 15)
    btn2H = buttonClass.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2), basicFont, 'Save 2', 75, 15)
    btn3 = buttonClass.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 150, basicFont, 'Save 3', 75, 15)
    btn3H = buttonClass.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 150, basicFont, 'Save 3', 75, 15)
    btn4 = buttonClass.buttonClass(buttonimg, win.get_width() - 400, (win.get_height() / 2) + 200, basicFont, 'How to Play', 25, 15)
    btn4H = buttonClass.buttonClass(button2img, win.get_width() - 400, (win.get_height() / 2) + 200, basicFont, 'How to Play', 25, 15)
    btn5 = buttonClass.buttonClass(buttonimg, 100, (win.get_height() / 2) + 200, basicFont, 'Settings', 50, 15)
    btn5H = buttonClass.buttonClass(button2img, 100, (win.get_height() / 2) + 200, basicFont, 'Settings', 50, 15)

    #Menu Loop
    while gameState[1] == 'start':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Title
            win.blit(title, (150,70))
            #Draw Images
            win.blit(trophyimg, (100, 150))
            win.blit(trophyimg, (win.get_width() - 419, 150))

            #check for mouse hover
            btn1Hov = imgHover(btn1)
            btn2Hov = imgHover(btn2)
            btn3Hov = imgHover(btn3)
            btn4Hov = imgHover(btn4)
            btn5Hov = imgHover(btn5)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)
            if btn2Hov == True:
                btn2H.draw(win)
            else:
                btn2.draw(win)
            if btn3Hov == True:
                btn3H.draw(win)
            else:
                btn3.draw(win)
            if btn4Hov == True:
                btn4H.draw(win)
            else:
                btn4.draw(win)
            if btn5Hov == True:
                btn5H.draw(win)
            else:
                btn5.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click save 1 btn")
                    gameState[0] = 'save1'
                    gameState[1] = 'openSave'
                if btn2Hov == True:
                    print("mouse click save 2 btn")
                    gameState[0] = 'save2'
                    gameState[1] = 'openSave'
                if btn3Hov == True:
                    print("mouse click save 3 btn")
                    gameState[0] = 'save3'
                    gameState[1] = 'openSave'
                if btn4Hov == True:
                    print("mouse click how to btn")
                    gameState[1] = 'howToPlay'
                if btn5Hov == True:
                    print("mouse click settings btn")
                    gameState[1] = 'settings'


        pygame.display.update()
        mainClock.tick(60)

#display help menu
def howToPlayMenu(gameState):

    print('in how to play menu - ', gameState)

    #Create Strings
    title = basicFont.render('How to Play', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClass.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn1H = buttonClass.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)

    #Menu Loop
    while gameState[1] == 'howToPlay':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (510,70))
            #Draw Images
            win.blit(helptxt1img, (75, 200))
            win.blit(helptxt2img, (75, 300))
            
            #check for mouse hover
            btn1Hov = imgHover(btn1)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click start menu btn")
                    gameState[1] = 'start'

        pygame.display.update()
        mainClock.tick(60)
    
#display settings menu
def settingsMenu(gameState):

    print('in settings - ', gameState)

    #Create Strings
    title = basicFont.render('Settings', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClass.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn1H = buttonClass.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)

    #Menu Loop
    while gameState[1] == 'settings':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (510,70))
            #Draw Images

            
            #check for mouse hover
            btn1Hov = imgHover(btn1)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click start menu btn")
                    gameState[1] = 'start'

        pygame.display.update()
        mainClock.tick(60)

#display locker room menu
def lockerRoomMenu(gameState):

    print('in locker room - ', gameState)

    #Create Strings
    title = basicFont.render('Locker Room', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClass.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn1H = buttonClass.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)

    #Menu Loop
    while gameState[1] == 'openSave':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (510,70))
            #Draw Images

            
            #check for mouse hover
            btn1Hov = imgHover(btn1)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click start menu btn")
                    gameState[1] = 'start'

        pygame.display.update()
        mainClock.tick(60)



#main
def main(gameState):
    #sets default gamestate ['save file', 'current menu']
    gameState = gameState
    print(gameState)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Displays current menu
        if gameState[1] == 'start':
            print('run start menu')
            startMenu(gameState)
            print('exit start menu')
        if gameState[1] == 'howToPlay':
            print('run how to play menu')
            howToPlayMenu(gameState)
            print('exit how to play menu')
        if gameState[1] == 'settings':
            print('run settings menu')
            settingsMenu(gameState)
            print('exit settings menu')
        if gameState[1] == 'openSave':
            print('run locker room menu')
            lockerRoomMenu(gameState)
            print('exit locker room menu')

        pygame.display.update()
        mainClock.tick(60)

main(gameState)

