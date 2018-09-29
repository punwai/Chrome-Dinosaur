## Chrome-Dinosaur 

*by Pun Waiwitlikhit 29 September 2018 Brighton College Programming Club*

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

