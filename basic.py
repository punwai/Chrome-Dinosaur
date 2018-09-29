import pygame
from dinosaur import Dinosaur #import the class Dinosaur from the file ’dinosaur’
from obstacle import Obstacle

pygame.init() #this ‘starts up’ pygame

size = width,height = 640, 480#creates tuple called size with width 400  and height 230 
gameDisplay= pygame.display.set_mode(size) #creates screen
xPos = 0
yPos = 0
black = 0,0,0
GROUND_HEIGHT = height-100 


dinosaur = Dinosaur(GROUND_HEIGHT)

lastFrame = pygame.time.get_ticks() #get ticks returns current time in milliseconds

import random
MINGAP = 200
VELOCITY = 300
MAXGAP = 600
obstacles = []
num_of_obstacles = 4
lastObstacle = width


obstaclesize = 20
for i in range(4):
    lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random() #Make distance between rocks random
    obstacles.append(Obstacle(lastObstacle, size, GROUND_HEIGHT))




white = 255,255,255
while True: #gameLoop it draws the frames of the game 
    t = pygame.time.get_ticks() #Get current time
    deltaTime = (t-lastFrame)/1000.0 #Find difference in time and then convert it to seconds
    lastFrame = t #set lastFrame as the current time for next frame.

    for event in pygame.event.get(): #Check for events
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            quit()
        if event.type == pygame.KEYDOWN: #If user uses the keyboard
            if event.key == pygame.K_SPACE: #If that key is space
                dinosaur.jump() #Make dinosaur jump


    gameDisplay.fill(black)

    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)

    for obs in obstacles:
        obs.update(deltaTime, VELOCITY)
        obs.draw(gameDisplay)
        if(obs.checkOver()):
            lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random()
            obs.x = lastObstacle

    lastObstacle -= VELOCITY*deltaTime


    pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])
    pygame.draw.rect(gameDisplay, white, [xPos,yPos,40,50]) #make xPos the value of pygame 
    xPos += 1 #increment by 1
    yPos += 1 #increment by 1
    pygame.display.update() #updates the screen 
