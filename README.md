# Chrome-Dinosaur
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

#Initializing
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

Drawing Shapes
To draw shapes in pygame, we use predefined commands from the pygame library. To do this, we edit the game loop 

```white = 255,255,255 #Define the RGB value of white as a tuple
while True:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
quit()			
pygame.draw.rect(gameDisplay, white, [30,30,40,50]) 
#draws a rectangle at coordinate (30 ,30) with width 40 pixel, height 50 pixels and with colour white on the surface ’gameDisplay’

pygame.display.update() 
```
