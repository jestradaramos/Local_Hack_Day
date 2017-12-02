import pygame 

class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()

		width = 40
		height = 60

		self.image = pygame.Surface([width,height])
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()

		self.change_x = 0
		self.change_y = 0

		self.level = None

	def update(self):
		self.gravity()

		self.rect.x += self.change_x

		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_x > 0: 
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right

		self.rect.y += self.change_y

		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_y > 0: 
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
		self.change_y = 0


	def gravity(self):
		if self.change_y == 0:
			self.change_y = 10
		else:
			self.change_y += 1

		if self.rect.y >= 800 - self.rect.height and self.change_y >= 0:
			self.change_y = 0;
			self.rect.y = 800 - self.rect.height

	def go_left(self):
		self.change_x = -6
	def go_right(self):
		self.change_x = 6
	def stop(self):
		self.change_x = 0

	def jump(self):
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2

		if len(platform_hit_list) > 0 or self.rect.bottom >= 800:
			self.change_y = -150
	

