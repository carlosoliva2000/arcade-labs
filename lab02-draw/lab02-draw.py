from time import sleep

import arcade
import random

# Variables de ventana
ANCHO = 800
ALTO = 600

arcade.open_window(ANCHO, ALTO, "Prueba")
arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

# Inicialización de renderizado
arcade.start_render()

# Cielo
color_arriba = arcade.csscolor.YELLOW
color_abajo = arcade.csscolor.DARK_RED
colores_cielo = (color_arriba, color_arriba, color_abajo, color_abajo)
puntos_cielo = ((0, ALTO), (ANCHO, ALTO), (ANCHO, ALTO / 4), (0, ALTO / 4))
arcade.create_rectangle_filled_with_colors(puntos_cielo, colores_cielo).draw()

# Sol
arcade.draw_circle_filled(ANCHO / 2, ALTO / 3, 100, arcade.csscolor.INDIANRED)

# Suelo
arcade.draw_lrtb_rectangle_filled(0, ANCHO, ALTO / 4, 0, (36, 54, 35))

# Arbol
# puntos_arbol = ((20, 20), (500, 20), (400, 400), (100, 350))
# arcade.draw_polygon_filled(puntos_arbol, arcade.color.BLACK)
# arcade.draw_rectangle_filled(ANCHO/2, ALTO/3.5, 10, 100, arcade.color.BLACK)

# Finalización de renderizado
arcade.finish_render()

# Mantiene la ventana abierta
arcade.run()
