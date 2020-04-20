import pygame
from pygame.locals import*
pygame.init()

import classes.Player as p
import classes.constants as c
import time
import multiprocessing as t
import random

class Mob():
    """Ennemi de base, pas très compliqué à battre"""
    def __init__(self, level):
        self.level = level
        self.target = level.player
        self.sprites = [
            pygame.image.load("assets/Mob/Right.png").convert_alpha(),
            pygame.image.load("assets/Mob/Left.png").convert_alpha()
        ]
        self.current_sprite = self.sprites[0]
        self.alive = True
        self.health = c.M_HEALTH
        self.attack = c.M_ATTACK
        self.case_x = 0
        self.case_y = 0
        self.rect = 0
        self.direction = "left"
        self.attackAnim = []
        
        for i in range(1,11):
            self.attackAnim.append(pygame.image.load("assets/Mob/Anim" + str(i) + ".png").convert_alpha())
        self.animrect = self.attackAnim[8].get_rect()

    def defRect(self, x, y):
        self.rect = pygame.Rect((x , y ), (c.SPRITE_SIZE, c.SPRITE_SIZE))

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.alive = False

    def Attack(self):
        for anim in self.attackAnim:
            self.level.display()
            self.level.window.blit(anim, self.animrect)
            self.level.window.blit(self.level.player.current_sprite, self.level.player.rect)
            self.level.player.stats()
            time.sleep(0.2)
        if self.animrect.colliderect(self.level.player.rect):
            self.level.player.damage(self.attack)

        self.attacked = True

    def scan(self):

        if self.alive and self.level.time:
            
            delta_x = c.SPRITE_SIZE * (self.level.player.case_x - self.case_x)
            delta_y = c.SPRITE_SIZE * (self.level.player.case_y - self.case_y)
            maxNeg = -1 * c.SPRITE_SIZE
            maxPos = 1 * c.SPRITE_SIZE

            assertY = delta_y <= maxPos and delta_y >= maxNeg
            assertX = delta_x <= maxPos and delta_x >= maxNeg

            if delta_y <= maxPos and delta_y >= maxNeg:
                if delta_x <= maxPos and delta_x >= maxNeg:
                    #t.Process(target=self.Attack).start()
                    self.Attack()


            if not assertX or not assertY:
                self.attacked = False

class Officer(Mob):
    """Des ennemis visiblement plus costauds"""
    def __init__(self, base_x, base_y, level, rank):
        super(Officer, self).__init__(level)
        self.assets = "assets/Officier" + str(rank)
        self.case_x = base_x
        self.health = c.O_HEALTH + rank * 2
        self.attack = c.O_ATTACK + rank * 2
        self.level = level
        self.level.badguy = self
        self.rank = rank
        self.case_y = base_y
        self.x = self.case_x * c.SPRITE_SIZE
        self.y = self.case_y * c.SPRITE_SIZE
        self.sprites = [
            pygame.image.load(self.assets + "/Right.png"),
            pygame.image.load(self.assets + "/Left.png")
        ]
        self.current_sprite = self.sprites[0]
        self.rect = self.current_sprite.get_rect().move(self.x, self.y)
        self.level.window.blit(self.current_sprite, self.rect)
        

    def Attack(self):
        if self.level.time and self.alive:
            target = self.level.player
            error = random.randint(0, 3) * c.SPRITE_SIZE
            delta_x = (c.SPRITE_SIZE * (self.target.case_x - self.case_x)) - (error / self.rank)
            delta_y = (c.SPRITE_SIZE * (self.target.case_y - self.case_y)) - (error / self.rank)

            print(delta_x)
            print(delta_y)
            self.current_sprite = self.sprites[0] if delta_x > 0 else self.sprites[1]
            self.case_x += delta_x / c.SPRITE_SIZE
            self.case_y += delta_y / c.SPRITE_SIZE
            self.rect = self.rect.move(delta_x, delta_y)
            if self.rect.colliderect(target.rect):
                target.damage(self.attack)
            self.level.display()
            self.level.window.blit(self.target.current_sprite, self.target.rect)
            self.level.window.blit(self.current_sprite, self.rect)
            self.target.stats()
            
