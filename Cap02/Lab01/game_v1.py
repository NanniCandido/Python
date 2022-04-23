# Game Ping-Pong

from tkinter import *
import random
import time

# Atribuição do nível desejado pelo usuário à variável 'level'
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
# Atribuição do nível desejado pelo usuário à variável 'level'
length = 500/level


root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Dimensionamento da tela
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
# Inicialização das variáveis 'count' e 'lost'
count = 0
lost = False

# Inicio da programação da classe 'bola'
class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

# Lista 
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
    # Coordenadas da tela cfe a bola vai se movendo
        self.canvas.move(self.id, self.x, self.y)

# Atribuição das coordenadas de tela na variável 'pos'
        pos = self.canvas.coords(self.id)

# Testa a posição da bola na tela e atribui à Y
        if pos[1] <= 0:
            self.y = 3
# Testa altura da bola na tela e atribui à Y
        if pos[3] >= self.canvas_height:
            self.y = -3
# Testa a posição da bola na tela e atribui à X
        if pos[0] <= 0:
            self.x = 3
 # Testa largura da bola na tela e atribui à Y e uso de operadores relacionais       
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

# Uso de operadores relacionais
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
# Uso de operadores relacionais (duas operações em um mesmo cálculo)
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

# Inicio da programação da classe 'Barra'
class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        
# Atribuição de zero
        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
# Atribuição
        self.pos = self.canvas.coords(self.id)
# Condição
        if self.pos[0] <= 0:
            self.x = 0
 # Condição       
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
# Condição  
        if lost == False:
            self.canvas.after(10, self.draw)
            
# criação do objeto de movimento para esquerda
    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3
# criação do objeto de movimento para direita
    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# criação do objeto de início de jogo
def start_game(event):
# incialização de variáveis globais
    global lost, count
# incialização de variáveis locais ao objeto    
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()

# criação do objeto de final de pontuação
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# criação do objeto de final de jogo
def game_over():
    canvas.itemconfig(game, text="Game over!")

# Tuplas
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()



