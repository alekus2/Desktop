from tkinter import *
from tkinter import ttk
def contar_cliques():
    global contador
    contador += 1
    print ("Voce clicou: ",contador)
root = Tk()
contador = 0
frm = ttk.Frame(root, padding=200)
frm.grid()
label_contador = ttk.Label(frm, text="Clique no botão :D", font=("Arial", 60))
label_contador.grid(column=0, row=0)
botao_contador = Button(frm, text="Clica ai meu querido",font=("Arial",7), command=contar_cliques)
botao_contador.grid(column=0, row=1)
root.mainloop() 