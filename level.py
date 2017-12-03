from platform import *

bg = pygame.image.load('background.png')
class Level():

	def __init__(self, player,enemies, lop):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		for enemy in enemies:
			self.enemy_list.add(enemy)
		self.player = player

		for platform in lop:
			block = Platform(platform[0], platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			self.platform_list.add(block)

		self.world_shift = 0

	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		screen.fill((255,255,255))
		screen.blit(bg, (0,0))	

		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

	def shift_world(self, shift_x):
		self.world_shift += shift_x

		for platform in self.platform_list:
			platform.rect.x += shift_x

		for enemy in self.enemy_list:
			enemy.rect.x += shift_x
		
# level format
# [width, height, x, y] 
level_1 = [ [80, 30, 200, 900], 
			[80, 30, 300, 800],
			[80, 30, 400, 700],
			[80, 30, 500, 600],
			[100, 690, 600, 600],
			[50, 30, 700, 500],
			[300, 400, 800, 540],
			[2500, 50, 0, 940],
			[300, 100, 1700, 890],
			[50, 200, 1300, 400],
			[50, 200, 1600, 400],
			[350, 50, 1300, 600]]
