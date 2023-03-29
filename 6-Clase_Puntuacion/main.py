#main.py
import turtle
import time

from serpiente import Serpiente
from comida import Comida
from puntuacion import Puntuacion

ventana = turtle.Screen()
ventana.setup(width=600, height=600)
ventana.bgcolor("black")
ventana.title("Snake Game")

ventana.tracer(0)

serpiente = Serpiente()   ##---------- CREAR LA SERPIENTE --------------##
comida = Comida()         ##---------- CREAR LA COMIDA -----------------##
puntuacion = Puntuacion() ##---------- CREAR LA PUNTUACION -------------##

ventana.listen()
ventana.onkey(serpiente.arriba, "Up")
ventana.onkey(serpiente.abajo, "Down")
ventana.onkey(serpiente.izquierda, "Left")
ventana.onkey(serpiente.derecha, "Right")

en_juego = True
while en_juego:
    ventana.update()
    time.sleep(0.1)
    serpiente.mover() ##---------- MOVER LA SERPIENTE ----------##
    
    ##----------DETECTAR COLISIONES COMIDA ----------##
    if serpiente.cabeza.distance(comida) < 15:
        comida.actualizar()
        puntuacion.incrementar_puntuacion()
    
ventana.exitonclick()
