import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Galeria MC sapao")
        self.master.configure(bg='turquoise')
        self.grid(column=0, row=0, padx=300, pady=300, sticky='nsew')

        frm = tk.Frame(self, background="turquoise")  # 
        frm.grid(column=0, row=0, sticky='nsew')

        frase = ttk.Label(frm, text="MC sapao", font=("Arial", 30), background="turquoise")
        frase.grid(column=0, row=1, padx=10, pady=10)

        # FOTOS DA GALERIA
        self.img_index = 0  
        self.imagens = [
            'Imagens/sapo.png',
            'Imagens/sapao.jpg',
            'Imagens/ratao.jpg',
            'Imagens/catioro-do-mau.jpg',
            'Imagens/sistem-safadow.jpg',
            'Imagens/sapo.png'
        ]
        
        # EXIBIR IMAGEM
        self.label_imagem = tk.Label(frm, background="turquoise")
        self.label_imagem.grid(column=0, row=0, padx=10, pady=10)
        self.atualizar_imagem()

        # BOTAO PRÓXIMO
        self.botao_anterior = ttk.Button(frm, text="Anterior", command=self.mudar_imagem_anterior)
        self.botao_anterior.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        self.botao_proximo = ttk.Button(frm, text="Próximo", command=self.mudar_imagem_proxima)
        self.botao_proximo.grid(column=0, row=2, padx=10, pady=10, sticky='e')

        # USUARIO
        self.frm_usuario = tk.Frame(self, padx=20, pady=20) 
        self.frm_usuario.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')

        self.label_usuario = tk.Label(self.frm_usuario, text="Digite uma descrição", font=("Arial", 20)                                                                                               )
        self.label_usuario.grid(column=0, row=0)

        self.teclaenterusuario = tk.Entry(self.frm_usuario)
        self.teclaenterusuario.grid(column=0, row=1)
        
        # RESULTADO DESCRIÇÃO
        self.resultado_label = ttk.Label(frm, text=" ", font=("Arial", 20), background="turquoise")
        self.resultado_label.grid(column=0, row=3, padx=10, pady=10)

        # BOTÃO SALVAR
        self.botao_salvar = ttk.Button(frm, text="Salvar", command=self.salvar_descricao)
        self.botao_salvar.grid(column=0, row=4, padx=10, pady=10)

    def atualizar_imagem(self):
        image_path = self.imagens[self.img_index]
        img = Image.open(image_path)
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        self.label_imagem.config(image=img_tk)
        self.label_imagem.image = img_tk

    def mudar_imagem_anterior(self):
        if self.img_index > 0:
            self.img_index -= 1
        else:
            self.img_index = len(self.imagens) - 1 
        self.atualizar_imagem()

    def mudar_imagem_proxima(self):
        if self.img_index < len(self.imagens) - 1:
            self.img_index += 1
        else:
            self.img_index = 0  
        self.atualizar_imagem()

    def salvar_descricao(self):
        descricao = self.teclaenterusuario.get().strip()
        if descricao:
            self.resultado_label.config(text=f"{descricao}", font=("Arial", 20))
            self.botao_salvar.config(text="Sair", command=self.master.destroy)
            
        if hasattr(self, 'teclaenterusuario'):
            self.teclaenterusuario.destroy()
            del self.teclaenterusuario
        if hasattr(self, 'label_usuario'):
            self.label_usuario.destroy()
            del self.label_usuario

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
