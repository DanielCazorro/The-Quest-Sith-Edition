"""
Este será el archivo donde va el juego en sí, es decir la clase del juego, con su constructor y su función principal de juego
"""
import os
import ctypes
import pygame as pg
from pygame.sprite import Sprite

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA
from .escenarios import Pantalla, Pantalla_Historia, Pantalla_Inicio, Pantalla_Jugar


class The_Quest:

    def __init__(self):
        print("Se inicia el juego")
        pg.init()

        # Estas líneas son para el icono que aparece en miniatura al abrir la aplicación
        icono = os.path.join(
            "resources", "images", "logo_sith_mini.png")
        pg.display.set_icon(pg.image.load(icono))
        if os.name == 'nt':
            appid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                appid)

        self.pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pg.display.set_caption("The Quest - Sith Edition")

        self.pantallas = [
            Pantalla(self.pantalla),
            Pantalla_Inicio(self.pantalla),
            Pantalla_Historia(self.pantalla),
            Pantalla_Jugar(self.pantalla)]

    def jugando(self):
        print("Estoy en el bucle principal")
        # Aquí va el bucle principal
        for escena in self.pantallas:
            he_acabado = escena.bucle_principal()
            if he_acabado:
                break
            print("He acabado el for")
            pg.quit

        # FIXME:
        # salir = False
        # while not salir:
        #     for evento in pg.event.get():
        #         if evento.type == pg.QUIT:
        #             salir = True
        #     pg.draw.rect(self.pantalla, (255, 255, 255),
        #                  pg.Rect(30, 60, 50, 150))
        #     pg.display.flip()
