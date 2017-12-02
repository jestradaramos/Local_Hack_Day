from platform import *

bg = pygame.image.load('background.png')
class Level():

	def __init__(self, player, lop):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
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
level_1 = [ [80, 20, 200, 900], 
			[80, 20, 300, 800],
			[80, 30, 400, 700],
			[80, 30, 500, 600]]
