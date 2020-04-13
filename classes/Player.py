import pygame
from pygame.locals import*
pygame.init()

import classes.constants as c
import classes.Weapon as w
import time

class Player():
	"""docstring for Player"""
	def __init__(self, level):
		self.level = level
		self.powermode = False
		self.health = c.HEALTH
		self.attack = c.ATTACK
		self.stamina = c.STAMINA
		self.exp = 0
		self.armed = False
		self.dead = False

		self.health_sprites = [
			pygame.image.load("assets/player/health/health_full.png").convert_alpha(),
			pygame.image.load("assets/player/health/health_half.png").convert_alpha()
		]

		self.stamina_sprites = [
			pygame.image.load("assets/player/stamina/full_stamina.png").convert_alpha(),
			pygame.image.load("assets/player/stamina/almost_full_stamina.png").convert_alpha(),
			pygame.image.load("assets/player/stamina/mid_stamina.png").convert_alpha(),
			pygame.image.load("assets/player/stamina/quart_stamina.png").convert_alpha(),
			pygame.image.load("assets/player/stamina/low_stamina.png").convert_alpha(),

		]

		self.powermode_sprites = [
			pygame.image.load("assets/player/LeftPowermode.png").convert_alpha(),
			pygame.image.load("assets/player/RightPowermode.png").convert_alpha()
		]

		self.sprites = [
			pygame.image.load("assets/player/Right.png").convert_alpha(),
			pygame.image.load("assets/player/Left.png").convert_alpha(),
			pygame.image.load("assets/player/RightArmed.png").convert_alpha(),
			pygame.image.load("assets/player/LeftArmed.png").convert_alpha()
		]

		self.current_sprite = self.sprites[0]

		self.rect = self.current_sprite.get_rect()

		self.case_x = 0
		self.case_y = 0

		self.weapon = w.Weapon(self)

		self.level.window.blit(self.current_sprite, self.rect)

	def powermodeToggle(self):
		if not self.powermode:
			if self.stamina == 5:
				self.powermode = True
				self.health += 10
				self.attack += 10
		else:
			self.powermode = False
			self.health = c.HEALTH
			self.attack = c.ATTACK

	def stats(self):
		ligne = 0
		for line in self.level.walls:
			col = 0
			for case in line:
				if case != "\n":
					x = col * c.SPRITE_SIZE
					y = ligne * c.SPRITE_SIZE
					letter = case
					if letter == "H":
						if self.health == 6:
							for i in range(3):
								self.level.window.blit(self.health_sprites[0], (x, y))
								x -= 30
						if self.health == 5:
							self.level.window.blit(self.health_sprites[1], (x, y))
							x -= 1
							for i in range(2):
								self.level.window.blit(self.health_sprites[0], (x, y))
								x -= 1
						if self.health == 4:
							for i in range(2):
								self.level.window.blit(self.health_sprites[0], (x, y))
								x -= 1
						if self.health == 3:
							self.level.window.blit(self.health_sprites[1], (x, y))
							x -= 1
							for i in range(1):
								self.level.window.blit(self.health_sprites[0], (x, y))
								x -= 1
						if self.health == 2:
							self.level.window.blit(self.health_sprites[0], (x, y))
						if self.health == 1:
							self.level.window.blit(self.health_sprites[1], (x, y))
						if self.health == 0:
							self.dead = True

					if case == "s":
						if self.stamina == 5:
							self.level.window.blit(self.stamina_sprites[0], (x, y))
							self.zawarudo = True
						if self.stamina == 4:
							self.level.window.blit(self.stamina_sprites[1], (x, y))
							self.zawarudo = False
						if self.stamina == 3:
							self.level.window.blit(self.stamina_sprites[2], (x, y))
						if self.stamina == 2:
							self.level.window.blit(self.stamina_sprites[3], (x, y))
						if self.stamina == 1:
							self.level.window.blit(self.stamina_sprites[4], (x, y))
							
				col += 1
			ligne += 1
		pygame.display.flip()

	def move(self, direction):
		if direction == "right":
			if self.case_x + 1 <= 30 and self.level.walls[self.case_y][self.case_x + 1] != "R":
				self.rect = self.rect.move(c.SPRITE_SIZE, 0)
				self.weapon.move(c.SPRITE_SIZE, 0)
				self.case_x += 1
				self.current_sprite = self.sprites[0] if not self.armed else self.sprites[2]
		if direction == "left":
			if self.case_x - 1 >= 0 and self.level.walls[self.case_y][self.case_x - 1] != "R":
				self.rect = self.rect.move(-c.SPRITE_SIZE, 0)
				self.weapon.move(-c.SPRITE_SIZE, 0)
				self.current_sprite = self.sprites[1] if not self.armed else self.sprites[3]
				self.case_x -= 1
		if direction == "top":
			if self.case_y - 1 >= 0 and self.level.walls[self.case_y - 1][self.case_x] != "R":
				self.rect = self.rect.move(0, -c.SPRITE_SIZE)
				self.weapon.move(0, -c.SPRITE_SIZE)

				self.case_y -= 1
		if direction == "bottom" and self.level.walls[self.case_y + 1][self.case_x] != "R":
			if self.case_y + 1 <= 20:
				self.rect = self.rect.move(0, c.SPRITE_SIZE)
				self.weapon.move(0, c.SPRITE_SIZE)
				self.case_y += 1
		self.level.display()
		self.stats()
		self.level.window.blit(self.current_sprite, self.rect)
		pygame.display.flip()

	def arm(self, t = 0):
		if t == 0:	
			time.sleep(0.5)
		if self.current_sprite == self.sprites[0]:
			self.current_sprite = self.sprites[2]
			self.armed = True
		elif self.current_sprite == self.sprites[1]:
			self.current_sprite = self.sprites[3]
			self.armed = True
		elif self.current_sprite == self.sprites[2]:
			self.current_sprite = self.sprites[0]
			self.armed = False
		else:
			self.current_sprite = self.sprites[1]
			self.armed = False

		self.level.display()
		self.stats()
		self.level.window.blit(self.current_sprite, self.rect)
		pygame.display.flip()

	#Ici le 2 dans self.arm() importe peu, c'est juste pour signifier à la méthode qu'on ne veut
	#pas qu'elle attende
	def Attack(self, direction):
		if self.armed:
			self.arm(2)
			self.weapon.attack(direction)
			self.arm(2)
		else:
			self.arm()
			time.sleep(0.1)
			self.arm(2)
			self.weapon.attack(direction)
			self.arm()

		if self.stamina < 5:
			self.stamina += 1
		self.stats()
		pygame.display.flip()

class BadGuy(Player):
	"""docstring for BadGuy"""
	def __init__(self, level):
		super(BadGuy, self).__init__(level)
		self.level.badguy = self
		self.sprites = [
			pygame.image.load("assets/FinalBoss/Left.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Right.png").convert_alpha()
		]
		self.powermode_sprites = [
			pygame.image.load("assets/FinalBoss/Left_Powermode.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Right_Powermode.png").convert_alpha()
		]
		self.current_sprite = self.sprites[0]
		self.rect = self.current_sprite.get_rect().move(475, 330)
		self.case_x = 16
		self.case_y = 15
		