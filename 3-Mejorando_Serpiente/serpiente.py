import turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)] #Constantes en mayusculas
DISTANCIA_MOVER = 20
ARRIBA = 90
ABAJO = 270
IZQUIERDA = 180
DERECHA = 0

class Serpiente:
    def __init__(self):
        self.segmentos = []
        self.crear_serpiente()
        self.cabeza = self.segmentos[0]

    def crear_serpiente(self):
        for posicion in POSICIONES_INICIALES:
            nuevo_segmento = turtle.Turtle("square") #Acepta el shape en el constructor de clase.
            nuevo_segmento.penup()
            nuevo_segmento.color("white")
            nuevo_segmento.goto(posicion)
            self.segmentos.append(nuevo_segmento)

    def mover(self):
        for seg_num in range(len(self.segmentos) - 1, 0, -1): #Empezar en el último segmento, ir hasta el segmento 0 de -1 en -1.
            nueva_x = self.segmentos[seg_num - 1].xcor()
            nueva_y = self.segmentos[seg_num - 1].ycor()
            self.segmentos[seg_num].goto(nueva_x, nueva_y)
        self.cabeza.forward(DISTANCIA_MOVER) #Movemos la cabeza y todo el cuerpo la sigue.
        
    def arriba(self):
        if self.cabeza.heading() != ABAJO:
            self.cabeza.setheading(ARRIBA)
    
    def abajo(self):
        if self.cabeza.heading() != ARRIBA:
            self.cabeza.setheading(ABAJO)
    
    def izquierda(self):
        if self.cabeza.heading() != DERECHA:
            self.cabeza.setheading(IZQUIERDA)
    
    def derecha(self):
        if self.cabeza.heading() != IZQUIERDA:
            self.cabeza.setheading(DERECHA)
