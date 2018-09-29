# Chrome-Dinosaur

### *by Pun Waiwitlikhit 29 September 2018 Brighton College Programming Club*

What are libraries?
- Libraries are a collection of functions which adds functions to a language.
- A video game library in python might add functions such as createSprite() which are not usable in normal python.
- Libraries are essentially a bunch of functions that can be imported to another file where it can be used.
- Pygame is a video game library that is written in python.

Intro to Pygame
- Pygame is a library meaning that you have to download it and import it into your code before you are able to use it.
You can install pygame by typing this in your TERMINAL: 

``` pip3 install pygame ```

To import pygame into your python code, add this to your python code: 

``` import pygame ```

# Initializing
The first thing we would like to do is initialize the project: We do this by

```
import pygame
pygame.init() #this ‘starts up’ pygame

size = width,height = 640, 480#creates tuple called size with width 400  and height 230
gameDisplay= pygame.display.set_mode(size) #creates screen

while True: #gameLoop it draws the frames of the game


  for event in pygame.event.get(): #Check for events
    if event.type == pygame.QUIT:
      pygame.quit() #quits
      quit()

  pygame.display.update() #updates the screen

```
The important parts of this code is the contents of while True: as it is the game loop, or the loop which draws the frame every second and updates the state of the game. The event loop (for event in pygame.event.get()) loops through all the events that have just happened -- an example of this being the user pressing the exit button on the window -- and then decides how to respond to the user input. Anything before the gameloop is just initialization code.

# Drawing Shapes
To draw shapes in pygame, we use predefined commands from the pygame library. To do this, we edit the game loop

```
white = 255,255,255 #Define the RGB value of white as a tuple
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()			
  pygame.draw.rect(gameDisplay, white, [30,30,40,50])
  #draws a rectangle at coordinate (30 ,30) with width 40 pixel, height 50 pixels and with colour white on the surface ’gameDisplay’

  pygame.display.update()
```

# Drawing the Ground
Now that we know how to draw a shape, we would like to have the practical use of the shape in the game. To do this, we will draw a ground. The ground is essentially a rectangle which left corner is on the edge and the width of the rectangle is as wide as the window. As we may want to experiment with the height of the ground we will use a variable to store it.

```GROUND_HEIGHT = height-200#The y coordinate of the floor which is 200 pixels away from the bottom```

To draw the ground, add this code to the main loop

```pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])```

As an update, your code should now look like this.

```
#main.py

import pygame
pygame.init() #this ‘starts up’ pygame
size = width,height = 640, 480 #creates tuple called size with width 400 and height 230
gameDisplay= pygame.display.set_mode(size) #creates screen
GROUND_HEIGHT = height-100
black = 0,0,0
white = 255,255,255 #Define the RGB value of white as a tuple
xPos = 0
yPos = 0
while True: #gameLoop it draws the frames of the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() #quits
      quit()
  gameDisplay.fill(black)
  pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])
  xPos += 1
  yPos += 1
  pygame.display.update() #updates the screen
```

# The Dinosaur
To create the dinosaur, we will first create a class defining a dinosaur and then create a dinosaur object which we will manipulate in the gameloop. To create a class, we start a new file called dinosaur.py in the same project folder as the main.py code. The class should look like this.

```
import pygame
dinocolour = 255,255,255
DINOHEIGHT = 40
DINOWIDTH = 20
class Dinosaur:
  def __init__(self, surfaceHeight):
    self.x = 60
    self.y = 0
    self.yvelocity = 0
    self.height = DINOHEIGHT
    self.width = DINOWIDTH
    self.surfaceHeight = surfaceHeight
  def jump(self): #When adding classes into function, the first parameter must be the parameter
    if(self.y == 0): #Only allow jumping if the dinosaur is on the ground to prevent mid air jumps.
      self.yvelocity = 300
  def update(self, deltaTime): #Updates the y position of the dinosaur each second
    self.yvelocity += -500*deltaTime #Gravity
    self.y += self.yvelocity * deltaTime
    if self.y < 0: #if the dinosaur sinks into the ground, make velocity and y = 0
      self.y = 0
      self.yvelocity = 0

  def draw(self,display):
    pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])
```

Now that we have created the class, we need to import the class into the game and create the dinosaur object to do that, we add the following code OUTSIDE the game loop.

```
from dinosaur import Dinosaur #import the class Dinosaur from the file ’dinosaur’
dinosaur = Dinosaur(GROUND_HEIGHT)
```

As our functions require a deltaTime (change in time between the current Game loop and the previous gameloop) which makes our dinosaur move relative to time not the speed of the computer running the game. To do that, we add this before the gameloop

```dinosaur = Dinosaur(GROUND_HEIGHT)```

and this at the start of the gameloop

```t = pygame.time.get_ticks() #Get current time
deltaTime = (t-lastFrame)/1000.0 #Find difference in time and then convert it to seconds
lastFrame = t #set lastFrame as the current time for next frame.
```

Now we want to draw and update the dinosaur

```dinosaur.update(deltaTime)
dinosaur.draw(gameDisplay) #Draw dinosaur on gameDisplay
```

After that, we would like to jump if the user presses space.

```if event.type == pygame.KEYDOWN: #If user uses the keyboard
if event.key == pygame.K_SPACE: #If that key is space
	dinosaur.jump() #Make dinosaur jump
```

In the end, your main.py should look like the following

```
import pygame
from dinosaur import Dinosaur #import the class Dinosaur from the file ’dinosaur’

pygame.init() #this ‘starts up’ pygame

#initialize game
size = width,height = 640, 480#creates tuple called size with width 400  and height 230
gameDisplay= pygame.display.set_mode(size) #creates screen
xPos = 0
yPos = 0
GROUND_HEIGHT = height-100

# create Dinosaur
dinosaur = Dinosaur(GROUND_HEIGHT)

#create lastframe variable
lastFrame = pygame.time.get_ticks() #get ticks returns current time in milliseconds

#define game colours
white = 255,255,255
black = 0,0,0

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

    pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])
    pygame.display.update() #updates the screen 

```


# The Obstacle

Just like the dinosaur, we will create the class for the obstacles on a completely separate file. I will name mine obstacle.py

```
# obstacle.py

import pygame

colour = 0,0,255
class Obstacle:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, colour, [self.x, self.GroundHeight-self.size, self.size, self.size])

    def update(self, deltaTime, velocity):
        self.x -= velocity*deltaTime

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False
```

#### Initializing the obstacle
To initialize the obstacle, we add this before the gameloop in your main.py file

```
# main.py

import random
from obstacle import Obstacle
MINGAP = 200
VELOCITY = 300
MAXGAP = 600
obstacles = []
num_of_obstacles = 4
lastObstacle = width
SCORE = 0
obstaclesize = 50
for i in range(4):
	lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random() #Make distance between rocks random
	obstacles.append(Obstacle(lastObstacle, obstaclesize, GROUND_HEIGHT))
```

#### Making the Obstacles move
To make the obstacles move, we would need to add the following to the main.py file
Now that we have created obstacles, we have to use the update function on them. In the initializing code above, we have defined VELOCITY which will be the speed at which the obstacles will move. Add the following into the main loop.

```
for obs in obstacles:
	obs.update(deltaTime, VELOCITY)
	obs.draw(gameDisplay)
```

To check if the obstacle has passed, we need add the if statement into the for loop above. Each time the obstacle touches the edge of the screen, it resets its position and the player also scores a point.

```
if(obs.checkOver()):
	SCORE += 1
	lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random()
	obs.x = lastObstacle
```

Also, in each frame of the game, we have to update the position of the lastObstacle (Keeps track of the position of the final obstacle so that the obstacles can add itself to the back of the queue. We do this by

```
lastObstacle -= VELOCITY*deltaTime
```
