#!/usr/bin/python
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

import pygame
import random

#Set up some colors
WHITE = 0xffffff
BLACK = 0x000000
RED = 0xff0000

#Some size variables
WIDTH = 600
HEIGHT = 600
FOOD_SIZE = 20
SNAKE_SIZE = 20

#set w some pygame stuff
pygame.font.init()
font = pygame.font.Font(None,36)

direction = 'r'

def main():

    #Set up the main stuff
    pygame.init()
    surface = pygame.display.set_mode((WIDTH,HEIGHT))

    #local variables
    snake_head_x = 0
    snake_head_y = 0
    snake_list = [Node(snake_head_x, snake_head_y)]
    food_x = 0
    food_y = 0
    direction = 'r'
    place_food = True

    #Check for events - key presses
    while True:
        pygame.time.Clock().tick(10)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w or event.key == pygame.K_DOWN) and direction != 'd':
                    direction = "u"
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and direction != 'r':
                    direction = 'l'
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and direction !='l':
                    direction = 'r'
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and direction != 'u':
                    direction = 'd'

        snake_head = pygame.Rect(snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE)

        #move the snake_head
        snake_list.pop()
        if(direction == 'u'):
            snake_head_y -= SNAKE_SIZE
        elif(direction == 'd'):
            snake_head_y += SNAKE_SIZE
        elif(direction == 'l'):
            snake_head_x -= SNAKE_SIZE
        elif(direction == 'r'):
            snake_head_x += SNAKE_SIZE
        snake_list.insert(0, Node(snake_head_x, snake_head_y))

        #ensure snake stays in box
        if(snake_head_x < (0 - SNAKE_SIZE * 2) or snake_head_x >= (WIDTH) or snake_head_y < (0 - SNAKE_SIZE * 2) or snake_head_y > (HEIGHT + SNAKE_SIZE)):
            print('snake x' + str(snake_head_x))
            print('snake y' + str(snake_head_y))
            return






        #place a new food
        if(place_food == True):
            food_x = random.randint(0,(WIDTH-(FOOD_SIZE))/FOOD_SIZE) * FOOD_SIZE
            food_y = random.randint(0,(HEIGHT-(FOOD_SIZE))/FOOD_SIZE) * FOOD_SIZE
            place_food = False
            print('foodx' + str(food_x))
            print('foody' + str(food_y))
        food_rect = pygame.Rect(food_x, food_y, FOOD_SIZE, FOOD_SIZE)

        #check if snake eats food
        if(snake_head.colliderect(food_rect)):
            #Reset food
            place_food = True
            snake_list.append(Node(food_x,food_y))
            food_x = FOOD_SIZE * -1
            food_y = FOOD_SIZE * -1

        #check if snake self eats
        if(any(x.x == snake_head_x and x.y == snake_head_y for x in snake_list[1:len(snake_list)])):
            return




        pygame.display.update()
        surface.fill(BLACK)

        if(len(snake_list) > 1):
            for x in snake_list:
                pygame.draw.rect(surface, WHITE, pygame.Rect(x.x,x.y,FOOD_SIZE, FOOD_SIZE))
        else:
            pygame.draw.rect(surface, WHITE, snake_head)

        pygame.draw.rect(surface, RED, food_rect)






main()
input('Press ENTER to exit')
