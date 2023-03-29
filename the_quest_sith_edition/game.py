import os
import ctypes
import pygame as pg
from pygame.sprite import Sprite

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA
from .escenarios import Pantalla, Pantalla_Historia, Pantalla_Inicio, Pantalla_Instrucciones, Pantalla_Jugar, Pantalla_Puntuacion


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
            Pantalla_Instrucciones(self.pantalla),
            Pantalla_Historia(self.pantalla),
            Pantalla_Jugar(self.pantalla),
            Pantalla_Puntuacion(self.pantalla)]

    def jugando(self):

        pantalla_actual = 0
        Pantalla = 0
        Inicio = 1
        Instrucciones = 2
        Historia = 3
        Jugar = 4
        Puntuacion = 5

        while pantalla_actual != "SALIR":
            resultado_bucle = self.pantallas[pantalla_actual].bucle_principal()

            if pantalla_actual == Pantalla:
                if resultado_bucle == True:
                    pantalla_actual = Inicio
                else:
                    pantalla_actual = Inicio

            if pantalla_actual == 1:
                if resultado_bucle == "S":
                    print("He pasado por primera elección: Jugar")
                    pantalla_actual = Jugar
                if resultado_bucle == "H":
                    print("He pasado por segunda elección: Historia")
                    pantalla_actual = Historia
                if resultado_bucle == "C":
                    print("He pasado por la tercera elección: Instrucciones")
                    pantalla_actual = Instrucciones
            if pantalla_actual == "SALIR":
                break
        pg.quit
        return

        # def jugando(self):
    #     print("Estoy en el bucle principal")
    #     # Aquí va el bucle principal
    #     for escena in self.pantallas:
    #         he_acabado = escena.bucle_principal()
    #         if he_acabado:
    #             break
    #         print("He acabado el for")
    #         pg.quit
