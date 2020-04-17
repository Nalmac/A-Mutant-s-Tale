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

level1 = l.Level(1)
level2 = l.Level(2)
menu = l.Menu()
perso = p.Player([level1, level2])
level2.player = perso
boss1 = m.Officer(10, 16, level1, 1)
boss2 = m.Officer(7, 1, level2, 2)
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
			num = random.randint(1, 15)
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
					perso.stamina += 1 if perso.stamina < 5 else 0
					level1.badguy.Attack()

	
	while level2.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 15)
			if event.type == QUIT:
				for mob in level2.mob:
					mob.alive = False
				keepGoing = False
				level2.loop = False
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
				for mob in level2.mob:
					mob.scan()
				i += 1
				time.sleep(0.2)
				if i % num == 0 or i % num <= 0.5:
					perso.stamina += 1 if perso.stamina < 5 else 0
					level2.badguy.Attack()

	break