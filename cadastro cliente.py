from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Função para validar e processar o cadastro
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
        resultado_label.config(text="Cadastro realizado com sucesso!", foreground="green")
        root.quit()

# Configuração da janela principal
root = Tk()
root.title("Login Form")
root.geometry("800x700")  # Ajuste o tamanho da janela conforme necessário

# Frame para a logo principal
logo_frame = Frame(root, background="#ffff66", width=400, height=600)
logo_frame.grid(row=0, column=0, sticky=(N, S, E, W))

# Logo principal da pizzaria
label_imagem = Label(logo_frame, background="#ffff66")
label_imagem.pack(fill=BOTH, expand=True)

# Lista de imagens e índice
img_index = 0
imagens = [
    'Imagens/Logo pizzaria.png',
    'Imagens/Logo-tipo-sem-fundo.png'
]

def logo_pizzaria():
    image_path = imagens[img_index]
    img = Image.open(image_path)
    img = img.resize((400, 800))  # Ajuste para cobrir toda a área
    img_tk = ImageTk.PhotoImage(img)
    label_imagem.config(image=img_tk)
    label_imagem.image = img_tk

# Inicializa a exibição da logo
logo_pizzaria()

# Frame principal para o formulário de login
frm = Frame(root, padx=65, pady=65, background="#ffff66", width=400, height=600)
frm.grid(row=0, column=1, sticky=(N, S, E, W))

# Logo pequena acima do formulário de login
logo_pequena_frame = Frame(frm, background="#ffff66")
logo_pequena_frame.grid(row=0, column=0, padx=1, pady=1, sticky=W)

# Logo pequena para o formulário
label_logo_pequena = Label(logo_pequena_frame, background="#ffff66")
label_logo_pequena.pack()

# Adicionar logo pequena (ajuste o caminho e tamanho conforme necessário)
def logo_pequena():
    image_path = 'Imagens/Logo-tipo-sem-fundo.png'  # Ajuste o caminho da logo pequena
    img = Image.open(image_path)
    img = img.resize((250, 250))  # Ajuste o tamanho da imagem pequena conforme necessário
    img_tk = ImageTk.PhotoImage(img)
    label_logo_pequena.config(image=img_tk)
    label_logo_pequena.image = img_tk

# Inicializa a exibição da logo pequena
logo_pequena()

# Label e Entry para usuário
label_usuario = ttk.Label(frm, text="Digite seu usuário:", font=("Agrandir", 20), background="#ffff66", foreground='#ff9933')
label_usuario.grid(column=0, row=1, padx=10, pady=5, sticky=W)
usuario = Entry(frm, font=("Arial", 16))
usuario.grid(column=0, row=2, padx=10, pady=5)

# Label e Entry para senha
label_senha = ttk.Label(frm, text="Digite sua senha:", font=("Agrandir", 20), background="#ffff66", foreground='#ff9933')
label_senha.grid(column=0, row=3, padx=10, pady=5, sticky=W)
senha = Entry(frm, font=("Arial", 16), show="*")
senha.grid(column=0, row=4, padx=10, pady=5)

# Label e Entry para confirmar senha
label_confirmar_senha = ttk.Label(frm, text="Confirme sua senha:", font=("Agrandir", 20), background="#ffff66", foreground='#ff9933')
label_confirmar_senha.grid(column=0, row=5, padx=10, pady=5, sticky=W)
confirmar_senha = Entry(frm, font=("Arial", 16), show="*")
confirmar_senha.grid(column=0, row=6, padx=10, pady=5)

# Resultado da validação
resultado_label = ttk.Label(frm, text="", font=("Agrandir", 16), background="#ffff66", foreground='#ff9933')
resultado_label.grid(column=0, row=8, padx=10, pady=10)

# Botão de login
botao_salvar = ttk.Button(frm, text="LOGIN", command=cadastro_realizado)
botao_salvar.grid(column=0, row=7, padx=10, pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
