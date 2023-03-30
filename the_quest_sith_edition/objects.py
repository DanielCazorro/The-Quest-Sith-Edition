import os
import pygame as pg
from pygame.sprite import Sprite

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

        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_DOWN]:
            print("Mueve abajo")
            self.rect.y += self.velocidad
            if self.rect.top > ALTO_PANTALLA:
                self.rect.top = ALTO_PANTALLA
        if teclas_pulsadas[pg.K_UP]:
            print("Mueve arriba")
            self.rect.y -= self.velocidad
            if self.rect.bottom < 0:
                self.rect.bottom = 0

    def aterrizar(self):
        pass


class Asteroides(Sprite):

    velocidad_asteroide = -5

    def __init__(self) -> None:
        super().__init__()

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            pass


class Puntuacion():
    pass


class Planet(Sprite):
    pass
