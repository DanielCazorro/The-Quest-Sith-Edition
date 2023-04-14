"""
Aquí irá la clase records, y toda su función de escritura en la base de datos
"""
import os
import pygame as pg
import sqlite3


class Base_Gestion:
    def __init__(self):
        pass

    def conseguir_puntuacion(self):
        consulta = "SELECT * FROM records ORDER BY puntos DESC LIMIT 5"

        conectar_base = sqlite3.connect()
