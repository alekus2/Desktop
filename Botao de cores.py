from tkinter import *

root = Tk()
frm = Frame(root, padx=400, pady=400, background="white")
frm.grid()
def cor_vermelha():
    frm.config(background="red")
# BOTAO COR VERMELHA
botao_vermelho= Button(frm, text="Vermelho",font=("Arial",20),foreground="black",command=cor_vermelha)
botao_vermelho.grid(column=0, row=0, padx=10, pady=10)

def cor_azul():
    frm.config(background="blue")
# BOTAO COR AZUL
botao_vermelho= Button(frm, text="Azul",font=("Arial",20),foreground="black",command=cor_azul)
botao_vermelho.grid(column=1, row=0, padx=10, pady=10)

def cor_amarela():
    frm.config(background="yellow")
# BOTAO COR AMARELO
botao_vermelho= Button(frm, text="Amarelo",font=("Arial",20),foreground="black",command=cor_amarela)
botao_vermelho.grid(column=2, row=0, padx=10, pady=10)


root.mainloop()