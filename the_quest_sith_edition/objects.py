import os
import pygame as pg
from pygame.sprite import Sprite
from random import randrange, randint

from . import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, COLOR_NEGRO


class Nave(Sprite):

    margen = 30
    velocidad = 1
    vidas = 3

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

    # def hay_colision(self, otro):
    #     if self.rect.colliderect(otro):
    #         # hay colisión
    #         print("Hay colisión")


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
            self.puntos = 10
        elif self.asteroide_aleatorio == 1:
            self.image = pg.transform.scale(self.image, self.asteroide_m)
            self.radius = 37
            self.puntos = 20
        elif self.asteroide_aleatorio == 2:
            self.image = pg.transform.scale(self.image, self.asteroide_l)
            self.puntos = 30

        self.rect = self.image.get_rect()
        self.margen_asteroide = (ALTO_PANTALLA - self.rect.height)
        self.rect.y = randrange(0, self.margen_asteroide)
        self.rect.x = ANCHO_PANTALLA + self.rect.width

        self.velocidad_x = randrange(1, 2)

    def update(self):

        self.rect.x -= self.velocidad_x
        if self.rect.right < -10:
            self.rect.y = randrange(0, self.margen_asteroide)
            self.rect.x = ANCHO_PANTALLA + self.rect.width
            self.velocidad_x = randrange(1, 3)
            self.puntuacion += self.puntos
            print(f"{self.puntuacion}")
            return self.puntuacion
        # FIXME: La puntuación no suma correctamente


class Puntuacion():
    pass


class Planet(Sprite):
    pass
