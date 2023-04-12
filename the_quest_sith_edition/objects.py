import os
import pygame as pg
from pygame.sprite import Sprite
from random import randrange, randint

from . import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, COLOR_NEGRO


class Nave(Sprite):

    margen = 30
    velocidad = 1
    vidas = 3

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
    # TODO


class Asteroide(Sprite):

    asteroide_s = (50, 50)
    asteroide_m = (75, 75)
    asteroide_l = (100, 100)

    puntuacion = 0

    def __init__(self):
        super().__init__()

        imagen_asteroide = os.path.join(
            "resources", "images", "asteroide.png")
        self.image = pg.image.load(imagen_asteroide)

        self.asteroide_aleatorio = randrange(0, 3)
        if self.asteroide_aleatorio == 0:
            self.image = pg.transform.scale(self.image, self.asteroide_s)
            self.radius = 25
            self.puntos_s = 5
        elif self.asteroide_aleatorio == 1:
            self.image = pg.transform.scale(self.image, self.asteroide_m)
            self.radius = 37
            self.puntos_m = 10
        elif self.asteroide_aleatorio == 2:
            self.image = pg.transform.scale(self.image, self.asteroide_l)
            self.radius = 50
            self.puntos_l = 23
        self.puntos = 30

        self.rect = self.image.get_rect()
        self.margen_asteroide = (ALTO_PANTALLA - self.rect.height)
        self.rect.y = randrange(0, self.margen_asteroide)
        self.rect.x = ANCHO_PANTALLA + self.rect.width

        self.velocidad_x = randrange(1, 3)

    def update(self):

        self.rect.x -= self.velocidad_x
        if self.rect.right <= 0:

            self.rect.y = randrange(0, self.margen_asteroide)
            self.rect.x = ANCHO_PANTALLA + self.rect.width
            self.velocidad_x = randrange(1, 3)

        if self.asteroide_aleatorio == 0:
            if self.rect.right < 0:
                self.puntuacion += self.puntos_s
        elif self.asteroide_aleatorio == 1:
            if self.rect.right < 0:
                self.puntuacion += self.puntos_m
        elif self.asteroide_aleatorio == 2:
            if self.rect.right < 0:
                self.puntuacion += self.puntos_l

        print(f"{self.puntuacion}")

        # FIXME: La puntuación no suma correctamente


class Planet(Sprite):
    pass
