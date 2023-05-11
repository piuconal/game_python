import pygame
import sys
from Button import Button
import Default
import Data
import random

CENTER_SCREEN_WIDTH = Default.SCREEN_WIDTH//2
CENTER_SCREEN_HEIGHT = Default.SCREEN_HEIGHT//2
ONE_OVER_FOUR_SCREEN_WIDTH = CENTER_SCREEN_WIDTH//2
ONE_OVER_FOUR_SCREEN_HEIGHT = CENTER_SCREEN_HEIGHT//2
# random pos answer
RANDOM_POS_ANSWER = [(3*ONE_OVER_FOUR_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT-100),
                     (3*ONE_OVER_FOUR_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT),
                     (3*ONE_OVER_FOUR_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT+100)]

# play backround music
Default.BG_MUSIC.play(loops=-1)

# print play game


def playScreen():

    # init button in menu
    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/close.png"),(60,48)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//3, CENTER_SCREEN_HEIGHT//4),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    random.shuffle(RANDOM_POS_ANSWER)

    while True:

        # check read all list
        if (Default.INDEX_LIST >= len(Data.LIST_DATA)):
            winScreen()

        # set background
        Default.SCREEN.blit(pygame.transform.scale(
            Default.BG, Default.SCREEN.get_size()), (0, 0))

        # render: render the text into an image with a given color
        MENU_TEXT = Default.get_font(64).render("Đây là gì", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(
            center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//9))

        # set menu text to screen
        Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

        # render score
        SCORE_TEXT = Default.get_font(52).render(
            "Điểm: {}".format(Default.SCORE), True, "#FFFFFF")
        SCORE_RECT = SCORE_TEXT.get_rect(
            center=(7*ONE_OVER_FOUR_SCREEN_WIDTH//2, Default.SCREEN_HEIGHT//9))
        Default.SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)

        THE_QUESTION = Data.LIST_DATA[Default.INDEX_LIST]

        THE_QUESTION_IMAGE = Button(image=pygame.transform.scale(pygame.image.load(THE_QUESTION[0]), (360, 240)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT),
                                    text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White").update(Default.SCREEN)
        THE_ANSWER_1 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=RANDOM_POS_ANSWER[0],
                              text_input=THE_QUESTION[1], font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")
        THE_ANSWER_2 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=RANDOM_POS_ANSWER[1],
                              text_input=THE_QUESTION[2], font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")
        THE_ANSWER_3 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=RANDOM_POS_ANSWER[2],
                              text_input=THE_QUESTION[3], font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")

        for button in [THE_ANSWER_1, THE_ANSWER_2, THE_ANSWER_3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)
        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    menuScreen()
                    break
                if THE_ANSWER_1.checkForInput(MENU_MOUSE_POS):
                    print("Click the answer 1")
                    clickTrue()
                    break
                if THE_ANSWER_2.checkForInput(MENU_MOUSE_POS):
                    print("Click the answer 2")
                    clickFalse()
                    break
                if THE_ANSWER_3.checkForInput(MENU_MOUSE_POS):
                    print("Click the answer 3")
                    clickFalse()
                    break
        pygame.display.update()

# print settings


def settingScreen():
    # render: render the text into an image with a given color
    MENU_TEXT = Default.get_font(64).render("Cài đặt", True, "#FFFFFF")
    MENU_RECT = MENU_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//5))

    # init button in menu
    MUSIC_ON_BUTTON = Button(image=pygame.image.load("assets/img/music_on.png"), pos=(3*ONE_OVER_FOUR_SCREEN_WIDTH, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                             text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")
    MUSIC_OFF_BUTTON = Button(image=pygame.image.load("assets/img/music_off.png"), pos=(ONE_OVER_FOUR_SCREEN_WIDTH, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                              text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")
    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/close.png"),(60,48)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//3, CENTER_SCREEN_HEIGHT//4),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))

    # set menu text to screen
    Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [MUSIC_ON_BUTTON, MUSIC_OFF_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MUSIC_ON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Music On")
                    musicOn()
                    break
                if MUSIC_OFF_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Music Off")
                    musicOff()
                    break
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    menuScreen()
                    break
        pygame.display.update()

# print main menu


def menuScreen():

    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))
    # set menu text
    # render: render the text into an image with a given color
    SETTINGS_TEXT = Default.get_font(64).render(
        "Học tiếng Việt cùng bé", True, "#FFFFFF")
    SETTINGS_RECT = SETTINGS_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//5))
    # init button in menu

    FRAME_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/frame.png"), (380, 180)), pos=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT),
                          text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/Bar.png"), (190, 50)), pos=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT-50),
                         text_input="Chơi", font=Default.get_font(42), base_color="#d7fcd4", hovering_color="Black")
    OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/Bar.png"), (190, 50)), pos=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT),
                            text_input="Cài đặt", font=Default.get_font(42), base_color="#d7fcd4", hovering_color="Black")
    QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/Bar.png"), (190, 50)), pos=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT+50),
                         text_input="Thoát", font=Default.get_font(42), base_color="#d7fcd4", hovering_color="Black")

    # set menu text to screen
    Default.SCREEN.blit(SETTINGS_TEXT, SETTINGS_RECT)

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [FRAME_BUTTON, PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Play Game")
                    chooseTopicScreen()
                    break
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Open options")
                    settingScreen()
                    break
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Exit Game")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

# print answer screen


def winScreen():
    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))

    # render: render the text into an image with a given color
    MENU_TEXT = Default.get_font(64).render(
        "Chúc mừng bé đã hoàn thành trò chơi", True, "#FFFFFF")
    MENU_RECT = MENU_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//9))

    # set menu text to screen
    Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

    # render score
    SCORE_TEXT = Default.get_font(52).render(
        "Điểm: {}".format(Default.SCORE), True, "#FFFFFF")
    SCORE_RECT = SCORE_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT))
    Default.SCREEN.blit(SCORE_TEXT, SCORE_RECT)

    # init button in menu
    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/close.png"),(60,48)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//3, CENTER_SCREEN_HEIGHT//4),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    while True:

        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)
        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    Default.INDEX_LIST = 0
                    Default.SCORE = 0
                    menuScreen()
                    break
        pygame.display.update()

# turn on music


def musicOn():
    if (Default.STATUS_MUSIC == False):
        Default.STATUS_MUSIC = True
        Default.BG_MUSIC.play(loops=-1)

# turn off music


def musicOff():
    if (Default.STATUS_MUSIC == True):
        Default.STATUS_MUSIC = False
        Default.BG_MUSIC.stop()


def clickUp():
    random.shuffle(RANDOM_POS_ANSWER)
    if (Default.INDEX_LIST < len(Data.LIST_DATA)):
        Default.INDEX_LIST += 1


def clickTrue():
    clickUp()
    Default.SCORE += 10
    correctScreen()


def clickFalse():
    clickUp()
    incorrectScreen()

# print correct screen


def correctScreen():
    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))
    # set menu text
    # render: render the text into an image with a given color
    SETTINGS_TEXT = Default.get_font(64).render(
        "Bé trả lời đúng rồi", True, "#FFFFFF")
    SETTINGS_RECT = SETTINGS_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT))
    # set menu text to screen
    Default.SCREEN.blit(SETTINGS_TEXT, SETTINGS_RECT)
    NEXT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/next.png"),(60,48)), pos=(7*(ONE_OVER_FOUR_SCREEN_WIDTH//2), 7*(ONE_OVER_FOUR_SCREEN_HEIGHT//2)),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    # set sound correct
    if Default.STATUS_MUSIC:
        Default.CORRECT_MUSIC.play()

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NEXT_BUTTON.update(Default.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Next Game")
                    playScreen()
        pygame.display.update()

# print incorrect screen


def incorrectScreen():
    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))
    # set menu text
    # render: render the text into an image with a given color
    SETTINGS_TEXT = Default.get_font(64).render(
        "Bé trả lời chưa đúng", True, "#FFFFFF")
    SETTINGS_RECT = SETTINGS_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT))
    # set menu text to screen
    Default.SCREEN.blit(SETTINGS_TEXT, SETTINGS_RECT)
    NEXT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/next.png"),(60,48)), pos=(7*(ONE_OVER_FOUR_SCREEN_WIDTH//2), 7*(ONE_OVER_FOUR_SCREEN_HEIGHT//2)),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    # set sound correct
    if Default.STATUS_MUSIC:
        Default.INCORRECT_MUSIC.play()
    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NEXT_BUTTON.update(Default.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Next Game")
                    playScreen()
        pygame.display.update()


# print choose topic screen

def chooseTopicScreen():
    # init button in menu
    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/close.png"),(60,48)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//3, CENTER_SCREEN_HEIGHT//4),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    # render: render the text into an image with a given color
    MENU_TEXT = Default.get_font(64).render("Chọn chủ đề", True, "#FFFFFF")
    MENU_RECT = MENU_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//5))

    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))

    # set menu text to screen
    Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

    THE_FLOWER = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH+100, ONE_OVER_FOUR_SCREEN_HEIGHT+100),
                        text_input="Các loại hoa", font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")
    THE_FRUIT = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=(ONE_OVER_FOUR_SCREEN_WIDTH+100, 3*ONE_OVER_FOUR_SCREEN_HEIGHT-100),
                       text_input="Các loại quả", font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")
    THE_WEATHER = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=(3*ONE_OVER_FOUR_SCREEN_WIDTH-100, ONE_OVER_FOUR_SCREEN_HEIGHT+100),
                         text_input="Các loại thời tiết", font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")
    THE_SKIN = Button(image=pygame.transform.scale(pygame.image.load("assets/img/barblue.png"), (180, 40)), pos=(3*ONE_OVER_FOUR_SCREEN_WIDTH-100, 3*ONE_OVER_FOUR_SCREEN_HEIGHT-100),
                      text_input="Các loại quần áo", font=Default.get_font(36), base_color="#FFFFFF", hovering_color="Black")

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [THE_FLOWER, THE_FRUIT, THE_SKIN, THE_WEATHER, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)
        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    menuScreen()
                    break
                if THE_FLOWER.checkForInput(MENU_MOUSE_POS):
                    print("Click the flower")
                    Data.LIST_DATA = Data.LIST_FLOWER
                    playScreen()
                    break
                if THE_FRUIT.checkForInput(MENU_MOUSE_POS):
                    print("Click the fruit")
                    Data.LIST_DATA = Data.LIST_FRUIT
                    playScreen()
                    break
                if THE_SKIN.checkForInput(MENU_MOUSE_POS):
                    print("Click the skin")
                    Data.LIST_DATA = Data.LIST_SKIN
                    playScreen()
                    break
                if THE_WEATHER.checkForInput(MENU_MOUSE_POS):
                    print("Click the weather")
                    Data.LIST_DATA = Data.LIST_WEATHER
                    playScreen()
                    break
        pygame.display.update()
