from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

# Define our functions for the buttons
def start_the_game():
    pass

# Start the pygame
pygame.init()
# Create a window with a size
surface = pygame.display.set_mode((600, 400))

# Creating the main menu
mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)

# Add stuff to the menu
# Make an input where the user can type in a username
mainmenu.add.text_input("Name: ", default='username', maxchar=10)
# Make a play button to start the game, when user clicks the button, trigger the start_the_game function
mainmenu.add.button('Play Game', start_the_game)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)


mainmenu.mainloop(surface)