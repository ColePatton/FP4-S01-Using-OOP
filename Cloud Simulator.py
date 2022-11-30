#--------------------------------
# Nov. 30th, 2022
# Cole Patton
# FP4-Summative 01 - Using OOP
#--------------------------------
# This program is called, "Cloud Simulator!". A funny name for a silly game.
# So basically, this game was developed using a a bit of code that I pulled out of a bunch of different
# versions of the SCHMUP game I made, as well as some of my own code I wrote. The idea for a game like this came from when
# on one version of the SCHMUP tutorial, he coded the left and right arrow keys, and I wondered if I would be able to
# add the movement for going up and down so you can move all over the screen. So that's what I did! And I wrote a bit more code
# to just make it more like a cloud simulator and then I was done!

#--------------------------------------------------------------------------

#-----------Imports Are Here-----------------
import pygame
import random
from os import path

#------A Few Variables Are Defined Here------
WIDTH = 480
HEIGHT = 600 # The screen size and the frames it will run at.
FPS = 60
img_dir = path.join(path.dirname(__file__), 'images') # Finds the image path to where it is located


#------Colors Defined Here-------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#----------initialize pygame and create window---------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))# Creates window using your width and height
pygame.display.set_caption("Cloud Simulator") # name of window
clock = pygame.time.Clock()# Keeps track of speed of game

#------------------Functions Defined Here---------------------
# This function is for the intro screen,
# it comes up once at the start before you begin to play!
def intro_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Cloud Simulator", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Use LEFT, RIGHT, UP and DOWN arrow keys to move!", 22,
              WIDTH / 2, HEIGHT / 2)                                                 #Intro text showing the instructions!
    draw_text(screen, "Press any key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                  #If statements to see if you quit out, or if any key is pressed,
            if event.type == pygame.KEYUP:     #it will begin the game!
                waiting = False
                
#The function for drawing any sort of text, this is reused many times!
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)                

# The player class, which in this case is the cloud
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, random.choice([(75, 125), (50, 100)])) # Scales the player model randomly!
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.rect.top = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        
    # This function in the player class checks what keys are pressed for movement, as well as
    # If you touch any of the borders, what it has to do then.
    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed() #gives list of every key pressed at the time
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5              # I added these keys to be able to move the rectangle up and down as well!
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT: # In these last 4 lines, I added this so that the rectangle does not just go off screen, and it instead teleports to
            self.rect.top = 0 # The bottom if you go over the top, and to the top if you go passed the bottom.
        if self.rect.bottom < 0:
            self.rect.bottom = HEIGHT 
        
#------------Game graphics Defined Here---------------
background = pygame.image.load(path.join(img_dir, "sky.jpg")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "cloud5.png")).convert()


#---------------The Sprites and the Player Are Defined and "Created" Here-------------

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#-------------------------------------------------------------------------

# Game Loop
running = True
game_over = True
while running:
    if game_over:
        intro_screen() # I added an intro screen for when you start up the game
        # keep running at the right speed
    game_over = False # This gets made False here so that the intro screen does not show again after you enter the game.
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()
    
    # Draw / Render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


#------------------------------Questions------------------------------------

#What is the difference between OOP and Procedural coding?
    # Procedural coding uses single line by line steps that are very exact to execute a program. This is quite different compared to OOP,
    # where, sure it uses line by line, but it uses things like classes and many different variables to create and redo code all by itself.
    # OOP in just many ways is much more complex than procedural coding. It's literally in the name, it uses just procedures of code
    # to work a program line by line.
#------------------------------------------------------------------
#How would your program differ if it were made in procedural coding instead?
    # I don't know how you would even do this. I can just imagine it being a hell of a lot longer, with MANY many more lines of code
    # than this one even has. I think it would differ in the fact that it would be much longer, and the code would be big and I think
    # best way to describe it, is very jumbled!
#------------------------------------------------------------------
#What are the benefits of OOP?
    # There are MANY benefits to using OOP in your programs. Your code is much more organized, and you don't have to have
    # as many lines of code especially when you are utilizing classes and functions to the best of their abilities. 
    # OOP makes your lines of code much more reusable and adjustable without having to change a lot of things. For example:
    # you don't have to change a bunch of functions and variables to edit one thing about something if you use classes
    # you can simply just edit the class that creates all of your things to edit, basically everything at once that is under that class.
    # OOP is VERY handy and I can see where/how/why it is used a lot in coding especially for more complex things like bigger videogames.
#--------------------------------------------------------------------------
# What are the drawbacks?
    # I think really the only drawback that I can think of would be just the difficult nature of OOP.
    # It is really quite confusing especially for a beginner with it who is just learning how to use it. It's hard to get the hang of it.
    # And there is always a lot going on when you are dealing with OOP. This is really te only drawback though, really. And it is one
    # that goes away after you practice lots and get very good with it. It is a drawback that simply just takes time to go away.
    # And after that, it is an amazing form of programming! :)
