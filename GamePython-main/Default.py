import pygame


# size of game
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 660

# get text font and size
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font/fontText.otf", size)

pygame.init()
default_left = False
default_right = False

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Học tiếng Việt cùng bé")

# set background image
BG = pygame.image.load("assets/img/backGroundMainScreen.png")

# set music song
BG_MUSIC = pygame.mixer.Sound("assets/sound/BG_music.wav")
BG_MUSIC.set_volume(0.1)

CORRECT_MUSIC = pygame.mixer.Sound("assets/sound/correct_answer.wav")

INCORRECT_MUSIC = pygame.mixer.Sound("assets/sound/incorrect_answer.wav")

pygame.mixer.set_num_channels(3)
channel2 = pygame.mixer.Channel(2)

# status music
STATUS_MUSIC = True 

# index list
INDEX_LIST = 0

# score
SCORE = 0
