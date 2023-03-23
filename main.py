from the_quest_sith_edition.game import The_Quest, ALTO_PANTALLA, ANCHO_PANTALLA


if __name__ == "__main__":
    print(
        f"El tamaño de pantalla es {ALTO_PANTALLA} Alto x {ANCHO_PANTALLA} Ancho")
    juego = The_Quest()
    juego.jugando()
