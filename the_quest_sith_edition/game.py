"""
Este será el archivo donde va el juego en sí, es decir la clase del juego, con su constructor y su función principal de juego
"""
import pygame as pg

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA


class The_Quest:

    def __init__(self):
        print("Se inicia el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pg.display.set_caption("The Quest - Sith Edition")

    def jugando(self):
        print("Estoy en el bucle principal")
        # Aquí va el bucle principal
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            pg.draw.rect(self.display, (255, 255, 255),
                         pg.Rect(30, 60, 50, 150))
            pg.display.flip()
