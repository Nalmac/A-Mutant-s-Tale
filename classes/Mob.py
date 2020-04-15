import pygame
from pygame.locals import*
pygame.init()

import classes.Player as p
import classes.constants as c
import threading as t
import time

class Mob():
    """Ennemi de base, pas très compliqué à battre"""
    def __init__(self, level):
        self.level = level
        self.target = level.player
        self.sprites = [
            pygame.image.load("assets/Mob/Right.png"),
            pygame.image.load("assets/Mob/Left.png")
        ]
        self.current_sprite = self.sprites[0]
        self.alive = True
        self.health = c.M_HEALTH
        self.attack = c.M_ATTACK
        self.rect = self.current_sprite.get_rect()

    def start(self):
        if self.alive:
            pass