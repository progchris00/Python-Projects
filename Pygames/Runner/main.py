import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 100)
end_font = pygame.font.Font("font/Pixeltype.ttf", 20)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()


snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

score_surf = test_font.render('Ang Pogi ko', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 90))

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

    if game_active:       
        screen.blits([(sky_surface, (0, 0)), (ground_surface, (0, 300))])
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        screen.blit(score_surf, score_rect)

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
    # else:
    #     screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60)
