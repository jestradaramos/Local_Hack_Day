import pygame 
#import spritesheet
#ss = spritesheet('hero_spritesheet.png')

image = pygame.image.load('trump.png')

class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()

		width = 40
		height = 60
		self.sprites = [(34,111,60,71), 
						(134,118,63,72), 
						(234,115,61,73),
						(333,112,62,70),
						(434,118,63,69),
						(534,116,61,70)]
		self.sprite_index = 0
		self.images = []
		self.images.append(image.subsurface(self.sprites[0]))
		self.images.append(image.subsurface(self.sprites[1]))
		self.images.append(image.subsurface(self.sprites[2]))
		self.images.append(image.subsurface(self.sprites[3]))
		self.images.append(image.subsurface(self.sprites[4]))
		self.images.append(image.subsurface(self.sprites[5]))
		self.image = self.images[self.sprite_index]
		self.rect = self.image.get_rect()

		self.tick = 0
		self.change_tick = 1
		self.change_x = 6
		self.change_y = 0

		self.level = None

	def update(self):
		
		self.gravity()
		self.tick += self.change_tick
		if self.tick > 2:
			self.sprite_index += 1
			if self.sprite_index > 5: 
				self.sprite_index = 0
			self.image = self.images[self.sprite_index]
			self.tick = 0

		self.rect.x += self.change_x

		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_x > 0: 
				self.rect.right = block.rect.left
				self.go_left()
			elif self.change_x < 0:
				self.rect.left = block.rect.right
				self.go_right()


	def gravity(self):
		if self.change_y == 0:
			self.change_y = 10
		else:
			self.change_y += 1

		if self.rect.y >= 990 - self.rect.height and self.change_y >= 0:
			self.change_y = 0;
			self.rect.y = 990 - self.rect.height

	def go_left(self):
		self.change_x = -6
		self.change_tick = 1
	def go_right(self):
		self.change_x = 6
		self.change_tick = 1
	def stop(self):
		self.change_x = 0
		self.change_tick = 0

	def jump(self):
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2

		if len(platform_hit_list) > 0 or self.rect.bottom >= 990:
			self.change_y = -150
	

