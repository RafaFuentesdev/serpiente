import turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)] #Constantes en mayusculas

class Serpiente:
    def __init__(self):
        self.segmentos = []
        self.crear_serpiente()

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
        self.segmentos[0].forward(20) #Movemos la cabeza y todo el cuerpo la sigue.
        
    def arriba(self):
        self.segmentos[0].setheading(90)
    
    def abajo(self):
        self.segmentos[0].setheading(270)
    
    def izquierda(self):
        self.segmentos[0].setheading(180)
    
    def derecha(self):
        self.segmentos[0].setheading(0)
