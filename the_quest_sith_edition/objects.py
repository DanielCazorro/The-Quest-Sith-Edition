import os
import pygame as pg
from pygame.sprite import Sprite
from random import randrange

from . import ANCHO_PANTALLA, ALTO_PANTALLA, FPS


class Nave(Sprite):

    margen = 30
    velocidad = 1

    # TODO: Se puden hacer varias imágenes, para que parezca que tenga movimiento

    def __init__(self):

        super().__init__()
        imagen_nave = os.path.join("resources", "images", "nave.png")
        self.image = pg.image.load(imagen_nave)
        self.rect = self.image.get_rect()
        self.rect.y = ALTO_PANTALLA/2
        self.rect.x = self.margen

    def update(self):
        """
        TODO: Aquí hay que hacer otro bucle con una función de pg que sea pulsar teclas, y que la velocidad sea menor (o aumnetar la velocidad de este bucle)
        """
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_DOWN]:
            print("Mueve abajo")
            self.rect.y += self.velocidad
            if self.rect.bottom > ALTO_PANTALLA:
                self.rect.bottom = ALTO_PANTALLA
        if teclas_pulsadas[pg.K_UP]:
            print("Mueve arriba")
            self.rect.y -= self.velocidad
            if self.rect.top < 0:
                self.rect.top = 0

    def aterrizar(self):
        pass


class Asteroides(Sprite):

    velocidad_asteroide = randrange(1, 3)
    # TODO: Aquí intentar hacer un random randint para el tamaño o quizás hacer varios tamaños en variables
    tam_asteroide = (40, 40)

    def __init__(self):

        super().__init__()
        imagen_asteroide = os.path.join("resources", "images", "asteroide.png")
        self.image = pg.image.load(imagen_asteroide)

        self.rect = self.image.get_rect()
        self.rect.y = randrange(0, ALTO_PANTALLA)
        self.rect.x = ANCHO_PANTALLA

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            pass


class Puntuacion():
    pass


class Planet(Sprite):
    pass
