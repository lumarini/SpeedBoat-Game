import pygame
import random
import time

pygame.init()
pygame.key.set_repeat(1, 80)

# SCREEN DEF
TITLE = "River Raid"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (83, 127, 181)
RED = (163, 41, 29)
GREEN = (0, 255, 0)
DARK_GREY = (100, 100, 100)
# FONT
pygame.font.init()
large_font = pygame.font.SysFont("Consolas", 60)
small_font = pygame.font.SysFont("Consolas", 32)
game_font = pygame.font.SysFont("Consolas", 18)
# IMAGES
player = "boat.png"
player_image = pygame.image.load(player)
fuel = "fuel.png"
fuel_resize = pygame.image.load(fuel)
fuel_image = pygame.transform.scale(fuel_resize, (75, 120))
bigboat = "obstacle1.png"
bigboat_load = pygame.image.load(bigboat)
bigboat_resize = pygame.transform.scale(bigboat_load, (100, 300))
bigboat_image = pygame.transform.rotate(bigboat_resize, 180)
smallboat = "obstacle2.png"
smallboat_load = pygame.image.load(smallboat)
smallboat_resize = pygame.transform.scale(smallboat_load, (80, 200))
smallboat_image = pygame.transform.rotate(smallboat_resize, 180)
# INITIAL POSITIONS
PLAYER_INITIAL_X = 400
PLAYER_INITIAL_Y = 450
# Gameplay
TICK_RATE = 30
clock = pygame.time.Clock()
pause = False
lives = 3

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(BLUE)
pygame.display.set_caption(TITLE)


# 1. Display.set_mode()
# 2. Create a font object font.Font() -- text_font
# 3. Create Text surface object render()
# 4. Create a rectangular object for text surface object using get_rect()
# 5. Set rect position - center property
# 6. Copying text surface to display using Blit
# 7. lastly, update display display.update()

# mouse = pygame.mouse.get_pos()
# mouse_click = pygame.mouse.get_pressed()


class Player(pygame.Rect):
    def __init__(self, image, x, y, w, h):
        super().__init__(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        game_screen.blit(image, (x, y))


class Obstacle(pygame.Rect):
    def __init__(self, image, x, y, width, height):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        game_screen.blit(image, (x, y))


class Fuel_station(pygame.Rect):
    def __init__(self, image, x, y, width, height):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        game_screen.blit(image, (x, y))


def add_text(x, y, text, font):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    game_screen.blit(text_surface, text_rect)


def unpause():
    global pause
    pause = False


def button_continue():
    light_green = (88, 245, 91)
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    mouse_xpos = mouse[0]
    mouse_ypos = mouse[1]
    green = (56, 156, 58)
    pygame.draw.rect(game_screen, DARK_GREY, [320, 320, 180, 90])
    if 360 < mouse_xpos < 520 and 320 < mouse_ypos < 410:
        pygame.draw.rect(game_screen, light_green, [320, 320, 170, 80])
        add_text(400, 360, "CONTINUE", small_font)
        if mouse_click[0] == 1:
            unpause()
    else:
        pygame.draw.rect(game_screen, green, [320, 320, 170, 80])
        add_text(400, 360, "CONTINUE", small_font)


def paused():
    global pause
    pause = True
    while pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    unpause()

        add_text(400, 240, "GAME PAUSED", large_font)
        button_continue()
        add_text(400, 450, "Press 'C' to continue.", small_font)
        pygame.display.update()
        clock.tick(15)


def button_start():
    light_green = (88, 245, 91)
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    mouse_xpos = mouse[0]
    mouse_ypos = mouse[1]
    green = (56, 156, 58)
    pygame.draw.rect(game_screen, DARK_GREY, [160, 360, 160, 90])
    if 160 < mouse_xpos < 320 and 360 < mouse_ypos < 450:
        pygame.draw.rect(game_screen, light_green, [160, 360, 150, 80])
        add_text(230, 400, "START", small_font)
        if mouse_click[0] == 1:
            game_loop()
    else:
        pygame.draw.rect(game_screen, green, [160, 360, 150, 80])
        add_text(230, 400, "START", small_font)


def button_quit():
    light_red = (232, 88, 86)
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    mouse_xpos = mouse[0]
    mouse_ypos = mouse[1]
    red = (186, 69, 67)
    pygame.draw.rect(game_screen, DARK_GREY, [480, 360, 160, 90])
    if 480 < mouse_xpos < 640 and 360 < mouse_ypos < 450:
        pygame.draw.rect(game_screen, light_red, [480, 360, 150, 80])
        add_text(550, 400, "QUIT", small_font)
        if mouse_click[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(game_screen, red, [480, 360, 150, 80])
        add_text(550, 400, "QUIT", small_font)


def game_intro():
    intro = True
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_screen.fill(BLUE)
        add_text(400, 240, "River Raid", large_font)
        button_start()
        button_quit()
        pygame.display.update()
        clock.tick(15)


def game_over_screen():
    global lives
    over = True
    while over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_screen.fill(BLUE)
        add_text(400, 200, "GAME OVER", large_font)
        add_text(400, 300, "Play again?", small_font)
        button_start()
        button_quit()
        lives = 3
        pygame.display.update()
        clock.tick(15)


def crash_sequence():
    global lives
    lives -= 1
    add_text(400, 200, "CRASHED!", large_font)
    add_text(400, 300, "You lose 1 life", small_font)
    if lives < 0:
        pygame.display.update()
        time.sleep(1)
        game_over_screen()


def game_loop():
    global lives
    game_over = False
    level = 1
    score = 0
    fuel = 100
    fuel_decrease_rate = 0.1
    player_speed = 7
    obstacle_speed = 5
    increased_obstacle_speed = obstacle_speed * 1.3
    decreased_obstacle_speed = obstacle_speed * 0.7
    player_x_change = 0
    player_x = 400
    player_y = PLAYER_INITIAL_Y
    start = [50, 250, 400, 550, 750]
    start2 = [80, 200, 350, 600, 750]
    start3 = [100,300,500,700]
    starty = [-50, -80, -100, -200, -300, -400]
    obstacle_x = random.choice(start)
    obstacle_y = -100
    obs_2_x = random.choice(start2)
    obs_2_y = -250
    obs_3_x = random.choice(start3)
    obs_3_y = -200
    fuelstation_x = random.choice(start)
    fuelstation_y = -100
    new_fuelstation = False


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change -= player_speed
                    fuel -= fuel_decrease_rate
                if event.key == pygame.K_RIGHT:
                    player_x_change += player_speed
                    fuel -= fuel_decrease_rate
                if event.key == pygame.K_SPACE:
                    paused()
                if event.key == pygame.K_UP:
                    if obstacle_speed <= increased_obstacle_speed:
                        obstacle_speed += 1
                        fuel -= fuel_decrease_rate * 1.4
                if event.key == pygame.K_DOWN:
                    if obstacle_speed >= decreased_obstacle_speed:
                        obstacle_speed -= 1
                        fuel -= fuel_decrease_rate

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change += 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    obstacle_speed += 0
                    fuel -= fuel_decrease_rate/2

        # CHANGING PLAYER POSITION
        current_player_x = player_x + player_x_change
        if current_player_x < 0 or current_player_x > 770:
            crash_sequence()
            player_x = 400
            obstacle_y = random.choice(starty)
            obstacle_x = random.choice(start)
            obs_2_x = random.choice(start2)
            obs_2_y = random.choice(starty)
            obs_3_x = random.choice(start3)
            obs_3_y = random.choice(starty)
            pygame.display.update()
            time.sleep(2)

        # CHANGING OBSTACLE POSITION
        obstacle_y += obstacle_speed
        obs_2_y += (obstacle_speed * 1.1)
        player_speed = (7 + level / 5)
        fuel_decrease_rate = (0.1 + level / 20)
        if score < 10:
            obs_3_y = -300

        if score > 10:
            obs_3_y += 5
            obstacle_speed = (5 + level/2)
            player_speed = (7 + level / 8)
            fuel_decrease_rate = (0.1 + level / 50)
            level = 1 + score // 10
            if score > 10 and score % 5 == 0:
                new_fuelstation = True

        # RE-DRAWING SCREEN
        fuel_shown = round(fuel)
        level_shown = round(level)
        game_screen.fill(BLUE)
        add_text(60, 20, f"LEVEL: {level_shown}", game_font)
        add_text(280, 20, f"SCORE: {score}", game_font)
        add_text(520, 20, f"LIVES: {lives}", game_font)
        add_text(720, 20, f"FUEL {fuel_shown} %", game_font)

        player = Player(player_image, current_player_x, player_y, 40, 80)
        first_boat = Obstacle(bigboat_image, obstacle_x, obstacle_y, 90, 290)
        second_boat = Obstacle(smallboat_image, obs_2_x, obs_2_y, 90, 230)
        third_boat = Obstacle(smallboat_image, obs_3_x, obs_3_y, 90, 230)

        if new_fuelstation == True:
            fuel_station = Fuel_station(fuel_image, fuelstation_x, fuelstation_y, 175, 120)
            fuelstation_y += obstacle_speed
            if player.colliderect(fuel_station):
                if fuel < 99:
                    fuel += 1
            if fuelstation_y > 600:
                fuelstation_x = random.choice(start)
                fuelstation_y = -200
                new_fuelstation = False

        if fuel < 1:
            lives -= 1
            add_text(400, 200, "OUT OF FUEL", large_font)
            add_text(400, 300, "You lose 1 life", small_font)
            pygame.display.update()
            time.sleep(2)
            if lives < 0:
                game_over_screen()
            fuel = 50
            player_x = 400
            obstacle_y = random.choice(starty)
            obstacle_x = random.choice(start)
            obs_2_x = random.choice(start2)
            obs_2_y = random.choice(starty)
            obs_3_x = random.choice(start3)
            obs_3_y = random.choice(starty)
            pygame.display.update()
            time.sleep(2)

        if player.colliderect(first_boat):
            crash_sequence()
            player_x = 400
            obstacle_y = random.choice(starty)
            obstacle_x = random.choice(start)
            obs_2_x = random.choice(start2)
            obs_2_y = random.choice(starty)
            obs_3_x = random.choice(start3)
            obs_3_y = random.choice(starty)
            pygame.display.update()
            time.sleep(2)


        if player.colliderect(second_boat):
            crash_sequence()
            player_x = 400
            obstacle_y = random.choice(starty)
            obstacle_x = random.choice(start)
            obs_2_x = random.choice(start2)
            obs_2_y = random.choice(starty)
            obs_3_x = random.choice(start3)
            obs_3_y = random.choice(starty)
            pygame.display.update()
            time.sleep(2)


        if player.colliderect(third_boat):
            crash_sequence()
            player_x = 400
            obstacle_y = random.choice(starty)
            obstacle_x = random.choice(start)
            obs_2_x = random.choice(start2)
            obs_2_y = random.choice(starty)
            obs_3_x = random.choice(start3)
            obs_3_y = random.choice(starty)
            pygame.display.update()
            time.sleep(2)


        if obstacle_y > 600:
            obstacle_y = random.choice(starty)
            score += 1
            obstacle_x = random.choice(start)

        if obs_2_y > 600:
            obs_2_y = random.choice(starty)
            score += 1
            obs_2_x = random.choice(start2)

        if obs_3_y > 600:
            obs_3_y = random.choice(starty)
            score += 1
            obs_3_x = random.choice(start3)

        pygame.display.update()
        clock.tick(TICK_RATE)
        print(f"Level: {level}, Score: {score}, fuel {fuel}, obstacle speed {obstacle_speed}, player speed {player_speed}, fuel decrease rate {fuel_decrease_rate}, ")

# INITIALISE PROGRAMME:
game_intro()
game_loop()

# QUIT PROGRAM
pygame.quit()
quit()
