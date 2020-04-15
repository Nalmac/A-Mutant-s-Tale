import pygame
from pygame.locals import*
pygame.init()

import classes.Player as p
import classes.constants as c
import time

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
        self.rect = self.current_sprite.get_rect()
        self.direction = "left"
        self.attackAnim = []
        
        for i in range(1,11):
            self.attackAnim.append(pygame.image.load("assets/Mob/Anim" + str(i) + ".png").convert_alpha())
        self.animrect = self.attackAnim[8].get_rect()
    def start(self):
        self.animrect = self.animrect.move(c.SPRITE_SIZE * self.case_x - c.SPRITE_SIZE, c.SPRITE_SIZE * self.case_y - c.SPRITE_SIZE)
        while self.alive:
            for anim in self.attackAnim:
                self.level.display()
                self.level.window.blit(anim, self.animrect)
                pygame.display.flip()
                time.sleep(0.1)
            time.sleep(5)           