from tkinter import *

root = Tk()
root.title("Calculadora do Alek")
root.geometry("320x500")
cor_main="#13283d"

resultado = Frame(root,width=320,height=135,bg=cor_main)
resultado.grid(row=0,column=0)

corpo=Frame(root,width=320,height=300)
corpo.grid(row=1,column=0)

botao1= Button(corpo,width=14,height=4,text="C")
botao1.place(x=0,y=0)

root.mainloop()