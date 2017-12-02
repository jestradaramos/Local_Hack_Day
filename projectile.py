import pygame
import math

class Projectile(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		width = 10
		height = 5
		
		self.image = pygame.Surface([width,height])
		self.image.set_alpha(128)
		self.image.fill((255,255,0))

		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.start_x = x
		self.start_y = y

		self.change_x = 10
		
		self.shooting = False

	def update(self):
		if self.shooting == True:
			on_screen = self.check_bounds()
			if on_screen:
				self.rect.x += self.change_x
				self.rect.y = math.sin(self.rect.x * 0.01) * 30 + self.start_y
			else:
				self.reset()
	
	def shoot(self, player):
		self.shooting = True
		self.rect.x = player.rect.x
		self.rect.y = player.rect.y
		self.start_x = player.rect.x
		self.start_y = player.rect.y

	def check_bounds(self):
		if self.rect.x > 2000:
			return False
		return True
	def reset(self):
		self.shooting = False
		self.rect.x = -100
		self.rect.y = -100

