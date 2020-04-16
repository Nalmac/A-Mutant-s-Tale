#A mutant's tale
#
#Author : Simon Maciag


#Modules importation and init

import pygame
from pygame.locals import*
pygame.init()

import classes.constants as c
import classes.Mob as m

#Levels classes
class Level():
	"""A basic level, that will eventually be used as a super class for some others"""
	def __init__(self, boss = 0, player = 0, number = 1):
		self.dimensions = c.LEVEL_PIXEL_DIMENSIONS
		self.time = True
		self.window = pygame.display.set_mode(self.dimensions)
		pygame.display.set_caption("A mutant's tale")
		self.background = pygame.image.load("assets/levels/background.jpeg")
		self.rock = pygame.image.load("assets/levels/Rock.png").convert_alpha()
		self.health_hole = pygame.image.load("assets/levels/LifeHole.png").convert_alpha()
		self.stamina_hole = pygame.image.load("assets/levels/StaminaHole.png").convert_alpha()
		self.bush = pygame.image.load("assets/levels/bush.png").convert_alpha()
		self.tree = pygame.image.load("assets/levels/tree.png").convert_alpha()
		self.portal = pygame.image.load("assets/levels/NextPortal.png").convert_alpha()
		self.portalRect = self.portal.get_rect()
		self.badguy = boss
		self.player = player
		self.it = 0
		self.loop = True
		self.mob = []
		for i in range(1): 
			self.mob.append(m.Mob(self))

		self.walls = []
		with open("assets/levels/level" + str(number) +".txt", 'r') as file:
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
					if case == "HH":
						self.window.blit(self.health_hole, (x, y))

					if case == "SH":
						self.window.blit(self.stamina_hole, (x, y))

					if case == "B":
						self.window.blit(self.bush, (x, y))

					if case == "T":
						self.window.blit(self.tree, (x, y))
					if case == "P":
						self.portalRect == self.portalRect.move(x, y)
						print(x, y)
						if not self.badguy.alive:
							self.window.blit(self.portal, self.portalRect)

					if case.split("b")[0] == "M":
						self.window.blit(self.mob[int(case.split("b")[1])].current_sprite, (x, y))
						self.mob[int(case.split("b")[1])].case_y = ligne
						self.mob[int(case.split("b")[1])].case_x = col
						if self.it == 0:
							self.mob[int(case.split("b")[1])].defRect(x, y)
							self.mob[int(case.split("b")[1])].animrect = pygame.Rect((x - 30, y - 30), (c.SPRITE_SIZE * 2, c.SPRITE_SIZE * 2))

				col += 1
			ligne += 1
		self.window.blit(self.player.current_sprite, self.player.rect)
		if self.badguy.alive:
			self.window.blit(self.badguy.current_sprite, self.badguy.rect)
		self.player.stats()

class Menu(Level):
		"""docstring for MenuLevel"""
		def __init__(self):
			Level.__init__(self)
			self.background = pygame.image.load("assets/levels/menu.jpg").convert_alpha()
			self.walls = []
			self.rock = 0

		def display(self):
			self.window.blit(self.background, (0, 0))
				