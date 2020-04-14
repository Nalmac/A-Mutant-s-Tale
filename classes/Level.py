#A mutant's tale
#
#Author : Simon Maciag


#Modules importation and init

import pygame
from pygame.locals import*
pygame.init()

import classes.constants as c

#Levels classes
class Level():
	"""A basic level, that will eventually be used as a super class for some others"""
	def __init__(self, boss = 0):
		self.dimensions = c.LEVEL_PIXEL_DIMENSIONS
		self.time = True
		self.window = pygame.display.set_mode(self.dimensions)
		pygame.display.set_caption("A mutant's tale")
		self.background = pygame.image.load("assets/levels/background.jpeg")
		self.rock = pygame.image.load("assets/levels/Rock.png").convert_alpha()
		self.badguy = boss
		self.walls = []
		with open("assets/levels/level1.txt", 'r') as file:
			for line in file:
				chars = line.split(" ")
				self.walls.append(chars)


	def display(self):
		self.window.blit(self.background, (0, 0))
		ligne = 0
		for line in self.walls:
			col = 0
			for case in line:
				if case != "\n":
					x = col * c.SPRITE_SIZE
					y = ligne * c.SPRITE_SIZE
					if case == "R":
						self.window.blit(self.rock, (x, y))
				col += 1
			ligne += 1
		if self.badguy.display:
			self.window.blit(self.badguy.current_sprite, self.badguy.rect)

class Menu(Level):
		"""docstring for MenuLevel"""
		def __init__(self):
			Level.__init__(self)
			self.background = pygame.image.load("assets/levels/menu.jpg").convert_alpha()
			self.walls = []
			self.rock = 0

		def display(self):
			self.window.blit(self.background, (0, 0))
				