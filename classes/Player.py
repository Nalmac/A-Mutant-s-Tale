import pygame
from pygame.locals import*
pygame.init()

import classes.constants as c
import classes.Weapon as w
import time
import threading as t

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
		self.alive = True
		self.moving = False

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

		self.powermode_health_sprites = [
			pygame.image.load("assets/player/health/powermode_health_full.png").convert_alpha()
		]

		for i in range(1, 6):
			self.powermode_health_sprites.append(pygame.image.load("assets/player/health/powermode_health_" + str(i) + ".png").convert_alpha())

		self.current_sprite = self.sprites[0]

		self.rect = self.current_sprite.get_rect()

		self.case_x = 0
		self.case_y = 0

		self.weapon = w.Weapon(self)
		self.attacking = False
		self.level.player = self

		self.level.window.blit(self.current_sprite, self.rect)

	def ult(self):
		if self.level.time:
			if self.powermode:
				self.level.time = False
			else:
				t.Thread(target=self.powermodeToggle).start()
				if self.powermode:
					self.level.time = False
			self.stamina -= 5
		else:
			self.level.time = True
			self.powermodeToggle()


	def powermodeToggle(self):
		if not self.powermode:
			if self.stamina == 5:
				self.powermode = True
				self.current_sprite = self.powermode_sprites[0] if self.current_sprite == self.sprites[1] or self.current_sprite == self.sprites[3] else self.powermode_sprites[1]
				self.health += 12
				self.attack += 10
				self.level.window.blit(self.current_sprite, self.rect)
				self.stats()
				for i in range(5):
					if self.powermode:
						time.sleep(1)
						self.stamina -= 1
				t.Thread(target=self.powermodeToggle()).start()
		else:
			self.powermode = False
			if not self.armed:
				if self.current_sprite == self.powermode_sprites[1]:
					self.current_sprite = self.sprites[0]
				else:
					self.current_sprite = self.sprites[1]
			elif self.current_sprite == self.powermode_sprites[1]:
				self.current_sprite = self.sprites[2]
			else:
				self.current_sprite = self.sprites[3]
			self.level.display()
			self.level.window.blit(self.current_sprite, self.rect)
			pygame.display.flip()
			self.level.time = True
			self.health = c.HEALTH
			self.attack = c.ATTACK
			self.stats()

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
						if not self.powermode :
							if self.health == 6:
								for i in range(3):
									self.level.window.blit(self.health_sprites[0], (x, y))
									x -= 30
							if self.health == 5:
								self.level.window.blit(self.health_sprites[1], (x, y))
								x -= 30
								for i in range(2):
									self.level.window.blit(self.health_sprites[0], (x, y))
									x -= 30
							if self.health == 4:
								for i in range(2):
									self.level.window.blit(self.health_sprites[0], (x, y))
									x -= 30
							if self.health == 3:
								self.level.window.blit(self.health_sprites[1], (x, y))
								x -= 30
								self.level.window.blit(self.health_sprites[0], (x, y))
								x -= 30
							if self.health == 2:
								self.level.window.blit(self.health_sprites[0], (x, y))
							if self.health == 1:
								self.level.window.blit(self.health_sprites[1], (x, y))
							if self.health <= 0:
								self.alive = False
								self.display = False
						else:
							if self.health % 6 == 0:
								for i in range(int(self.health / 6)):
									self.level.window.blit(self.powermode_health_sprites[0], (x, y))
									x -= 30
							else:
								quot = self.health / 6
								intQuot = int(quot)
								rest = self.health - intQuot * 6

								for i in range(intQuot):
									self.level.window.blit(self.powermode_health_sprites[0], (x, y))
									x -= 30
								self.level.window.blit(self.powermode_health_sprites[rest], (x, y))


					if case == "s":
						if self.stamina == 5:
							self.level.window.blit(self.stamina_sprites[0], (x, y))
						if self.stamina == 4:
							self.level.window.blit(self.stamina_sprites[1], (x, y))
						if self.stamina == 3:
							self.level.window.blit(self.stamina_sprites[2], (x, y))
						if self.stamina == 2:
							self.level.window.blit(self.stamina_sprites[3], (x, y))
						if self.stamina == 1 or self.stamina <= 0:
							self.level.window.blit(self.stamina_sprites[4], (x, y))
							
				col += 1
			ligne += 1
		pygame.display.flip()

	def move(self, direction):
		self.moving = True
		if direction == "right":
			if self.case_x + 1 <= 30 and self.level.walls[self.case_y][self.case_x + 1] != "R":
				self.rect = self.rect.move(c.SPRITE_SIZE, 0)
				self.weapon.move(c.SPRITE_SIZE, 0)
				

				if self.level.walls[self.case_y][self.case_x + 1] == "HH":
					self.health += 1 if self.health < 6 else 0

				if self.level.walls[self.case_y][self.case_x + 1] == "SH":
					self.stamina += 1 if self.stamina < 5 else 0

				if not self.powermode:
					self.current_sprite = self.sprites[0] if not self.armed else self.sprites[2]
				else:
					self.current_sprite = self.powermode_sprites[1]
				self.case_x += 1
		if direction == "left":
			if self.case_x - 1 >= 0 and self.level.walls[self.case_y][self.case_x - 1] != "R":
				self.rect = self.rect.move(-c.SPRITE_SIZE, 0)
				self.weapon.move(-c.SPRITE_SIZE, 0)
				if not self.powermode:
					self.current_sprite = self.sprites[1] if not self.armed else self.sprites[3]
				else:
					self.current_sprite = self.powermode_sprites[0]

				if self.level.walls[self.case_y][self.case_x - 1] == "HH":
					self.health += 1 if self.health < 6 else 0

				if self.level.walls[self.case_y][self.case_x - 1] == "SH":
					self.stamina += 1 if self.stamina < 5 else 0

				self.case_x -= 1
		if direction == "top":
			if self.case_y - 1 >= 0 and self.level.walls[self.case_y - 1][self.case_x] != "R":
				self.rect = self.rect.move(0, -c.SPRITE_SIZE)
				self.weapon.move(0, -c.SPRITE_SIZE)

				if self.level.walls[self.case_y - 1][self.case_x] == "HH":
					self.health += 1 if self.health < 6 else 0

				if self.level.walls[self.case_y - 1][self.case_x] == "SH":
					self.stamina += 1 if self.stamina < 5 else 0

				self.case_y -= 1
		if direction == "bottom" and self.level.walls[self.case_y + 1][self.case_x] != "R":
			if self.case_y + 1 <= 20:
				self.rect = self.rect.move(0, c.SPRITE_SIZE)
				self.weapon.move(0, c.SPRITE_SIZE)
				if self.level.walls[self.case_y + 1][self.case_x] == "HH":
					self.health += 1 if self.health < 6 else 0
				if self.level.walls[self.case_y - 1][self.case_x] == "SH":
					self.stamina += 1 if self.stamina < 5 else 0
				self.case_y += 1
		self.level.display()
		self.stats()
		self.level.window.blit(self.current_sprite, self.rect)
		pygame.display.flip()
		self.moving = False

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
		self.attacking = True
		if self.armed:
			if not self.powermode : self.arm(2)
			self.weapon.attack(direction)
			if not self.powermode : self.arm(2)
		else:
			if not self.powermode : self.arm()
			time.sleep(0.1)
			if not self.powermode : self.arm(2)
			self.weapon.attack(direction)
			if not self.powermode : self.arm()

		if self.stamina < 5:
			self.stamina += 1
		self.stats()
		self.attacking = False
		pygame.display.flip()

	def damage(self, dmg):
		if self.stamina > 0:
			dmg -= 2
			self.stamina -= 1
		if dmg >= 0:
			self.health -= dmg
		self.stats()

class BadGuy(Player):
	"""docstring for BadGuy"""
	def __init__(self, level, player):
		super(BadGuy, self).__init__(level)
		self.level.badguy = self
		self.player = player
		self.sprites = [
			pygame.image.load("assets/FinalBoss/Left.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Right.png").convert_alpha()
		]
		self.powermode_sprites = [
			pygame.image.load("assets/FinalBoss/Left_Powermode.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Right_Powermode.png").convert_alpha()
		]
		self.current_sprite = self.sprites[0]
		self.case_x = 16
		self.case_y = 15
		self.rect = self.current_sprite.get_rect().move(self.case_x * c.SPRITE_SIZE, self.case_y * c.SPRITE_SIZE)
		self.weapon = w.BossWeapon(self, self.player)
		print(self.weapon.x, self.weapon.y)
		self.stamina = c.B_STAMINA
		self.attack = c.B_ATTACK
		self.health = c.B_HEALTH
	
	def Attack(self, direction):
		self.attacking = True
		self.weapon.attack(direction)
		self.player.stats()
		self.attacking = False

	def scan(self):
		delta_x = c.SPRITE_SIZE * (self.player.case_x - self.case_x)
		delta_y = c.SPRITE_SIZE * (self.player.case_y - self.case_y)
		maxNeg = -5 * c.SPRITE_SIZE
		maxPos = 5 * c.SPRITE_SIZE

		if delta_x == 0 and delta_y < 0 and delta_y >= maxNeg:
			if not self.player.attacking and not self.player.moving:
				thread = t.Thread(target=self.Attack, args=("top",))
			else:
				self.Attack("top")
				thread = 0
		elif delta_x == 0 and delta_y > 0 and delta_y <= maxPos:
			if not self.player.attacking and not self.player.moving:
				thread = t.Thread(target=self.Attack, args=("bottom",))
			else:
				thread = 0
				self.Attack("bottom")
		elif delta_y == 0 and delta_x < 0 and delta_x >= maxNeg:
			self.current_sprite = self.sprites[0]
			if not self.player.attacking and not self.player.moving:
				thread = t.Thread(target=self.Attack, args=("left",))
			else:
				thread = 0
				self.Attack("left")
		elif delta_y == 0 and delta_x > 0 and delta_x <= maxPos:
			self.current_sprite = self.sprites[1]
			if not self.player.attacking and not self.player.moving:
				thread = t.Thread(target=self.Attack, args=("right",))
			else:
				thread = 0
				self.Attack("right")
		else:
			if not self.powermode:
				self.powermodeToggle()
			thread = 0
		if thread != 0:
			thread.start()
		