import os
import pygame as pg
from pygame.sprite import Sprite
from random import randrange, randint

from . import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, COLOR_NEGRO


class Nave(Sprite):

    margen = 30
    velocidad = 3
    vidas = 3

    def __init__(self):

        super().__init__()
        imagen_nave = os.path.join("resources", "images", "nave.png")
        self.image = pg.image.load(imagen_nave)
        self.rect = self.image.get_rect()
        self.rect.y = ALTO_PANTALLA/2
        self.rect.x = self.margen

        self.nave_esconder = False
        self.nave_aterrizar = False

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

        if self.nave_esconder and pg.time.get_ticks()/500 - self.tiempo_esconder > 3:
            self.nave_esconder = False
            self.rect.y = ALTO_PANTALLA/2
            self.rect.x = self.margen

    def aterrizar_planeta(self, aterriza):
        pass
    # TODO
        self.nave_aterrizar = aterriza
        if aterriza:
            if self.rect.y < (ALTO_PANTALLA - self.rect.height) / 2:
                self.rect.y += self.velocidad
            elif self.rect.y > (ALTO_PANTALLA - self.rect.height) / 2:
                self.rect.y -= self.velocidad

    def nave_golpeada(self):
        self.tiempo_esconder = pg.time.get_ticks() / 500
        self.nave_esconder = True
        self.rect.x = -1000
        self.rect.y = -1000


class Asteroide(Sprite):

    asteroide_s = (50, 50)
    asteroide_m = (75, 75)
    asteroide_l = (100, 100)

    puntuacion = 0
    contador_tiempo = 0

    def __init__(self):
        super().__init__()

        imagen_asteroide = os.path.join(
            "resources", "images", "asteroide.png")
        self.image = pg.image.load(imagen_asteroide)

        self.asteroide_aleatorio = randrange(0, 3)
        if self.asteroide_aleatorio == 0:
            self.image = pg.transform.scale(self.image, self.asteroide_s)
            self.radius = 25
        elif self.asteroide_aleatorio == 1:
            self.image = pg.transform.scale(self.image, self.asteroide_m)
            self.radius = 37
        elif self.asteroide_aleatorio == 2:
            self.image = pg.transform.scale(self.image, self.asteroide_l)
            self.radius = 50

        self.rect = self.image.get_rect()
        self.margen_asteroide = (ALTO_PANTALLA - self.rect.height)
        self.rect.y = randrange(0, self.margen_asteroide)
        self.rect.x = ANCHO_PANTALLA + self.rect.width

        self.velocidad_x = randrange(1, 3)

    def update(self):

        self.rect.x -= self.velocidad_x

        if self.rect.right <= 0:

            self.contador_tiempo += 1
            self.puntuacion += 10

            self.rect.y = randrange(0, self.margen_asteroide)
            self.rect.x = ANCHO_PANTALLA + self.rect.width
            self.velocidad_x = randrange(1, 3)

        print(f"{self.puntuacion}")
        print(f"TIEMPO: {self.contador_tiempo}")

        # FIXME: La puntuación no suma correctamente


class Planeta(Sprite):
    def __init__(self, otro):
        super().__init__()
        self.pantalla = otro.pantalla
        self.pantalla_rect = otro.pantalla.get_rect()
        self.planeta_imagen = pg.image.load(
            os.path.join("resources", "images", "planeta.png"))
        self.planeta_rect = self.planeta_imagen.get_rect(
            midleft=(ANCHO_PANTALLA + 5, ALTO_PANTALLA/2))
        self.velocidad_x = 1

    def blit_planeta(self):
        self.pantalla.blit(self.planeta_imagen, self.planeta_rect)
