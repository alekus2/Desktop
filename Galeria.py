import tkinter as tk
from tkinter import ttk
class App(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Galeria MC sapao")
        self.grid(column=0, row=0, padx=300, pady=300)
        frm = ttk.Frame(self)
        frm.grid(column=0, row=0, sticky='nsew')

        frase = ttk.Label(frm, text="MC sapao", font=("Arial", 30))
        frase.grid(column=0, row=1, padx=10, pady=10)
        #FOTOS DA GALERIA
        try:
            foto = tk.PhotoImage(file="Imagens/sapo.png")
            foto = foto.subsample(2, 2)
            figura = tk.Label(frm, image=foto)
            figura.image = foto 
            figura.grid(column=0, row=0, padx=1, pady=1)
        except tk.TclError:
            print("Erro ao carregar a imagem. Verifique o caminho.")

        #USUARIO       
        self.frm_usuario = tk.Frame(self, padx=20, pady=20)
        self.frm_usuario.grid(column=0, row=1, padx=10, pady=10)

        self.label_usuario = tk.Label(self.frm_usuario, text="Digite uma descrição", font=("Arial", 20))
        self.label_usuario.grid(column=0, row=0)

        self.teclaenterusuario = tk.Entry(self.frm_usuario)
        self.teclaenterusuario.grid(column=0, row=1)

        #RESULTADO DESCRIÇÃO
        self.resultado_label = ttk.Label(frm, text=" ", font=("Arial", 20))
        self.resultado_label.grid(column=0, row=2, padx=10, pady=10)

        #BOTAO SALVAR
        self.botao_salvar = ttk.Button(frm, text="Salvar", command=self.salvar_descricao)
        self.botao_salvar.grid(column=0, row=3, padx=10, pady=10)
    

    def salvar_descricao(self):
        try:
          descricao = self.teclaenterusuario.get().strip() 
          if descricao:
            self.resultado_label.config(text=f"{descricao}", font=("Arial", 20))
          if hasattr(self, 'teclaenterusuario'):
            self.teclaenterusuario.destroy()
            del self.teclaenterusuario
          if hasattr(self, 'label_usuario'):
            self.label_usuario.destroy()
            del self.label_usuario
        except AttributeError:
            print ("nao da nao man")
    def mudar_imagem (fotos):
        global img_tk
        image_path= imagens [fotos]


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.grid()  
    root.mainloop()