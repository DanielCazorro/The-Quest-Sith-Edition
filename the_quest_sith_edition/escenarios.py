import os
import pygame as pg

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_AMARILLO, COLOR_BLANCO, COLOR_ROJO, FPS
from .objects import Nave, Asteroides


class Pantalla:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Pantalla_Inicio(Pantalla):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        # TODO:  COMO LAS FUENTES SE REPITEN, SACARLAS A LA CLASE PANTALLA PARA LLAMARLAS Y NO ESTAR COPIA-PEGA
        fuente_titulo = os.path.join(
            "resources", "fonts", "fuente-titulo.ttf")
        self.titulo = pg.font.Font(fuente_titulo, 30)

        fuente_historia = os.path.join(
            "resources", "fonts", "fuente-historia.ttf")
        self.historia = pg.font.Font(fuente_historia, 15)

        fuente_extra = os.path.join(
            "resources", "fonts", "fuente-extra.ttf")
        self.extra = pg.font.Font(fuente_extra, 32)

        # TODO: Revisar esta parte: TONY explica que no es necesario poner todo lo anterior, se puede simplificar así
        self.extra_peque = pg.font.Font(fuente_extra, 25)

        imagen_inicio = os.path.join(
            "resources", "images", "fondo_pantalla_inicio.jpg")
        self.pantalla_inicio = pg.image.load(imagen_inicio)

        logo_sith = os.path.join("resources", "images", "logo_sith.png")
        self.logo_sith = pg.image.load(logo_sith)

    def bucle_principal(self):
        """
        Devuelve True si hay que finalizar el programa
        Devuelve False si hay que pasar a la siguiente escena
        """

        # TODO: Hay que hacer que al pulsar la tecla s cambie a la pantalla historia, pero que si se pulsa espacio cambie al juego. Seguir investigando por ahora
        super().bucle_principal()
        salir = False
        self.musica_fondo()
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_s:
                    salir = True
                """
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    break                    
                ESTA PARTE SEGURAMENTE VAYA COMO HA EXPLICADO TONI EN EL BUCLE PRINCIPAL
                """
                if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ESTO SIRVE PARA PARAR LA MUSICA PULSANDO A
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.stop()
                    else:
                        pg.mixer_music.play(-1, 0.0)
            self.pantalla.fill((99, 0, 0))
            self.pintar_fondo()
            self.pintar_texto_iniciar()
            self.pintar_texto_musica()
            self.pintar_texto_inicio_controles()
            self.pintar_texto_inicio_historia()
            self.pintar_logo()
            pg.display.flip()
        return False

    def pintar_fondo(self):

        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.pantalla_inicio, (0, 0))

    def pintar_texto_iniciar(self):
        mensaje = "Pulsa <espacio> para comenzar la partida"
        texto = self.titulo.render(mensaje, True, (COLOR_BLANCO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA * 5/8
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_musica(self):
        mensaje = "Pulsa <a> para pausar/reaundar la música"
        texto = self.extra_peque.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_inicio_historia(self):
        mensaje = "Pulsa <s> para adentrarte en el lado oscuro y conocer todos sus secretos"
        texto = self.extra.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA * 6/8
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_inicio_controles(self):

        mensaje = "Pulsa <i> para ver los controles"
        texto = self.extra_peque.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 40
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_logo(self):
        ancho_titulo = self.logo_sith.get_width()
        pos_x = (ANCHO_PANTALLA - ancho_titulo) / 2
        pos_y = ALTO_PANTALLA/48
        self.pantalla.blit(self.logo_sith, (pos_x, pos_y))

    def musica_fondo(self):
        pg.mixer.init()
        musica_fondo = os.path.join("resources", "sounds", "musica_intro.mp3")
        pg.mixer.music.load(musica_fondo)
        pg.mixer.music.set_volume(0.75)
        pg.mixer.music.play(-1, 0.0)


class Pantalla_Instrucciones(Pantalla):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        # TODO:  COMO LAS FUENTES SE REPITEN, SACARLAS A LA CLASE PANTALLA PARA LLAMARLAS Y NO ESTAR COPIA-PEGA
        fuente_titulo = os.path.join(
            "resources", "fonts", "fuente-titulo.ttf")
        self.titulo = pg.font.Font(fuente_titulo, 27)

        fuente_extra = os.path.join(
            "resources", "fonts", "fuente-extra.ttf")
        self.extra = pg.font.Font(fuente_extra, 40)

        # TODO: Revisar esta parte: TONY explica que no es necesario poner todo lo anterior, se puede simplificar así
        self.extra_peque = pg.font.Font(fuente_extra, 25)

        imagen_inicio = os.path.join(
            "resources", "images", "fondo_pantalla_instrucciones.jpg")
        self.pantalla_inicio = pg.image.load(imagen_inicio)

    def bucle_principal(self):
        """
        Devuelve True si hay que finalizar el programa
        Devuelve False si hay que pasar a la siguiente escena
        """

        # TODO: Hay que hacer que al pulsar la tecla s cambie a la pantalla historia, pero que si se pulsa espacio cambie al juego. Seguir investigando por ahora
        super().bucle_principal()
        salir = False
        self.musica_fondo()
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_b:
                    salir = True
                """
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    break                    
                ESTA PARTE SEGURAMENTE VAYA COMO HA EXPLICADO TONI EN EL BUCLE PRINCIPAL
                """
                if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ESTO SIRVE PARA PARAR LA MUSICA PULSANDO A
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.stop()
                    else:
                        pg.mixer_music.play(-1, 0.0)
            self.pantalla.fill((99, 0, 0))
            self.pintar_fondo()
            self.pintar_texto_iniciar()
            self.pintar_texto_musica()
            self.pintar_texto_instrucciones()
            pg.display.flip()
        return False

    def pintar_fondo(self):

        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.pantalla_inicio, (0, 0))

    def pintar_texto_iniciar(self):
        mensaje = "Pulsa <b> para volver a la pantalla de inicio"
        texto = self.titulo.render(mensaje, True, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA - 100
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_instrucciones(self):

        lugar_pantalla = [200, 240]
        instrucciones = ["Pulsa <flecha arriba> para subir la nave.",
                         "Pulsa <flecha abajo> para bajar la nave."]

        pos_x = ANCHO_PANTALLA - 1150
        contador_lugar = 0

        for instruccion in instrucciones:
            texto_render = self.extra.render(
                (instruccion), True, COLOR_ROJO)
            self.pantalla.blit(
                texto_render, (pos_x, lugar_pantalla[contador_lugar]))
            contador_lugar += 1

    def pintar_texto_musica(self):
        mensaje = "Pulsa <a> para pausar/reaundar la música"
        texto = self.extra_peque.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))

    def musica_fondo(self):
        pg.mixer.init()
        musica_fondo = os.path.join(
            "resources", "sounds", "musica_instrucciones.mp3")
        pg.mixer.music.load(musica_fondo)
        pg.mixer.music.set_volume(0.75)
        pg.mixer.music.play(-1, 0.0)


class Pantalla_Historia(Pantalla):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        fuente_titulo = os.path.join(
            "resources", "fonts", "fuente-titulo.ttf")
        self.titulo = pg.font.Font(fuente_titulo, 25)

        fuente_historia = os.path.join(
            "resources", "fonts", "fuente-historia.ttf")
        self.historia = pg.font.Font(fuente_historia, 20)

        fuente_extra = os.path.join(
            "resources", "fonts", "fuente-extra.ttf")
        self.extra = pg.font.Font(fuente_extra, 37)

        # FIXME: PREGUNTAR AQUÍ SI HAY ALGÚN MÉTODO PARA CAMBIAR EL TAMAÑO DE LA LETRA DESDE LA FUNCIÓN PARA NO TENER QUE COPIAR Y PEGAR VARIAS VECES (REPETIDO)
        fuente_extra_peque = os.path.join(
            "resources", "fonts", "fuente-extra.ttf")
        self.extra_peque = pg.font.Font(fuente_extra_peque, 25)

        imagen_historia = os.path.join(
            "resources", "images", "fondo_pantalla_historia.jpg")
        self.pantalla_historia = pg.image.load(imagen_historia)

    def bucle_principal(self):
        """
        Devuelve True si hay que finalizar el programa
        Devuelve False si hay que pasar a la siguiente escena
        """
        super().bucle_principal()
        salir = False
        inicio = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_b:
                    inicio = True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
            # self.pantalla.fill((99, 0, 0))
            self.pintar_fondo()
            # self.pintar_texto_iniciar()
            # self.pintar_texto_inicio_controles()
            # self.pintar_texto_inicio_historia()
            # self.pintar_logo()
            self.pintar_historia()
            pg.display.flip()

            # Si pulso b, se que paso por aquí. Ahora hay que intentar que al pasar por aquí haya una condición (junto con el bucle principal de game.py) para que pase a a la escena
            if inicio == True:
                print("Pasando por pantalla inicio")
                return Pantalla_Inicio(Pantalla)
        return False

    def pintar_fondo(self):
        # FIXME: Aquí sería mejor poner la ruta de la imagen???? En lugar de ponerla como variable general en la clase?
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.pantalla_historia, (0, 0))

    def pintar_historia(self):
        # FIXME:Probar a hacer varias frases en una lista, y con un bucle for irlos poniendo en posiciones
        # TODO: Pensar en hacer un bucle o algo para que aparezcan de una en una las frases
        frases = ["Hace mucho tiempo, en una galaxia lejana...",
                  "El terror y la anarquía reinaban en todas partes.",
                  "Por  suerte, surgieron unos héroes, que lucharon por la libertad...",
                  "Los Sith. Caballeros nobles y poderosos que luchaban por el orden.",
                  "Nuestra historia sigue a un gran caballero Sith,",
                  "Que busca sin descanso a los malvados Jedi por los planetas de la galaxia."]


class Pantalla_Jugar(Pantalla):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.jugador = Nave()

    def bucle_principal(self):
        salir = False
        inicio = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_b:
                    inicio = True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
            # self.pantalla.fill((99, 0, 0))
            self.pintar_fondo()
            # self.pintar_texto_iniciar()
            # self.pintar_texto_inicio_controles()
            # self.pintar_texto_inicio_historia()
            # self.pintar_logo()
            pg.display.flip()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

        # # FIXME: Elegir aquí la otra imagen y la letra correcta
        # fuente1 = os.path.join("resources", "fonts",
        #                        "PressStart2P-Regular.ttf")
        # self.titulo = pg.font.Font(fuente1, 40)

        # imagen_inicio = os.path.join("resources", "images", "Andor_galaxy.jpg")
        # self.logo = pg.image.load(imagen_inicio)


class Pantalla_Puntuacion(Pantalla):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
        return False
