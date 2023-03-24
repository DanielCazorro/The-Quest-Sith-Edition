"""
Aquí crearemos las diferentes pantallas, como la pantalla de inicio, la pantalla de juego, etc.
"""
import os
import pygame as pg

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_AMARILLO, FPS


class Pantalla:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        """
        Este método debe ser implementado por cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida.
        """
        pass


class Pantalla_Inicio(Pantalla):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        fuente1 = os.path.join("resources", "fonts",
                               "PressStart2P-Regular.ttf")
        # FIXME: Aquí pondremos mas fuentes
        self.titulo = pg.font.Font(fuente1, 40)

        imagen_inicio = os.path.join("resources", "images", "Andor_galaxy.jpg")
        self.fondo = pg.image.load(imagen_inicio)

    def bucle_principal(self):
        """
        Devuelve True si hay que finalizar el programa
        Devuelve False si hay que pasar a la siguiente escena
        """
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pintar_fondo()
            self.pintar_texto()
            # self.pintar_logo()  HAY QUE HACER ESTA FUNCIÓN ABAJO PRIMERO
            pg.display.flip()
        return False

# TODO: Hacer funcion pintar logo para poner un logo básico tipo The Quest o algo de star wars

    def pintar_fondo(self):
        # FIXME: Esto sería para pintar un logo
        # ancho_titulo = self.logo.get_width()
        # pos_x = (ANCHO_PANTALLA - ancho_titulo) / 2
        # pos_y = ALTO_PANTALLA/3
        # self.pantalla.blit(self.logo, (pos_x, pos_y))

        # FIXME: Aquí sería mejor poner la ruta de la imagen????
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0, 0))

    def pintar_texto(self):
        # FIXME: Arreglar el tamaño de la letra Y HACER VARIABLE PARA EL COLOR, NO PONER NÚMEROS MÁGICOS
        mensaje = "Pulsa <espacio> para comenzar la partida"
        texto = self.titulo.render(mensaje, True, (255, 255, 255))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA * 3 / 4
        self.pantalla.blit(texto, (pos_x, pos_y))


class Pantalla_Jugar(Pantalla):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        # FIXME: Elegir aquí la otra imagen y la letra correcta
        fuente1 = os.path.join("resources", "fonts",
                               "PressStart2P-Regular.ttf")
        self.titulo = pg.font.Font(fuente1, 40)

        imagen_inicio = os.path.join("resources", "images", "Andor_galaxy.jpg")
        self.logo = pg.image.load(imagen_inicio)
