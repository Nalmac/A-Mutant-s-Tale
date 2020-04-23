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
level3 = l.Level(3)
level4 = l.Level(4)
level5 = l.Level(5)

menu = l.Menu()
perso = p.Player([level1, level2, level3, level4, level5])
level1.player = perso
level2.player = perso
level3.player = perso
level4.player = perso
level5.player = perso

boss1 = m.Officer(10, 16, level1, 1)
boss2 = m.Officer(7, 1, level2, 2)
boss3 = m.Officer(7, 1, level3, 3)
boss4 = m.Officer(10, 7, level4, 4)
FinalBoss = p.BadGuy([level5], perso)

pygame.display.flip()

Menu = True
keepGoing = True
i = 0
while keepGoing:
	while Menu:
		menu.display()
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				keepGoing = False
				Menu = False
				perso.alive = False
			if event.type == KEYDOWN:
				if event.key == K_F1:
					Menu = False
					level1.display()
					level1.window.blit(perso.current_sprite, perso.rect)
					perso.stats()

	while level1.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 15 - level1.badguy.rank)
			if event.type == QUIT:
				for mob in level1.mob:
					mob.alive = False
				keepGoing = False
				perso.alive = False

				level1.loop = False
				break
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					t.Thread(target=perso.move, args=("bottom",)).start()
				if event.key == K_UP:
					t.Thread(target=perso.move, args=("top",)).start()
				if event.key == K_LEFT:
					t.Thread(target=perso.move, args=("left",)).start()
				if event.key == K_RIGHT:
					t.Thread(target=perso.move, args=("right",)).start()
				if event.key == K_a:
					t.Thread(target=perso.arm).start()
				if event.key == K_z:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("top",)).start()
						
					else :
						
						perso.Attack("top") 
				if event.key == K_q:
					if not not perso.moving: 
						t.Thread(target=perso.Attack, args=("left",)).start()
						
					else :
						
						perso.Attack("left") 
				if event.key == K_d:
					if not perso.moving: 
						t.Thread(target=perso.Attack, args=("right",)).start()
						
					else : 
						
						perso.Attack("right") 
				if event.key == K_s:
					if not perso.moving: 
						t.Thread(target=perso.Attack, args=("bottom",)).start()
						
					else : 
						
						perso.Attack("bottom") 
				if event.key == K_p:
					t.Thread(target=perso.powermodeToggle).start()
				if event.key == K_SPACE:
					perso.ult()
				for mob in level1.mob:
					t.Thread(target=mob.scan).start()
				i += 1
				time.sleep(0.2)
				if i % num == 0:
					perso.stamina += 1 if perso.stamina < 5 else 0
					level1.badguy.Attack()

	
	while level2.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 15 - level2.badguy.rank )
			if event.type == QUIT:
				for mob in level2.mob:
					mob.alive = False
				keepGoing = False
				level2.loop = False
				perso.alive = False

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
						
					else :
						
						perso.Attack("top") 
				if event.key == K_q:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("left",)).start()
						
					else :
						
						perso.Attack("left") 
				if event.key == K_d:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("right",)).start()
						
					else : 
						
						perso.Attack("right") 
				if event.key == K_s:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("bottom",)).start()
						
					else : 
						
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

	while level3.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 15 - level3.badguy.rank)
			if event.type == QUIT:
				for mob in level3.mob:
					mob.alive = False
				keepGoing = False
				perso.alive = False

				level3.loop = False
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
						
					else :
						
						perso.Attack("top") 
				if event.key == K_q:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("left",)).start()
						
					else :
						
						perso.Attack("left") 
				if event.key == K_d:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("right",)).start()
						
					else : 
						
						perso.Attack("right") 
				if event.key == K_s:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("bottom",)).start()
						
					else : 
						
						perso.Attack("bottom") 
				if event.key == K_p:
					t.Thread(target=perso.powermodeToggle).start()
				if event.key == K_SPACE:
					perso.ult()
				for mob in level3.mob:
					mob.scan()
				i += 1
				time.sleep(0.2)
				if i % num == 0:
					perso.stamina += 1 if perso.stamina < 5 else 0
					level3.badguy.Attack()
	while level4.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 15 - level4.badguy.rank)
			if event.type == QUIT:
				for mob in level4.mob:
					mob.alive = False
				keepGoing = False
				perso.alive = False

				level4.loop = False
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
						
					else :
						
						perso.Attack("top") 
				if event.key == K_q:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("left",)).start()
						
					else :
						
						perso.Attack("left") 
				if event.key == K_d:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("right",)).start()
						
					else : 
						
						perso.Attack("right") 
				if event.key == K_s:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("bottom",)).start()
						
					else : 
						
						perso.Attack("bottom") 
				if event.key == K_p:
					t.Thread(target=perso.powermodeToggle).start()
				if event.key == K_SPACE:
					perso.ult()
				for mob in level4.mob:
					mob.scan()
				i += 1
				time.sleep(0.2)
				if i % num == 0:
					perso.stamina += 1 if perso.stamina < 5 else 0
					level4.badguy.Attack()
	while level5.loop and perso.alive:
		for event in pygame.event.get():
			num = random.randint(1, 5)
			if event.type == QUIT:
				for mob in level5.mob:
					mob.alive = False
				keepGoing = False
				perso.alive = False

				level5.loop = False
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
						
					else :
						
						perso.Attack("top") 
				if event.key == K_q:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("left",)).start()
						
					else :
						
						perso.Attack("left") 
				if event.key == K_d:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("right",)).start()
						
					else : 
						
						perso.Attack("right") 
				if event.key == K_s:
					if not perso.attacking and not perso.moving: 
						t.Thread(target=perso.Attack, args=("bottom",)).start()
						
					else : 
						
						perso.Attack("bottom") 
				if event.key == K_p:
					t.Thread(target=perso.powermodeToggle).start()
				if event.key == K_SPACE:
					perso.ult()
				for mob in level5.mob:
					mob.scan()
				i += 1
				time.sleep(0.2)
				if i % num == 0:
					perso.stamina += 1 if perso.stamina < 5 else 0
					level5.badguy.move()
				level5.badguy.scan()
	break