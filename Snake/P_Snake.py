import turtle
import time

# Configuração da tela
tela = turtle.Screen()
tela.title("Jogo da cobrinha")
tela.bgcolor("black")
tela.setup(width=600, height=600)

# Configuração da cobra
cobra = turtle.Turtle()
cobra.speed(10)
cobra.color("white")
cobra.penup()
cobra.goto(0,0)
cobra.direction = "stop"
cobra.shape("square")
cobra.shapesize(stretch_wid=1, stretch_len=1)

# Configuração da comida
comida = turtle.Turtle()
comida.speed(0)
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.shape("circle")

# Função para mover a cobra
def mover_cobra():
    if cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)
    
    if cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)
    
    if cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)
    
    if cobra.direction == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)

# Função para mudar a direção da cobra
def mudar_direcao_cima():
    cobra.direction = "up"

def mudar_direcao_baixo():
    cobra.direction = "down"

def mudar_direcao_esquerda():
    cobra.direction = "left"

def mudar_direcao_direita():
    cobra.direction = "right"

# Configuração de teclado
turtle.listen()
turtle.onkeypress(mudar_direcao_cima, "Up")
turtle.onkeypress(mudar_direcao_baixo, "Down")
