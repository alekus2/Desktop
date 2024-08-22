from tkinter import *
from tkinter import ttk

root = Tk()
frm = Frame(root, padx=400, pady=400, background="turquoise")
frm.grid()

# #USUARIO
usuario = Entry(frm, font=("Arial", 20))
usuario.grid(column=0, row=1, padx=10, pady=10)
label_usuario = ttk.Label(frm, text="Digite seu usuário.", font=("Arial", 40), background="turquoise", foreground='white')
label_usuario.grid(column=0, row=0)

# #SENHA
senha = Entry(frm, font=("Arial", 20), show="*")
senha.grid(column=0, row=3, padx=10, pady=10)
label_senha = ttk.Label(frm, text="Digite sua senha.", font=("Arial", 40), background="turquoise", foreground='white')
label_senha.grid(column=0, row=2)

# #CONFIRMAR SENHA
confirmar_senha = Entry(frm, font=("Arial", 20), show="*")
confirmar_senha.grid(column=0, row=5, padx=10, pady=10)
label_confirmar_senha = ttk.Label(frm, text="Confirme sua senha.", font=("Arial", 40), background="turquoise", foreground='white')
label_confirmar_senha.grid(column=0, row=4)

resultado_label = ttk.Label(frm, text="", font=("Arial", 20), background="turquoise", foreground='white')
resultado_label.grid(column=0, row=7, padx=10, pady=10)

def cadastro_realizado():
    usuario_text = usuario.get().strip()
    senha_text = senha.get().strip()
    confirmar_senha_text = confirmar_senha.get().strip()
    
    if not usuario_text or not senha_text or not confirmar_senha_text:
        resultado_label.config(text="Campo não preenchido, confira os campos de cadastro e tente novamente.", foreground="red")
    elif senha_text != confirmar_senha_text:
        resultado_label.config(text="Senhas não coincidem!!", foreground="red")
    elif usuario_text == senha_text:
        resultado_label.config(text="Usuário e senha não podem coincidir!", foreground="red")
    else:
        resultado_label.config(text="Cadastro Realizado com Sucesso! :D", foreground="green")

# BOTAO LOGIN
botao_salvar = ttk.Button(frm, text="LOGIN", command=cadastro_realizado)
botao_salvar.grid(column=0, row=6, padx=10, pady=10)

root.mainloop()