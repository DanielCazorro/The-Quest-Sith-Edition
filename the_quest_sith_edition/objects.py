import os
import pygame as pg
from pygame.sprite import Sprite
from random import randrange, randint

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

    # velocidad_asteroide = randrange(1, 3) TODO: Quizás sea mejor ponerlo abajo
    # TODO: Aquí intentar hacer un random randint para el tamaño o quizás hacer varios tamaños en variables
    tam_asteroide_pequeño = (40, 40)
    tam_asteroide_mediano = (55, 55)
    tam_asteroide_grande = (70, 70)

    def __init__(self):

        super().__init__()
        imagen_asteroide = os.path.join("resources", "images", "asteroide.png")
        # self.image = pg.image.load(imagen_asteroide)

        # self.asteroide_aleatorio = randrange(0, 3)
        # if self.asteroide_aleatorio == 0:
        #     self.image = pg.transform.scale(
        #         self.image, self.tam_asteroide_pequeño)
        #     self.radius = 10
        # if self.asteroide_aleatorio == 1:
        #     self.image = pg.transform.scale(
        #         self.image, self.tam_asteroide_mediano)
        #     self.radius = 10
        # if self.asteroide_aleatorio == 2:
        #     self.image = pg.transform.scale(
        #         self.image, self.tam_asteroide_grande)
        #     self.radius = 10

        self.ancho = 50
        self.alto = 50
        self.image = pg.Surface((self.ancho, self.alto), pg.SRCALPHA)
        self.plantilla = pg.image.load(imagen_asteroide)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_PANTALLA - self.rect.width
        self.rect.y = randrange(ALTO_PANTALLA-self.rect.height)
        self.velocidad_asteroide = randint(2, 6)

        # self.rect = self.image.get_rect()
        # self.margen_asteroide = (ALTO_PANTALLA - self.rect.height)
        # self.rect.y = randrange(0, self.margen_asteroide)
        # self.rect.x = ANCHO_PANTALLA + self.rect.width

        # self.velocidad_asteroide = randrange(1, 6)

    def movimiento(self):

        self.rect.x -= self.velocidad_asteroide
        if self.rect.right < -20:
            self.rect.y = randrange(0, self.margen_asteroide)
            self.rect.x = ANCHO_PANTALLA + self.rect.width
            self.velocidad_asteroide = randrange(1, 6)

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            pass


class Puntuacion():
    pass


class Planet(Sprite):
    pass
