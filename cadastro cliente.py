import tkinter as tk
from tkinter import *

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Cadastro Cliente")
        self.pack(padx=20, pady=20)  

        # Frame para o nome de usuário
        self.frm_usuario = tk.Frame(self, padx=100, pady=100)
        self.frm_usuario.pack()

        self.label_usuario = tk.Label(self.frm_usuario, text="Digite seu nome de usuário.", font=("Arial", 50),foreground="pink")
        self.label_usuario.pack()

        self.usuario = tk.StringVar()
        self.teclaenterusuario["textvariable"] = self.usuario

        # Frame para a senha
        self.frm_senha = tk.Frame(self, padx=100, pady=100)
        self.frm_senha.pack()

        self.label_senha = tk.Label(self.frm_senha, text="Digite sua senha.", font=("Arial", 50))
        self.label_senha.pack()

        self.teclaentersenha = tk.Entry(self.frm_senha, show="*")  # Mostrar caracteres como asteriscos
        self.teclaentersenha.pack()

        self.senha = tk.StringVar()
        self.teclaentersenha["textvariable"] = self.senha

        # Bind de eventos para a tecla Enter
        self.teclaenterusuario.bind('<Return>', self.imprimir_terminal_usuario)
        self.teclaentersenha.bind('<Return>', self.imprimir_terminal_senha)

    def imprimir_terminal_usuario(self, event):
        print("Nome de usuário:", self.usuario.get())

    def imprimir_terminal_senha(self, event):
        print("Senha:", self.senha.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()