#A mutant's tale
#
#Author : Simon Maciag


import pygame
from pygame.locals import *
pygame.init()

import classes.Player as p
import classes.Level as l
import threading as t
import Xlib as x

level1 = l.Level()
menu = l.Menu()
perso = p.Player(level1)
boss = p.BadGuy(level1, perso)
pygame.display.flip()

Menu = True
Level1 = True
keepGoing = True
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
					pygame.display.flip()
	while Level1 and perso.alive:
		for event in pygame.event.get():
			try:
				if event.type == QUIT:
					keepGoing = False
					Level1 = False
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
						t.Thread(target=perso.arm).start()
					if event.key == K_z:
						if not boss.attacking and not perso.attacking and not perso.moving: 
							t.Thread(target=perso.Attack, args=("top",)).start()
						else : 
							perso.Attack("top") 
					if event.key == K_q:
						if not boss.attacking and not perso.attacking and not perso.moving: 
							t.Thread(target=perso.Attack, args=("left",)).start()
						else : 
							perso.Attack("left") 
					if event.key == K_d:
						if not boss.attacking and not perso.attacking and not perso.moving: 
							t.Thread(target=perso.Attack, args=("right",)).start()
						else : 
							perso.Attack("right") 
					if event.key == K_s:
						if not boss.attacking and not perso.attacking and not perso.moving: 
							t.Thread(target=perso.Attack, args=("bottom",)).start()
						else : 
							perso.Attack("bottom") 
					if event.key == K_p:
						t.Thread(target=perso.powermodeToggle).start()
					if event.key == K_SPACE:
						perso.ult()
					boss.scan()
			except Exception as e:
				print("Erreur : " + str(e))
	break