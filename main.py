import pygame
from player import *
from platform import *
from level import *

pygame.init()
width = 2000
height = 800
gameDisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption('Local Hack')
running = True

player = Player()
player.rect.x = 100
player.rect.y = 700

level1 = Level(player, level_1)

active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)

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
