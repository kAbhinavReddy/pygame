import pygame
import math
import random
from pygame  import  mixer
pygame.init()
screen = pygame.display.set_mode((800, 600))
# back ground
background = pygame.image.load('PycharmProjects/hello/background.jpg')
# background sound
mixer.music.load('PycharmProjects/hello/background.wav')
mixer.music.play(-1)
pygame.display.set_caption("space game")

icon = pygame.image.load('PycharmProjects/hello/transport.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('PycharmProjects/hello/space.png')
playerx = 370
playery = 500
playerx_change = 0
# enemy
enemyImg = pygame.image.load('PycharmProjects/django/enemy.png')
enemyx = random.randint(0, 768)
enemyy = random.randint(50, 150)
enemyx_change = 3
enemyy_change = 40
bulletImg = pygame.image.load('PycharmProjects/hello/miscellaneous.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 5
bullet_state = "ready"
score_v=0
font=pygame.font.Font('freesansbold.ttf',32)
testx=10
testy=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def game_over():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))


def show_score(x,y):
    score=font.render("score:"+str(score_v),True,(255,255,255))
    screen.blit(score,(x,y))



def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x,y))
def  iscollesion(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2))
    if distance<40:
        return True
    else:
        return  False
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('PycharmProjects/hello/laser.wav')
                    bullet_sound.play()
                    bulletx=playerx
                    fire_bullet(playerx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerx_change = 0
    # boundaries
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    if playerx >= 768:
        playerx = 768
    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 3
        enemyy += enemyy_change
    elif enemyx >= 768:
        enemyx_change = -3
        enemyy += enemyy_change
    if enemyy>440:
        enemyy=2000
        game_over()


    #bullet movement
    if bullety<=0:
        bullety=480
        bullet_state="ready"
    if bullet_state=="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    collision=iscollesion(enemyx,enemyy,bulletx,bullety)
    if collision:
        explosion_sound=mixer.Sound('PycharmProjects/hello/explosion.wav')
        explosion_sound.play()
        bullety=480
        bullet_state="ready"
        score_v+=1
        enemyx = random.randint(0, 768)
        enemyy = random.randint(50, 150)
    player(playerx, playery)
    enemy(enemyx, enemyy)
    show_score(testx,testy)
    pygame.display.update()
