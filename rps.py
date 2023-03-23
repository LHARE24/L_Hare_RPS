# File created by Liam Hare

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
from random import randint
import os

# setup asset folders 
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings 
WIDTH = 1000
HEIGHT = 800
FPS = 30

# define colors, RGB values, immutable
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# defines draw text into 
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

choices = ["rock", "paper", "scissors"]


# function that allows cpu to choose randomly...
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice

# initialzes pygame and creates a window
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
clock = pg.time.Clock()

# Importing the rock image,changing its location
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()

# Importing the paper image, changing its location
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()

# Importing the scissors image
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
scissors_image_rect = scissors_image.get_rect()

# Game loop
start_screen = True

player_choice = ""
cpu_choice = ""
running = True
replay = False
while running:
    # keeps the loop running using clock
    clock.tick(FPS)
        
    # When hitting space, the game starts
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("Start")
                start_screen = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                print("Watch")
                replay = True
        if event.type == pg.MOUSEBUTTONUP:
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
        # shows where you are clicking on the screen
        if event.type == pg.MOUSEBUTTONUP:
            # displays the coordinates of where we clicked
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
        # if the mouse clickes, then it tells us if we clicked on the images or not
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("You clicked on Rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                print("You clicked on Paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("You clicked on Scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
            else:
                print("You didnt click on Anything")

    # draws the background screen black
    screen.fill(BLACK)
    # draws the rock, the paper, and the scissors
    screen.blit(rock_image, rock_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    screen.blit(paper_image, paper_image_rect)

    if start_screen:
        print("this is working...")
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
        rock_image_rect.y = 2000
        paper_image_rect.y = 2000
        scissors_image_rect.y = 2000

    # allows player to choose rock paper or scissors
    if not start_screen and player_choice == "":
        rock_image_rect.y = 50
        paper_image_rect.y = 250
        scissors_image_rect.y = 400
      

    # checks to see what the outcome of the contest was
    if player_choice == "rock":
        if cpu_choice == "rock":
            rock_image_rect.x = 700
            screen.blit(rock_image, rock_image_rect)
            draw_text("You tied", 22, WHITE, WIDTH/2, HEIGHT/10)
            
        if cpu_choice == "paper":
            paper_image_rect.x = 700
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, paper_image_rect)
            draw_text("You Lost", 22, WHITE, WIDTH/2, HEIGHT/10)
            
        if cpu_choice == "scissors":
            scissors_image_rect.x = 700
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, scissors_image_rect)
            draw_text("You Won", 22, WHITE, WIDTH/2, HEIGHT/10)

    if player_choice == "paper":
        if cpu_choice == "rock":
            rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            draw_text("You Won", 22, WHITE, WIDTH/2, HEIGHT/10)
            
        if cpu_choice == "paper":
            paper_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, paper_image_rect)
            draw_text("You Tied", 22, WHITE, WIDTH/2, HEIGHT/10)
            
        if cpu_choice == "scissors":
            scissors_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, scissors_image_rect)
            draw_text("You Lost", 22, WHITE, WIDTH/2, HEIGHT/10)

    if player_choice == "scissors":
        if cpu_choice == "rock":
            rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            draw_text("You Lost", 22, WHITE, WIDTH/2, HEIGHT/10)
            
        if cpu_choice == "paper":
            paper_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, paper_image_rect)
            draw_text("You Won", 22, WHITE, WIDTH/2, HEIGHT/10)
            
        if cpu_choice == "scissors":
            scissors_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, scissors_image_rect)
            draw_text("You Tied", 22, WHITE, WIDTH/2, HEIGHT/10)
    pg.display.flip()
pg.quit()