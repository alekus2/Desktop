from tkinter import *
import math

root = Tk()
root.title("Calculadora do Alek")
root.geometry("320x390")
cor_main = "#13283d"

frame_resultado = Frame(root, width=320, height=90, bg=cor_main)
frame_resultado.grid(row=0, column=0)

corpo = Frame(root, width=320, height=300)
corpo.grid(row=1, column=0)

# FUNÇÃO VALORES 

valor = ''

def on_off():
    root.quit()

def entrar_valor1(event):
    global valor
    valor += str(event)
    valor_texto.set(valor)

def backspace():
    global valor
    valor = valor[:-1]
    valor_texto.set(valor)

def calcular():
    global valor
    valor = valor.replace("^", "**").replace("÷","/").replace("×","*").replace(",",".")
    if "%" in valor:
        while "%" in valor:
            idx = valor.index("%")
            left_part = valor[:idx].rstrip()
            if left_part:
                if left_part[-1] in "+-*/":
                    left_part = left_part[:-1]
                try:
                    left_value = eval(left_part)
                except:
                    left_value = 1 
                valor = valor[:idx] + f"*{left_value}/100" + valor[idx+1:]
    if "√" in valor:
        valor = valor.replace("√", "math.sqrt(") + ")"
    try:
        resultado = eval(valor, {"math": math})
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado = int(resultado)
        valor_texto.set(resultado)
        valor = str(resultado)
    except Exception as e:
        valor_texto.set("Erro")
        valor = ''

# CALCULADORA
valor_texto = StringVar()
conta_label = Label(frame_resultado, textvariable=valor_texto, width=12, height=4, padx=145, relief=FLAT, anchor="e", justify="right", font="Ivy 18", bg=cor_main)
conta_label.place(x=5, y=20)

# BOTÕES
# PRIMEIRA SESSÃO
botao1 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1 ("%"), text="%", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao1.place(x=0, y=0)

botao2 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1(""), text="C", font=("Ivy 13 bold"), bg="#ff9933", relief=RAISED, overrelief=RIDGE)
botao2.place(x=80, y=0)

botao3 = Button(corpo, width=7, height=2, command=lambda: valor_texto.set(''), text="CE", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao3.place(x=160, y=0)

botao4 = Button(corpo, width=7, height=2, command=backspace, text="⌦", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao4.place(x=240, y=0)

# SEGUNDA SESSÃO
botao5 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("√"), text="√", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao5.place(x=0, y=51)

botao6 = Button(corpo, width=7, height=2, command=lambda: valor_texto.set(''), text="AC", font=("Ivy 13 bold"), bg="#ff9933", relief=RAISED, overrelief=RIDGE)
botao6.place(x=80, y=51)

botao7 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("^"), text="^", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao7.place(x=160, y=51)

botao8 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("÷"), text="÷", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao8.place(x=240, y=51)

# TERCEIRA SESSÃO
botao9 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("7"), text="7", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao9.place(x=0, y=102)

botao10 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("8"), text="8", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao10.place(x=80, y=102)

botao11 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("9"), text="9", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao11.place(x=160, y=102)

botao12 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("×"), text="×", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao12.place(x=240, y=102)

# QUARTA SESSÃO
botao13 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("4"), text="4", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao13.place(x=0, y=153)

botao14 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("5"), text="5", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao14.place(x=80, y=153)

botao15 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("6"), text="6", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao15.place(x=160, y=153)

botao16 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("-"), text="-", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao16.place(x=240, y=153)

# QUINTA SESSÃO
botao17 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("1"), text="1", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao17.place(x=0, y=204)

botao18 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("2"), text="2", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao18.place(x=80, y=204)

botao19 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("3"), text="3", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao19.place(x=160, y=204)

botao20 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("+"), text="+", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao20.place(x=240, y=204)

# SEXTA SESSÃO
botao21 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("0"), text="0", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao21.place(x=0, y=256)

botao22 = Button(corpo, width=7, height=2, command=lambda: entrar_valor1("00"), text="00", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao22.place(x=80, y=256)

botao23= Button(corpo,width=7,height=2,command= lambda: entrar_valor1 (","),text="‚",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao23.place(x=160,y=256)

botao24= Button(corpo,width=7,height=2,command= calcular,text="=",font=("Ivy 13 bold"),bg=cor_main,foreground="WHITE",relief=RAISED,overrelief=RIDGE)
botao24.place(x=240,y=256)

root.mainloop()