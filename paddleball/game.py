import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Unpredicta-Ball")
clock = pygame.time.Clock()
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, 1000)
ball_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() //2)
ball_hb_pos = pygame.Vector2((screen.get_width() // 2) - 15 , (screen.get_height() //2) - 15)
ball_direction = pygame.Vector2(screen.get_width() / 2, 1080)


while True:
    for event in pygame.event.get(): #quit checker
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    screen.fill("black")

    paddleft = pygame.Rect((player_pos.x - 30, player_pos.y),(30,20))
    paddmid = pygame.Rect(player_pos,(30,20))
    paddright = pygame.Rect((player_pos.x + 30, player_pos.y),(30,20))
    ball_hitbox = pygame.Rect(ball_hb_pos, (30,30))
    pygame.draw.rect(screen, "white", paddmid)
    pygame.draw.rect(screen, "white", paddleft)
    pygame.draw.rect(screen,"white", paddright)
    pygame.draw.rect(screen,"white", ball_hitbox)
    pygame.draw.circle(screen, "white", ball_pos, 20)




    keys = pygame.key.get_pressed()  
    if keys[pygame.K_a]:
        if player_pos.x >= 0:
            player_pos.x -= 500 * dt
    if keys[pygame.K_d]:
        if player_pos.x <= 1840:
            player_pos.x += 500 * dt


    if ball_hitbox.colliderect(paddmid):
        coin = random.randint(1,2)
        if coin == 1:
            ball_direction = pygame.Vector2(ball_pos.x * random.uniform(1,1.8), 10)
        if coin == 2:
            ball_direction = pygame.Vector2(ball_pos.x / random.uniform(1,1.8), 10)
    if ball_hitbox.colliderect(paddleft):
        ball_direction = pygame.Vector2(ball_direction.x / random.uniform(1,3.5) , 10)
    if ball_hitbox.colliderect(paddright):
        ball_direction = pygame.Vector2(ball_direction.x * random.uniform(1,3.5) , 10)
    if ball_hitbox.y <= 1:
        coin = random.randint(1,2)
        if coin == 1:
            ball_direction = pygame.Vector2(ball_direction.x / random.uniform(1,2.5), 1080)
        if coin == 2:
            ball_direction = pygame.Vector2(ball_direction.x * random.uniform(1,2.5), 1080)
    if ball_hitbox.y >= (screen.get_height() - 50):
        pygame.quit()
        exit()       
    
    ball_pos = ball_pos.move_towards(ball_direction, 7)
    ball_hb_pos.x = ball_pos.x - 15
    ball_hb_pos.y = ball_pos.y - 15

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()