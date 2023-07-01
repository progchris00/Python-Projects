import pygame
from sys import exit

def display_score():
    current_time = round(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 100)
end_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()


snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))


player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand2x = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand2x.get_rect(center = (400, 200))

top_message = test_font.render("Pixel Runner", False, (111, 196, 169))
top_message_rect = top_message.get_rect(center =(400, 80))

bottom_message = end_font.render("Press space to start", False, (111, 196, 169))
bottom_message_rect = bottom_message.get_rect(center =(400, 320))

final_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
        
        if game_active:
            if player_rect.bottom == 300:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_gravity = -17
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = round(pygame.time.get_ticks() / 1000)

    if game_active:       
        screen.blits([(sky_surface, (0, 0)), (ground_surface, (0, 300))])
        final_score = display_score()

        snail_rect.left -= 6
        if snail_rect.left < -100: snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        
        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand2x, player_stand_rect)
        screen.blit(top_message, top_message_rect)  

        score_message = end_font.render(f"Your final score is {final_score}", False, "White")
        score_message_rect = score_message.get_rect(center = (400, 320))

        if final_score == 0:
            screen.blit(bottom_message, bottom_message_rect)
        
        else:
            screen.blit(score_message, score_message_rect)


            
    pygame.display.update()
    clock.tick(60)
