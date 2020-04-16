#A mutant's tale
#
#Author : Simon Maciag


import pygame
from pygame.locals import *
pygame.init()

import classes.Player as p
import classes.Level as l
import classes.Mob as m
import threading as t
import multiprocessing as multi
import random
import time

level1 = l.Level()
menu = l.Menu()
perso = p.Player(level1)
boss1 = m.Officer(10, 16, level1, 1)
pygame.display.flip()

Menu = True
Level1 = True
keepGoing = True
i = 0
while keepGoing:
	while Menu:
		menu.display()
		pygame.display.flip()
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

	while level1.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 30)
			if event.type == QUIT:
				for mob in level1.mob:
					mob.alive = False
				keepGoing = False
				level1.loop = False
				break
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					perso.move("bottom")
				if event.key == K_UP:
					perso.move("top")
				if event.key == K_LEFT:
					perso.move("left")
				if event.key == K_RIGHT:
					perso.move("right")
				if event.key == K_a:
					perso.arm()
				if event.key == K_z:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("top",)).start()
						pass
					else :
						pass
						perso.Attack("top") 
				if event.key == K_q:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("left",)).start()
						pass
					else :
						pass
						perso.Attack("left") 
				if event.key == K_d:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("right",)).start()
						pass
					else : 
						pass
						perso.Attack("right") 
				if event.key == K_s:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("bottom",)).start()
						pass
					else : 
						pass
						perso.Attack("bottom") 
				if event.key == K_p:
					t.Thread(target=perso.powermodeToggle).start()
				if event.key == K_SPACE:
					perso.ult()
				for mob in level1.mob:
					mob.scan()
				i += 1
				time.sleep(0.2)
				if i % num == 0:
					player.stamina += 1
					level1.badguy.Attack()

				
	break