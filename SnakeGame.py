# draw.rect---> has in order.... x coord, y coord, length, breadth
# After every pygame.display.update()-> the screen changes like to another
# Clock.tick() --> tells us how fast the snake moves
# Improvements- can add command to not go down in same line when moving up, add high score
# for i in range(10000000) delay of 1 sec

import time
import pygame
import random
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
global dis_width, dis_height, snakeblock, snakelist
snakelist=[]
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("times new roman", 25)
score_font = pygame.font.SysFont("times new roman", 35)

def rules():
    pygame.init()
    rul="Rules of the game:"
    rule1="-> The snake is of colour white."
    rule2="-> Eat the food to increase the length of the snake."
    rule3="-> Level 1-Level without boundaries."
    rule4="-> Level 2-With boundaries, same speed as level 1."
    rule5="-> Level 3-The speed of the snake increases with boundary intact."
    rule6="-> Level 4-Speed increases and obstacles are introduced."
    exit_rule="--->>  In order to play the game close the rules window"
    display_surface = pygame.display.set_mode((dis_width,dis_height))
    pygame.display.set_caption('Rules')
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(rul, True, white)
    textRect = text.get_rect()
    textRect.center = (150,25)
    tex1 = font.render(rule1, True, white)
    textRec1 =tex1.get_rect()
    textRec1= (140,60)
    tex2 = font.render(rule2, True, white)
    textRec2 =tex2.get_rect()
    textRec2= (140,100)
    tex3 = font.render(rule3, True, white)
    textRec3 =tex3.get_rect()
    textRec3= (140,140)
    tex4 = font.render(rule4, True, white)
    textRec4 =tex4.get_rect()
    textRec4= (140,180)
    tex5 = font.render(rule5, True, white)
    textRec5 =tex5.get_rect()
    textRec5= (140,220)
    tex6 = font.render(rule6, True, white)
    textRec6 =tex6.get_rect()
    textRec6= (140,260)
    tex7 = font.render(exit_rule, True, white)
    textRec7 =tex7.get_rect()
    textRec7= (140,320)
    while True:
        display_surface.fill(black)
        display_surface.blit(text, textRect)
        display_surface.blit(tex1 , textRec1)
        display_surface.blit(tex2 , textRec2)
        display_surface.blit(tex3 , textRec3)
        display_surface.blit(tex4 , textRec4)
        display_surface.blit(tex5 , textRec5)
        display_surface.blit(tex6 , textRec6)
        display_surface.blit(tex7 , textRec7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoopLvl1()
            pygame.display.update()

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)   #render- screen displayed below and text on top
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):  #Funct to incr len of snake
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [150, 180])

def gameLoopLvl1():
    pygame.display.set_caption('Snake Game ~ aDITHYA')
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
     if Length_of_snake<=5:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press A-Play Again or Q-Quit", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameLoopLvl1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width:
            x1=0
        if x1 < 0:
            x1=dis_width
        if y1 >= dis_height:
            y1=0
        if y1 < 0:
            y1=dis_height
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
     else:
        message("Congrats!!! Level 2 begins in 3 seconds...", white)
        pygame.display.update()
        time.sleep(3)
        gameLoopLvl2()
    pygame.quit()
    quit()

def gameLoopLvl2():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
     if Length_of_snake <= 5:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press A-Play Again or Q-Quit", white)
            Your_score(Length_of_snake+4)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameLoopLvl1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake+4)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
     else:
        message("Congrats!!! Level 3 begins in 3 seconds...", white)
        pygame.display.update()
        time.sleep(3)
        gameLoopLvl3()
    pygame.quit()
    quit()

def gameLoopLvl3():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
    obstructx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    obstructy = round(random.randrange(35, dis_width - snake_block) / 10) * 10
    while not game_over:
     if Length_of_snake <=5:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press A-Play Again or Q-Quit", white)
            Your_score(Length_of_snake+9)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameLoopLvl1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [obstructx, obstructy, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake+9)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        if (x1== obstructx and y1 == obstructy):
            game_close=True
        clock.tick(snake_speed+5)
     else:
        message("Congrats!!! Level 4 begins in 3 seconds...", white)
        pygame.display.update()
        time.sleep(3)
        gameLoopLvl4()
    pygame.quit()
    quit()

def gameLoopLvl4():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
    obstructx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    obstructy = round(random.randrange(35, dis_width - snake_block) / 10) * 10
    obstructx1 = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    obstructy1 = round(random.randrange(35, dis_width - snake_block) / 10) * 10
    obstructx2 = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    obstructy2 = round(random.randrange(35, dis_width - snake_block) / 10) * 10
    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press A-Play Again or Q-Quit", white)
            Your_score(Length_of_snake+14)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameLoopLvl1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [obstructx, obstructy, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [obstructx1, obstructy1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [obstructx2, obstructy2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake+14)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            obstructx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            obstructy = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
            obstructx1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            obstructy1 = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
            obstructx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            obstructy2 = round(random.randrange(35, dis_height - snake_block) / 10.0) * 10.0
        if (x1== obstructx and y1 == obstructy) or (x1== obstructx1 and y1== obstructy1) or (x1==obstructx2 and y1== obstructy2):
            game_close=True
        clock.tick(snake_speed+10)
    pygame.quit()
    quit()
rules()