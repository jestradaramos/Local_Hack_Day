import pygame
from player import *
from platform import *
from level import *
from projectile import *

pygame.init()
width = 1500
height = 990
gameDisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption('Local Hack')
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)



running = True

player = Player()
player.rect.x = 100
player.rect.y = 500

level1 = Level(player, level_1)

projectile = []
for i in range(10):
	projectile.append(Projectile(-100,-100))

projectile_index = 0


active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)
for project in projectile:
	active_sprite_list.add(project)


# temporary
active_sprite_list.add(projectile)

player.level = level1

clock = pygame.time.Clock()



while running:
	for event in pygame.event.get():
		print(event)

		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.go_left()
			if event.key == pygame.K_d:
				player.go_right()
			if event.key == pygame.K_w:
				player.jump()
				
			if event.key == pygame.K_SPACE:
				projectile[projectile_index].shoot(player)
				projectile_index += 1
				if projectile_index > 9: 
					projectile_index = 0

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a and player.change_x < 0:
				player.stop()
			if event.key == pygame.K_d and player.change_x > 0:
				player.stop()
		
	# Shifting of world
	if (player.rect.right >= 1000):
		diff = player.rect.right - 1000
		player.rect.right = 1000
		level1.shift_world(-diff)
	if (player.rect.left <= 120):
		diff = 120 - player.rect.left 
		player.rect.left = 120
		level1.shift_world(diff)
		
	# Update	
	level1.update()
	active_sprite_list.update()
	# Draw
	level1.draw(gameDisplay)
	active_sprite_list.draw(gameDisplay)
	
	pygame.display.flip()
	clock.tick(60)

pygame.display.update()

pygame.quit()
quit()
