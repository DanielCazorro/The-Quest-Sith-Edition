"""
Aquí crearemos las diferentes pantallas, como la pantalla de inicio, la pantalla de juego, etc.
"""
import os
import pygame as pg

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_AMARILLO


class Pantalla:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Pantalla_Inicio(Pantalla):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        fuente1 = os.path.join("resources", "fonts",
                               "PressStart2P-Regular.ttf")

        self.titulo = pg.font.Font(fuente1, 40)


class Pantalla_Jugar(Pantalla):
    def __init__(self, pantalla):
        super().__init__(pantalla)
