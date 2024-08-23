from tkinter import *
from tkinter import Tk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Cadastro Cliente")
        self.pack(padx=20, pady=20)  

        # Frame para o nome de usuário
        self.frm_usuario = frame(self, padx=20, pady=20)
        self.frm_usuario.pack()

        self.label_usuario = Label(self.frm_usuario, text="Digite seu nome de usuário.", font=("Arial", 20))
        self.label_usuario.pack()

        self.teclaenterusuario = Entry(self.frm_usuario)
        self.teclaenterusuario.pack()

        self.usuario = tk.StringVar()
        self.teclaenterusuario["textvariable"] = self.usuario

        # Frame para a senha
        self.frm_senha = Frame(self, padx=20, pady=20)
        self.frm_senha.pack()

        self.label_senha = Label(self.frm_senha, text="Digite sua senha.", font=("Arial", 20))
        self.label_senha.pack()

        self.teclaentersenha = Entry(self.frm_senha, show="*")  # Mostrar caracteres como asteriscos
        self.teclaentersenha.pack()

        self.senha = tk.StringVar()
        self.teclaentersenha["textvariable"] = self.senha

        # Bind de eventos para a tecla Enter
        self.teclaenterusuario.bind('<Return>', self.imprimir_terminal_usuario)
        self.teclaentersenha.bind('<Return>', self.imprimir_terminal_senha)

    def imprimir_terminal_usuario(self, event):
        # Imprime apenas o valor do campo de usuário
        print("Nome de usuário:", self.usuario.get())

    def imprimir_terminal_senha(self, event):
        # Imprime apenas o valor do campo de senha
        print("Senha:", self.senha.get())

if __name__ == "__main__":
    root = Tk ()
    app = App(root)
    app.mainloop()
