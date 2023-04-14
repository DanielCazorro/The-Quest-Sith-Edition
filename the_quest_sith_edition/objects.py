import os
import pygame as pg
from pygame.sprite import Sprite
from random import randrange

from . import ANCHO_PANTALLA, ALTO_PANTALLA, PUNTOS


class Nave(Sprite):

    margen = 30
    velocidad = 6
    velocidad_aterrizaje = 2
    vidas = 3

    def __init__(self):

        super().__init__()
        imagen_nave = os.path.join("resources", "images", "nave.png")
        self.image = pg.image.load(imagen_nave)
        self.rect = self.image.get_rect()
        self.rect.y = ALTO_PANTALLA/2
        self.rect.x = self.margen
        self.giro = 0

        self.nave_esconder = False
        self.nave_aterrizar = False
        self.rotar = False
        self.terminar_rotar = False

    def movimiento_nave(self, aterriza):

        teclas_pulsadas = pg.key.get_pressed()
        if not aterriza:
            if teclas_pulsadas[pg.K_DOWN]:
                self.rect.y += self.velocidad
                if self.rect.bottom > ALTO_PANTALLA:
                    self.rect.bottom = ALTO_PANTALLA
            if teclas_pulsadas[pg.K_UP]:
                self.rect.y -= self.velocidad
                if self.rect.top < 0:
                    self.rect.top = 0

    def update(self):

        self.movimiento_nave(self.nave_aterrizar)

        if self.nave_esconder and pg.time.get_ticks()/500 - self.tiempo_esconder > 3:
            self.nave_esconder = False
            self.rect.y = ALTO_PANTALLA/2
            self.rect.x = self.margen

    def aterrizando_nave(self, aterriza, pantalla):

        self.nave_aterrizar = aterriza
        if aterriza:
            self.rect.x += self.velocidad_aterrizaje

            # Utilizar el centro en lugar de la y
            if self.rect.centery > (ALTO_PANTALLA - self.rect.height)/2:
                self.rect.y -= self.velocidad_aterrizaje
            elif self.rect.centery < (ALTO_PANTALLA - self.rect.height)/2:
                self.rect.y += self.velocidad_aterrizaje

            if self.rect.x > ANCHO_PANTALLA/2 + 50:
                self.rect.x = ANCHO_PANTALLA/2 + 50
                self.rect.centery = ALTO_PANTALLA/2
                self.rotar = True

                if self.giro == 180:
                    self.rotar = False
                    self.terminar_rotar = True
                    nave_girada = pg.transform.rotate(self.image, 180)
                    rect_rotado2 = nave_girada.get_rect(
                        center=self.rect.center)
                    # Estoy pintando la nave en lugar de girarla
                    pantalla.blit(nave_girada, rect_rotado2)

                if self.rotar:
                    self.giro += 4
                    img_rotada = pg.transform.rotate(self.image, self.giro)
                    rect_rotado = img_rotada.get_rect(center=self.rect.center)
                    pantalla.blit(img_rotada, rect_rotado)

            else:
                pantalla.blit(self.image, self.rect)

    def nave_golpeada(self):
        self.tiempo_esconder = pg.time.get_ticks() / 500
        self.nave_esconder = True
        self.rect.x = -2000
        self.rect.y = -2000


class Asteroide(Sprite):

    asteroide_s = (50, 50)
    asteroide_m = (75, 75)
    asteroide_l = (100, 100)

    puntuacion = PUNTOS
    contador_tiempo = 0

    def __init__(self, puntuacion):

        super().__init__()
        self.puntos = puntuacion
        # self.width = randrange(30, 100)
        # self.height = randrange(30, 100)
        imagen_asteroide = os.path.join(
            "resources", "images", "asteroide.png")
        self.image = pg.image.load(imagen_asteroide)
        # self.image = pg.transform.scale(self.image, (self.width, self.height))

        # # FIXME: Arreglar los asteroides, para que no cargue al disco duro cada vez, guadarlo antes y luego llamarlo
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
        # self.rect = self.image.get_rect(midbottom=(
        #     ANCHO_PANTALLA - 50, randrange(0, ALTO_PANTALLA - self.height - 10)))
        self.margen_asteroide = (ALTO_PANTALLA - self.rect.height)
        self.rect.y = randrange(0, self.margen_asteroide)
        self.rect.x = ANCHO_PANTALLA + self.rect.width

        self.velocidad_x = randrange(2, 6)

    def update(self):

        self.rect.x -= self.velocidad_x

        if self.rect.right < 10:
            self.rect.y = randrange(0, self.margen_asteroide)
            self.rect.x = ANCHO_PANTALLA + self.rect.width
            self.velocidad_x = randrange(2, 6)
            # if self.rect.top == 0:
            #     self.rect.y = 50
            # if self.rect.bottom == ALTO_PANTALLA:
            #     self.rect.y = ALTO_PANTALLA - 50


class Planeta(Sprite):
    def __init__(self, otro):
        super().__init__()
        self.image = otro
        self.rect = self.image.get_rect()
        # self.planeta_imagen = pg.image.load(
        #     os.path.join("resources", "images", "planeta.png"))
        # self.planeta_rect = self.planeta_imagen.get_rect(
        #     midleft=(ANCHO_PANTALLA + 5, ALTO_PANTALLA/2))
        self.rect.x = 500
        self.rect.y = (ALTO_PANTALLA - self.image.get_height()) / 2
        self.velocidad_x = 1

    def aparece_planeta(self, aterrizando_nave):
        if aterrizando_nave:
            self.rect.x -= self.velocidad_x
            if self.rect.x < (ANCHO_PANTALLA - self.rect.height) * 2:
                self.rect.x = (ANCHO_PANTALLA - self.rect.height) * 2
