import os
import pygame as pg
from random import randint

from the_quest_sith_edition import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_AMARILLO, COLOR_BLANCO, COLOR_ROJO, FPS
from .objects import Nave, Asteroide, Planeta


class Pantalla:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

        # Aquí van las fuentes generales
        fuente_titulo = os.path.join(
            "resources", "fonts", "fuente-titulo.ttf")
        self.titulo = pg.font.Font(fuente_titulo, 30)

        self.titulo_instrucciones = pg.font.Font(fuente_titulo, 25)

        fuente_historia = os.path.join(
            "resources", "fonts", "fuente-historia.ttf")
        self.historia = pg.font.Font(fuente_historia, 35)

        fuente_extra = os.path.join(
            "resources", "fonts", "fuente-extra.ttf")
        self.extra = pg.font.Font(fuente_extra, 32)

        self.extra_peque = pg.font.Font(fuente_extra, 25)

        self.extra_musica = pg.font.Font(fuente_extra, 18)

    def bucle_principal(self):
        pass


class Pantalla_Inicio(Pantalla):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        imagen_inicio = os.path.join(
            "resources", "images", "fondo_pantalla_inicio.jpg")
        self.pantalla_inicio = pg.image.load(imagen_inicio)

        logo_sith = os.path.join("resources", "images", "logo_sith.png")
        self.logo_sith = pg.image.load(logo_sith)

    def bucle_principal(self):

        super().bucle_principal()
        salir = False
        self.musica_fondo()

        while not salir:
            print(pg.time.get_ticks())
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return "SALIR"
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    return "S"
                if event.type == pg.KEYDOWN and event.key == pg.K_h:
                    return "H"
                if event.type == pg.KEYDOWN and event.key == pg.K_c:
                    return "C"
                if pg.time.get_ticks() > 500000000:  # TODO: Cambiar este número a algo mas normal
                    return "R"

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
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_inicio_historia(self):
        mensaje = "Pulsa <H> para adentrarte en el lado oscuro y conocer todos sus secretos"
        texto = self.extra.render(mensaje, False, (COLOR_ROJO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA * 6/8
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_inicio_controles(self):

        mensaje = "Pulsa <C> para ver los controles"
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

        imagen_inicio = os.path.join(
            "resources", "images", "fondo_pantalla_instrucciones.jpg")
        self.pantalla_inicio = pg.image.load(imagen_inicio)

    def bucle_principal(self):

        super().bucle_principal()
        salir = False
        self.musica_fondo()

        while not salir:

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return "SALIR"
                if event.type == pg.KEYDOWN and event.key == pg.K_b:
                    return "B"

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
        mensaje = "Pulsa <B> para volver a la pantalla de inicio"
        texto = self.titulo_instrucciones.render(
            mensaje, True, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA - 100
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_instrucciones(self):

        lugar_pantalla = [220, 280]
        instrucciones = ["--> Pulsa <flecha arriba> para subir la nave",
                         "--> Pulsa <flecha abajo> para bajar la nave"]

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
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
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
        imagen_historia = os.path.join(
            "resources", "images", "fondo_pantalla_historia.jpg")
        self.pantalla_historia = pg.image.load(imagen_historia)

    def bucle_principal(self):

        super().bucle_principal()
        salir = False
        self.musica_fondo()

        while not salir:

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return "SALIR"
                if event.type == pg.KEYDOWN and event.key == pg.K_b:
                    return "B"

                if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ESTO SIRVE PARA PARAR LA MUSICA PULSANDO A
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.stop()
                    else:
                        pg.mixer_music.play(-1, 0.0)

            self.pantalla.fill((99, 0, 0))
            self.pintar_fondo()
            self.pintar_texto_iniciar()
            self.pintar_texto_musica()
            self.pintar_historia()
            self.pintar_historia()
            pg.display.flip()
        return False

    def musica_fondo(self):
        pg.mixer.init()
        musica_fondo = os.path.join(
            "resources", "sounds", "musica_historia.mp3")
        pg.mixer.music.load(musica_fondo)
        pg.mixer.music.set_volume(0.75)
        pg.mixer.music.play(-1, 0.0)

    def pintar_fondo(self):

        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.pantalla_historia, (0, 0))

    def pintar_historia(self):

        # TODO: Pensar en hacer un bucle o algo para que aparezcan de una en una las frases
        lugar_pantalla = [140, 200, 260, 320, 380, 440]
        frases = ["Hace mucho tiempo, en una galaxia lejana...",
                  "El terror y la anarquía reinaban en todas partes.",
                  "Por  suerte, surgieron unos héroes, que lucharon por la libertad...",
                  "Los Sith. Caballeros nobles y poderosos que luchaban por el orden.",
                  "Nuestra historia sigue a un gran caballero Sith,",
                  "Que busca sin descanso a los malvados Jedi por los planetas de la galaxia."]

        pos_x = ANCHO_PANTALLA - 1200
        contador_lugar = 0

        for frase in frases:
            texto_render = self.historia.render(
                (frase), True, COLOR_ROJO)
            self.pantalla.blit(
                texto_render, (pos_x, lugar_pantalla[contador_lugar]))
            contador_lugar += 1

    def pintar_texto_iniciar(self):
        mensaje = "Pulsa <B> para volver a la pantalla de inicio"
        texto = self.titulo_instrucciones.render(
            mensaje, True, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA - 100
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_texto_musica(self):
        mensaje = "Pulsa <a> para pausar/reaundar la música"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))


class Pantalla_Jugar(Pantalla):

    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.jugador = Nave()
        # self.puntuacion = puntuacion
        imagen_jugar = os.path.join(
            "resources", "images", "fondo_pantalla_jugar.jpg")
        self.pantalla_jugar = pg.image.load(imagen_jugar)

        imagen_planeta = pg.image.load(os.path.join(
            "resources", "images", "planeta.png"))
        self.planeta = Planeta(imagen_planeta)

        self.asteroides = pg.sprite.Group()
        self.crear_asteroides(5, 10, 5)

    def bucle_principal(self):

        ticks_juego = pg.time.get_ticks()
        # PONER EN EL INIT
        salir = False
        aterrizaje = False
        self.musica_fondo()

        self.jugador.vidas = 3

        while not salir:
            self.reloj.tick(FPS)
            tiempo_juego = (pg.time.get_ticks() - ticks_juego)//900

            for event in pg.event.get():

                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return "SALIR"
                if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ESTO SIRVE PARA PARAR LA MUSICA PULSANDO A
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.stop()
                    else:
                        pg.mixer_music.play(-1, 0.0)

            self.pintar_fondo()
            self.pintar_vidas()
            self.pintar_puntuacion()
            self.pintar_texto_musica()
            self.jugador.update()
            self.aparece_planeta(aterrizaje)
            if not aterrizaje:
                self.pintar_asteroides()
            self.colisionar_y_puntos(aterrizaje, 5, 10, 5)

            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            if tiempo_juego >= 25:
                aterrizaje = True

            if self.jugador.terminar_rotar:
                self.pintar_texto_continuar()
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                        return "PASAS"

            if self.jugador.vidas <= 0:
                print("Has muerto")
                # Aquí iría un stop, y que se elija si camibar de pantalla o no
                return "0"

            pg.display.flip()

    def pintar_fondo(self):

        # self.pantalla.fill((0, 0, 0)) # TODO: Todo esto qeu he ido copiando de arriba, sobra puesto que la pintalla no hay que pintarla, ya tiene una imagen de fondo
        self.pantalla.blit(self.pantalla_jugar, (0, 0))

    def pintar_vidas(self):
        vidas = self.jugador.vidas
        mensaje = f"VIDAS = {vidas}"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA - 50
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_puntuacion(self):
        puntuacion = Asteroide.puntuacion
        mensaje = f"PUNTOS = {puntuacion}"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        pos_x = ANCHO_PANTALLA / 40
        pos_y = ALTO_PANTALLA - 50
        self.pantalla.blit(texto, (pos_x, pos_y))

    def musica_fondo(self):
        pg.mixer.init()
        musica_fondo = os.path.join("resources", "sounds", "musica_juego.mp3")
        pg.mixer.music.load(musica_fondo)
        pg.mixer.music.set_volume(0.75)
        pg.mixer.music.play(-1, 0.0)

    def sonido_explosion(self):
        sonido_explosion = os.path.join(
            "resources", "sounds", "sonido_explosion.mp3")
        self.sound_explosion = pg.mixer.Sound(sonido_explosion)
        self.sound_explosion.play()

    def pintar_texto_musica(self):
        mensaje = "Pulsa <a> para pausar/reaundar la música"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))

    def aparece_planeta(self, aterrizar):
        self.jugador.update()
        if not aterrizar:
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
        else:
            self.pantalla.blit(self.planeta.image, self.planeta.rect)
            self.planeta.aparece_planeta(aterrizar)
            self.jugador.aterrizando_nave(aterrizar, self.pantalla)

    def crear_asteroides(self, min_asteroide, max_asteroide, n_puntos):

        # if not aterrizaje:
        #     num_asteroides = randint(min_asteroide, max_asteroide)
        # else:
        #     num_asteroides = 0
        num_asteroides = randint(min_asteroide, max_asteroide)
        for asteroid in range(num_asteroides):
            n_puntos = (asteroid + n_puntos) - n_puntos
            asteroide = Asteroide(n_puntos)
            self.asteroides.add(asteroide)
            if asteroide.rect.right < 0:
                self.puntuacion += 10

    def pintar_asteroides(self):
        self.asteroides.update()
        self.asteroides.draw(self.pantalla)

    def colisionar_y_puntos(self, aterrizar, min, max, puntos):
        if not aterrizar:
            hit = pg.sprite.spritecollide(self.jugador, self.asteroides, True)
            if hit:
                self.jugador.nave_golpeada()
                self.jugador.vidas -= 1

            for asteroide in self.asteroides.sprites():
                if asteroide.rect.x < 0:
                    if not self.jugador.nave_esconder:
                        Asteroide.puntuacion += puntos
                    # self.asteroides.remove(asteroide)

            if len(self.asteroides.sprites()) < 3:
                self.crear_asteroides(5, 10, 5)

        else:
            self.asteroides.clear(self.pantalla, self.pantalla)

    def pintar_texto_continuar(self):
        mensaje = "Pulsa <espacio> para el siguiente nivel"
        texto = self.titulo.render(mensaje, True, (COLOR_BLANCO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA * 5/8
        self.pantalla.blit(texto, (pos_x, pos_y))


class Pantalla_Jugar2(Pantalla):

    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.jugador = Nave()
        imagen_jugar = os.path.join(
            "resources", "images", "fondo_pantalla_jugar2.jpg")
        self.pantalla_jugar = pg.image.load(imagen_jugar)

        # FIXME:
        imagen_planeta = pg.image.load(os.path.join(
            "resources", "images", "planeta.png"))
        self.planeta = Planeta(imagen_planeta)

        self.asteroides = pg.sprite.Group()
        # FIXME: Esto quizás sea mejor sacar a variables globales
        # FIXME: llamar desde objeto asteroide

    def bucle_principal(self):
        # super().bucle_principal()  # FIXME: Quitar
        ticks_juego = pg.time.get_ticks()

        # PONER EN EL INIT
        salir = False
        self.musica_fondo()

        aterrizaje = False

        while not salir:
            self.reloj.tick(FPS)

            tiempo_juego = (pg.time.get_ticks() - ticks_juego)//900
            self.jugador.vidas = self.jugador.vidas
            for event in pg.event.get():

                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return "SALIR"

                # if self.jugador.terminar_rotar:
                #     pass
                # TODO: Colocar aquí que al pulsar tecla, pase al siguiente nivel?

                if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ESTO SIRVE PARA PARAR LA MUSICA PULSANDO A
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.stop()
                    else:
                        pg.mixer_music.play(-1, 0.0)

            # self.pantalla.fill((0, 0, 0))
            self.pintar_fondo()
            self.pintar_vidas()
            self.pintar_puntuacion()
            self.pintar_texto_musica()
            self.jugador.update()
            self.aparece_planeta(aterrizaje)
            self.pintar_asteroides()
            self.colisionar_y_puntos(aterrizaje, 5, 10, 5)

            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            if tiempo_juego >= 25:
                aterrizaje = True

            if self.jugador.terminar_rotar:
                self.pintar_texto_ganador()
                if tiempo_juego >= 30:
                    return "RECORDS"

            if self.jugador.vidas <= 0:
                print("Has muerto")
                # Aquí iría un stop, y que se elija si camibar de pantalla o no
                return "0"

            pg.display.flip()

    def pintar_fondo(self):

        self.pantalla.fill((0, 0, 0))
        self.pantalla.blit(self.pantalla_jugar, (0, 0))

    def musica_fondo(self):
        pg.mixer.init()
        musica_fondo = os.path.join("resources", "sounds", "musica_juego2.mp3")
        pg.mixer.music.load(musica_fondo)
        pg.mixer.music.set_volume(0.75)
        pg.mixer.music.play(-1, 0.0)

    def sonido_explosion(self):
        sonido_explosion = os.path.join(
            "resources", "sounds", "sonido_explosion.mp3")
        self.sound_explosion = pg.mixer.Sound(sonido_explosion)
        self.sound_explosion.play()

    def pintar_texto_musica(self):
        mensaje = "Pulsa <a> para pausar/reaundar la música"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA * 1/28
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_vidas(self):
        vidas = self.jugador.vidas
        mensaje = f"VIDAS = {vidas}"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        anchura_texto = texto.get_width()
        pos_x = ANCHO_PANTALLA - (anchura_texto + 20)
        pos_y = ALTO_PANTALLA - 50
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_puntuacion(self):
        puntuacion = Asteroide.puntuacion
        mensaje = f"PUNTOS = {puntuacion}"
        texto = self.extra_musica.render(mensaje, False, (COLOR_AMARILLO))
        pos_x = ANCHO_PANTALLA / 40
        pos_y = ALTO_PANTALLA - 50
        self.pantalla.blit(texto, (pos_x, pos_y))

    def aparece_planeta(self, aterrizar):
        self.jugador.update()
        if not aterrizar:
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
        else:
            self.pantalla.blit(self.planeta.image, self.planeta.rect)
            self.planeta.aparece_planeta(aterrizar)
            self.jugador.aterrizando_nave(aterrizar, self.pantalla)

    def crear_asteroides(self, min_asteroide, max_asteroide, n_puntos):

        # if not aterrizaje:
        #     num_asteroides = randint(min_asteroide, max_asteroide)
        # else:
        #     num_asteroides = 0
        num_asteroides = randint(min_asteroide, max_asteroide)
        for asteroid in range(num_asteroides):
            n_puntos = (asteroid + n_puntos) - n_puntos
            asteroide = Asteroide(n_puntos)
            self.asteroides.add(asteroide)

    def pintar_asteroides(self):
        self.asteroides.update()
        self.asteroides.draw(self.pantalla)

    def colisionar_y_puntos(self, aterrizar, min, max, puntos):
        if not aterrizar:
            hit = pg.sprite.spritecollide(self.jugador, self.asteroides, True)
            if hit:
                self.jugador.nave_golpeada()
                self.jugador.vidas -= 1

            for asteroide in self.asteroides.sprites():
                if asteroide.rect.right < 0:
                    if not self.jugador.nave_esconder:
                        Asteroide.puntuacion += puntos
                    self.asteroides.remove(asteroide)

            if len(self.asteroides.sprites()) < 3:
                self.crear_asteroides(10, 20, 6)

        else:
            self.asteroides.clear(self.pantalla, self.pantalla)

    def pintar_texto_ganador(self):
        mensaje = "EL IMPERIO AGRADECE TUS SERVICIOS"
        texto = self.titulo_instrucciones.render(mensaje, True, (COLOR_ROJO))
        anchura_texto = texto.get_width()
        pos_x = (ANCHO_PANTALLA - anchura_texto) / 2
        pos_y = ALTO_PANTALLA * 5/8
        self.pantalla.blit(texto, (pos_x, pos_y))


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
