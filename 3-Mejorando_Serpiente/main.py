import turtle
import time

from serpiente import Serpiente

ventana = turtle.Screen()
ventana.setup(width=600, height=600)
ventana.bgcolor("black")
ventana.title("Snake Game")

ventana.tracer(0)

serpiente = Serpiente() ##----------CREAR LA SERPIENTE----------##

ventana.listen()
ventana.onkey(serpiente.arriba, "Up")
ventana.onkey(serpiente.abajo, "Down")
ventana.onkey(serpiente.izquierda, "Left")
ventana.onkey(serpiente.derecha, "Right")

     
en_juego = True
while en_juego:
    ventana.update()
    time.sleep(0.1)
    
    serpiente.mover() ##----------MOVER LA SERPIENTE----------##
    
ventana.exitonclick()
