import os
import ctypes
import pygame as pg
from pygame.sprite import Sprite

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA
from .escenarios import Pantalla, Pantalla_Historia, Pantalla_Inicio, Pantalla_Instrucciones, Pantalla_Jugar, Pantalla_Jugar2, Pantalla_Puntuacion


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
            Pantalla_Jugar2(self.pantalla),
            Pantalla_Puntuacion(self.pantalla)]

    def jugando(self):

        pantalla_actual = 0
        Pantalla = 0
        Inicio = 1
        Instrucciones = 2
        Historia = 3
        Jugar = 4
        Jugar2 = 5
        Puntuacion = 6

        while pantalla_actual != "SALIR":
            resultado_bucle = self.pantallas[pantalla_actual].bucle_principal()

            # Estas es el bucle de elección de Pantalal
            if pantalla_actual == Pantalla:
                if resultado_bucle == True:
                    pantalla_actual = Inicio
                else:
                    pantalla_actual = Inicio

            # Este es el bucle de elección de Pantalla_Inicio
            if pantalla_actual == Inicio:
                if resultado_bucle == "SALIR":
                    pantalla_actual = "SALIR"
                if resultado_bucle == "S":
                    print("He pasado por primera elección: Jugar")
                    pantalla_actual = Jugar
                if resultado_bucle == "H":
                    print("He pasado por segunda elección: Historia")
                    pantalla_actual = Historia
                if resultado_bucle == "C":
                    print("He pasado por la tercera elección: Instrucciones")
                    pantalla_actual = Instrucciones
                if resultado_bucle == "R":
                    print("Cambiamos a pantalla records")
                    pantalla_actual = Puntuacion

            # Este es el bucle de elección de la Pantalla_Instrucciones
            if pantalla_actual == Instrucciones:
                if resultado_bucle == "SALIR":
                    pantalla_actual = "SALIR"
                if resultado_bucle == "B":
                    pantalla_actual = Inicio

            # Este es el bucle de elección de la Pantalla_Historia
            if pantalla_actual == Historia:
                if resultado_bucle == "SALIR":
                    pantalla_actual = "SALIR"
                if resultado_bucle == "B":
                    pantalla_actual = Inicio

            # Este es el bucle de la elección de la Pantalla_Juego
            if pantalla_actual == Jugar:
                if resultado_bucle == "SALIR":
                    pantalla_actual = "SALIR"
                if resultado_bucle == "0":
                    pantalla_actual = Inicio
                if resultado_bucle == "PASAS":
                    pantalla_actual = Jugar2
                if resultado_bucle == "RECORDS":
                    pantalla_actual = Puntuacion

            # Este es el bucle de la elección de la Pantalla_juego2
            if pantalla_actual == Jugar2:
                if resultado_bucle == "SALIR":
                    pantalla_actual = "SALIR"
                if resultado_bucle == "RECORDS":
                    pantalla_actual = Puntuacion

            if pantalla_actual == Puntuacion:
                if resultado_bucle == "SALIR":
                    pantalla_actual = "SALIR"
                if resultado_bucle == "INICIO":
                    pantalla_actual == Inicio
        pg.quit
        return
