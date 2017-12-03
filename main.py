import pygame
from player import *
from platform import *
from level import *
from projectile import *
from enemy import *
pygame.init()
width = 1500
height = 990
gameDisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption('Local Hack')
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)



running = True
score = 0
player = Player()
player.rect.x = 50
player.rect.y = 500

enemy = Enemy()
enemy.rect.x = 1200
enemy.rect.y = 860
enemy1 = Enemy()
enemy1.rect.x = 700
enemy1.rect.y = 860
enemy2 = Enemy()
enemy2.rect.x = 300
enemy2.rect.y = 860
enemy3 = Enemy()
enemy3.rect.x = 1550
enemy3.rect.y = 520
enemies = [enemy, enemy1, enemy2, enemy3]
level1 = Level(player, enemies, level_1)

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
for enemy in enemies:
	enemy.level = level1


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

	
	collision = pygame.sprite.spritecollide(player, level1.enemy_list, True)
	if collision:

		running = False
		print("You lose")
	for project in projectile:	
		collisions = pygame.sprite.spritecollide(project, level1.enemy_list, True) 
		if collisions:
			score += 1
			project.reset()
	if score == 4: 
		print("You win!")
		running = False
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
