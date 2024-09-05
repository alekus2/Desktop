from tkinter import *

root = Tk()
root.title("Calculadora do Alek")
root.geometry("320x435")
cor_main="#13283d"

resultado = Frame(root,width=320,height=135,bg=cor_main)
resultado.grid(row=0,column=0)

corpo=Frame(root,width=320,height=300)
corpo.grid(row=1,column=0)

#PRIMEIRA SESSÃO

botao1= Button(corpo,width=7,height=2,text="%",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao1.place(x=0,y=0)

botao2= Button(corpo,width=7,height=2,text="C",font=("Ivy 13 bold"),bg="#ff9933",relief=RAISED,overrelief=RIDGE)
botao2.place(x=80,y=0)

botao3= Button(corpo,width=7,height=2,text="CE",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao3.place(x=160,y=0)

botao4= Button(corpo,width=7,height=2,text="⌦",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao4.place(x=240,y=0)

#SEGUNDA SESSÃO

botao5= Button(corpo,width=7,height=2,text="√",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao5.place(x=0,y=51)

botao6= Button(corpo,width=7,height=2,text="AC",font=("Ivy 13 bold"),bg="#ff9933",relief=RAISED,overrelief=RIDGE)
botao6.place(x=80,y=51)

botao7= Button(corpo,width=7,height=2,text="+/-",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao7.place(x=160,y=51)

botao8= Button(corpo,width=7,height=2,text="÷",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao8.place(x=240,y=51)

#TERCEIRA SESSÃO

botao9= Button(corpo,width=7,height=2,text="7",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao9.place(x=0,y=102)

botao10= Button(corpo,width=7,height=2,text="8",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao10.place(x=80,y=102)

botao11= Button(corpo,width=7,height=2,text="9",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao11.place(x=160,y=102)

botao12= Button(corpo,width=7,height=2,text="×",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao12.place(x=240,y=102)

#QUARTA SESSÃO

botao13= Button(corpo,width=7,height=2,text="4",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao13.place(x=0,y=153)

botao14= Button(corpo,width=7,height=2,text="5",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao14.place(x=80,y=153)

botao15= Button(corpo,width=7,height=2,text="6",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao15.place(x=160,y=153)

botao16= Button(corpo,width=7,height=2,text="-",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao16.place(x=240,y=153)

#QUINTA SESSÃO

botao17= Button(corpo,width=7,height=2,text="1",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao17.place(x=0,y=204)

botao18= Button(corpo,width=7,height=2,text="2",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao18.place(x=80,y=204)

botao19= Button(corpo,width=7,height=2,text="3",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao19.place(x=160,y=204)

botao20= Button(corpo,width=7,height=2,text="+",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao20.place(x=240,y=204)

#SEXTA SESSÃO

botao21= Button(corpo,width=7,height=2,text="0",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao21.place(x=0,y=256)

botao22= Button(corpo,width=7,height=2,text="00",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao22.place(x=80,y=256)

botao23= Button(corpo,width=7,height=2,text="‚",font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
botao23.place(x=160,y=256)

botao24= Button(corpo,width=7,height=2,text="=",font=("Ivy 13 bold"),bg=cor_main,foreground="WHITE",relief=RAISED,overrelief=RIDGE)
botao24.place(x=240,y=256)


root.mainloop()