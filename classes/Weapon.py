#A mutant's tale
#Simon Maciag

import pygame
import time
import classes.constants as c

class Weapon():
	def __init__(self, player):
		self.sprites = []
		self.level = player.level
		self.player = player
		for i in range(1, 5):
			self.sprites.append(pygame.image.load("assets/player/weapon/" + str(i) + ".png").convert_alpha())
		
		self.current_sprite = self.sprites[0]
		self.rect = self.current_sprite.get_rect()
		self.case_x = player.case_x
		self.case_y = player.case_y
		self.x = c.SPRITE_SIZE * self.case_x
		self.y = c.SPRITE_SIZE * self.case_y
		self.rect.move(self.x, self.y)

	def move(self, x, y):
		self.rect = self.rect.move(x, y)
		if x > 0:
			self.case_x += 1
		elif x < 0:
			self.case_x -= 1
		elif y < 0:
			self.case_y -= 1
		elif y > 0:
			self.case_y += 1
	
	def attack(self, direction):
		for i in range(5):
			if direction == "right":
				if self.case_x + 1 <= 30 and self.level.walls[self.case_y][self.case_x + 1] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(c.SPRITE_SIZE, 0)
					self.case_x += 1
			if direction == "left":
				if self.case_x - 1 >= 0 and self.level.walls[self.case_y][self.case_x - 1] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(-c.SPRITE_SIZE, 0)
					self.case_x -= 1
			if direction == "top":
				if self.case_y - 1 >= 0 and self.level.walls[self.case_y - 1][self.case_x] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(0, -c.SPRITE_SIZE)
					self.case_y -= 1
				else:
					break
			if direction == "bottom" and self.level.walls[self.case_y + 1][self.case_x] != "R":
				time.sleep(0.2)
				if self.case_y + 1 <= 20:
					self.rect = self.rect.move(0, c.SPRITE_SIZE)
					self.case_y += 1
			self.current_sprite = self.sprites[i] if i - 3 <= 0 else self.sprites[i - 3]

			self.level.display()
			self.level.window.blit(self.player.current_sprite, self.player.rect)
			self.player.stats()
			self.level.window.blit(self.current_sprite, self.rect)
			pygame.display.flip()

			if self.rect.colliderect(self.player.level.badguy.rect):
				self.player.level.badguy.health -= self.player.attack
				break

		delta_y = c.SPRITE_SIZE * (self.player.case_y - self.case_y) 		
		delta_x = c.SPRITE_SIZE * (self.player.case_x - self.case_x)
		self.rect = self.rect.move(delta_x, delta_y)

		self.case_x += int(delta_x / c.SPRITE_SIZE)
		self.case_y += int(delta_y / c.SPRITE_SIZE)
		self.level.display()
		self.player.stats()
		self.level.window.blit(self.player.current_sprite, self.player.rect)
		pygame.display.flip()

class BossWeapon(Weapon):
	"""docstring for BossWeapon"""
	def __init__(self, boss, target):
		super(BossWeapon, self).__init__(boss)
		self.target = target
		self.boss = boss
		self.sprites = [
			pygame.image.load("assets/FinalBoss/Weapon/Right.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Weapon/Left.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Weapon/Top.png").convert_alpha(),
			pygame.image.load("assets/FinalBoss/Weapon/Bottom.png").convert_alpha()
		]

		self.current_sprite = 0
		self.rect = self.boss.rect
		#self.rect.move(case_x  * c.SPRITE_SIZE, case_y * c.SPRITE_SIZE)

	def attack(self, direction):
		for i in range(5):
			if direction == "right":
				self.current_sprite = self.sprites[0]
				if self.case_x + 1 <= 30 and self.level.walls[self.case_y][self.case_x + 1] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(c.SPRITE_SIZE, 0)
					self.case_x += 1
					
			if direction == "left":
				self.current_sprite = self.sprites[1]
				if self.case_x - 1 >= 0 and self.level.walls[self.case_y][self.case_x - 1] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(-c.SPRITE_SIZE, 0)
					self.case_x -= 1
					
			if direction == "top":
				self.current_sprite = self.sprites[2]
				if self.case_y - 1 >= 0 and self.level.walls[self.case_y - 1][self.case_x] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(0, -c.SPRITE_SIZE)
					self.case_y -= 1
					
			if direction == "bottom":
				self.current_sprite = self.sprites[3]
				if self.case_y + 1 <= 20 and self.level.walls[self.case_y + 1][self.case_x] != "R":
					time.sleep(0.2)
					self.rect = self.rect.move(0, c.SPRITE_SIZE)
					self.case_y += 1
					

			self.level.display()
			self.level.window.blit(self.boss.current_sprite, self.boss.rect)
			self.level.window.blit(self.target.current_sprite, self.target.rect)
			self.level.window.blit(self.current_sprite, self.rect)
			self.target.stats()

			if self.rect.colliderect(self.target.rect):
				self.target.damage(self.boss.attack)
				print(self.target.health)
				print("attack")
				break

		delta_y = c.SPRITE_SIZE * (self.boss.case_y - self.case_y) 		
		delta_x = c.SPRITE_SIZE * (self.boss.case_x - self.case_x)
		self.rect = self.rect.move(delta_x, delta_y)

		self.case_x += int(delta_x / c.SPRITE_SIZE)
		self.case_y += int(delta_y / c.SPRITE_SIZE)
		self.level.display()
		self.player.stats()
		self.level.window.blit(self.player.current_sprite, self.player.rect)
		self.level.window.blit(self.target.current_sprite, self.target.rect)
		pygame.display.flip()