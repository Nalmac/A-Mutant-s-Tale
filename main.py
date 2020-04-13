#A mutant's tale
#
#Author : Simon Maciag


import pygame
from pygame.locals import *
pygame.init()

import classes.Player as p
import classes.Level as l

level1 = l.Level()
menu = l.Menu()
menu.display()
perso = p.Player(level1)
boss = p.BadGuy(level1, perso)
pygame.display.flip()

Menu = True
Level1 = True
keepGoing = True
while keepGoing:
	while Menu:
		for event in pygame.event.get():
			if event.type == QUIT:
				keepGoing = False
				Level1 = False
				Menu = False
			if event.type == KEYDOWN:
				if event.key == K_F1:
					Menu = False
					level1.display()
					level1.window.blit(perso.current_sprite, perso.rect)
					perso.stats()
					pygame.display.flip()
	while Level1 and not perso.dead:
		boss.scan()
		for event in pygame.event.get():
			if event.type == QUIT:
				keepGoing = False
				Level1 = False
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					perso.move("right")
				if event.key == K_LEFT:
					perso.move("left")
				if event.key == K_UP:
					perso.move("top")
				if event.key == K_DOWN:
					perso.move("bottom")
				if event.key == K_a:
					perso.arm()
				if event.key == K_z:
					perso.Attack("top")
				if event.key == K_q:
					perso.Attack("left")
				if event.key == K_d:
					perso.Attack("right")
				if event.key == K_s:
					perso.Attack("bottom")
