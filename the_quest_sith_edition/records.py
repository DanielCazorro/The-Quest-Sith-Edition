import os
import sqlite3
import pygame as pg

from . import ALTO_PANTALLA, ANCHO_PANTALLA, COLOR_BLANCO, COLOR_AMARILLO


class Base_Gestion:
    def __init__(self, direccion):
        self.direccion = direccion

    def conseguir_puntuacion(self):
        consulta = "SELECT * FROM records ORDER BY puntos DESC LIMIT 5"
        conexion = sqlite3.connect(self.direccion)
        cursor = conexion.cursor()
        cursor.execute(consulta)

        puntuaciones = []
        columnas_nombres = []

        for columna_d in cursor.description:
            columnas_nombres.append(columna_d[0])

        datos = cursor.fetchall()
        for dato in datos:
            puntuacion = {}
            indice = 0
            for nombre in columnas_nombres:
                puntuacion[nombre] = dato[indice]
                indice += 1
            puntuaciones.append(puntuacion)

        conexion.close()

        return puntuaciones

    def guardar_puntuaciones(self, nombre, puntos):

        consulta = "INSERT INTO records (Nombre,Puntos) VALUES (?,?)"
        conexion = sqlite3.connect(self.direccion)
        cursor = conexion.cursor()
        cursor.execute(consulta, (nombre, puntos))
        conexion.commit()
        conexion.close()

    def puntuacion_superior(self):

        records = self.conseguir_puntuacion()
        puntuaciones = [x["Puntos"] for x in records]
        puntuaciones.sort(reverse=True)

        return puntuaciones[0]


class CajaTexto:

    def __init__(self, pantalla: pg.Surface, color_texto=COLOR_BLANCO, color_fondo=COLOR_AMARILLO, title=""):
        font_file = os.path.join(
            "resources", "fonts", "fuente-extra.ttf")
        self.tipografia = pg.font.Font(font_file, 20)
        self.texto = ""
        self.color_fondo = color_fondo
        self.color_texto = color_texto
        self.pantalla = pantalla
        self.margen = 30
        self.crear_entradas()
        self.maxima_longidtud = 3

    def conseguir_texto(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE and len(self.texto) > 0:
                        self.texto = self.texto[:-1]
                    elif event.key == pg.K_RETURN:
                        salir = True
                    else:
                        if len(self.texto) < self.maxima_longidtud:
                            self.texto += event.unicode
            self.pintar()
            pg.display.flip()
        return self.texto

    def pintar(self):
        pg.draw.rect(self.pantalla, self.color_fondo, self.fondo)
        self.pantalla.blit(self.titulo, (self.x_titulo, self.y_titulo))

        superficie_texto = self.tipografia.render(
            self.texto, True, self.color_texto, self.color_fondo)
        pos_x = self.x_titulo
        pos_y = self.y_titulo + self.titulo.get_height()
        self.pantalla.blit(superficie_texto, (pos_x, pos_y))

    def crear_entradas(self):
        self.titulo = self.tipografia.render(
            "Gracias por destruir a los Jedi. Introduce tus iniciales:", True, self.color_texto, self.color_fondo)
        self.x_titulo = (ANCHO_PANTALLA-self.titulo.get_width())//2 - 200
        self.y_titulo = (ALTO_PANTALLA-self.titulo.get_height())//2

        x_fondo = self.x_titulo - self.margen
        y_fondo = self.y_titulo - self.margen
        w_fondo = self.titulo.get_width() + self.margen * 2
        h_fondo = self.titulo.get_height() * 2 + self.margen * 2
        self.fondo = pg.Rect(x_fondo, y_fondo, w_fondo, h_fondo)
