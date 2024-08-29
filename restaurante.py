import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import time

class AplicativoRestaurante:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante do Ederson")
        self.root.configure(background="#13293D")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('Highlighted.TButton', background='#4caf50', foreground='#ffffff')

        self.pedidos = {}
        self.tela_login()

    def tela_login(self):
        self.frame_login = tk.Frame(self.root, bg="turquoise")
        self.frame_login.pack(fill=tk.BOTH, expand=True)

        label_usuario = ttk.Label(self.frame_login, text="Digite seu usuário:", font=("Arial", 20), background="turquoise", foreground='white')
        label_usuario.grid(column=0, row=0, padx=10, pady=5, sticky="w")
        self.entry_usuario = tk.Entry(self.frame_login, font=("Arial", 16))
        self.entry_usuario.grid(column=0, row=1, padx=10, pady=5)

        label_senha = ttk.Label(self.frame_login, text="Digite sua senha:", font=("Arial", 20), background="turquoise", foreground='white')
        label_senha.grid(column=0, row=2, padx=10, pady=5, sticky="w")
        self.entry_senha = tk.Entry(self.frame_login, font=("Arial", 16), show="*")
        self.entry_senha.grid(column=0, row=3, padx=10, pady=5)

        label_confirmar_senha = ttk.Label(self.frame_login, text="Confirme sua senha:", font=("Arial", 20), background="turquoise", foreground='white')
        label_confirmar_senha.grid(column=0, row=4, padx=10, pady=5, sticky="w")
        self.entry_confirmar_senha = tk.Entry(self.frame_login, font=("Arial", 16), show="*")
        self.entry_confirmar_senha.grid(column=0, row=5, padx=10, pady=5)

        self.label_resultado = ttk.Label(self.frame_login, text="", font=("Arial", 16), background="turquoise", foreground='white')
        self.label_resultado.grid(column=0, row=6, padx=10, pady=10)

        botao_cadastrar = ttk.Button(self.frame_login, text="Cadastrar", style="Highlighted.TButton", command=self.cadastro_realizado)
        botao_cadastrar.grid(column=0, row=7, padx=10, pady=10)

    def cadastro_realizado(self):
        usuario_texto = self.entry_usuario.get().strip()
        senha_texto = self.entry_senha.get().strip()
        confirmar_senha_texto = self.entry_confirmar_senha.get().strip()
        
        if not usuario_texto or not senha_texto or not confirmar_senha_texto:
            self.label_resultado.config(text="Campo não preenchido, confira os campos de cadastro e tente novamente.", foreground="red")
        elif senha_texto != confirmar_senha_texto:
            self.label_resultado.config(text="Senhas não coincidem!!", foreground="red")
        elif usuario_texto == senha_texto:
            self.label_resultado.config(text="Usuário e senha não podem coincidir!", foreground="red")
        else:
            self.label_resultado.config(text="Cadastro realizado com sucesso!", foreground="green")
            self.frame_login.pack_forget()
            self.pagina_logada()

    def pagina_logada(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Abas
        self.frame_menu = tk.Frame(self.notebook, bg="#13293D")
        self.notebook.add(self.frame_menu, text="Cardápio")

        self.frame_finalizar_pedido = tk.Frame(self.notebook, bg="#13293D")
        self.notebook.add(self.frame_finalizar_pedido, text="Finalizar Pedido")

        self.frame_dados_cliente = tk.Frame(self.notebook, bg="#13293D")
        self.notebook.add(self.frame_dados_cliente, text="Dados do Cliente")

        self.dados_cliente()
        self.menu()
        self.pedidos_pendentes()

    def dados_cliente(self):
        lbl_nome = tk.Label(self.frame_dados_cliente, text="Nome:", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_nome.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_nome = tk.Entry(self.frame_dados_cliente, font=("Arial", 12), bg="#ffffff", bd=0)
        self.entry_nome.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        lbl_mesa = tk.Label(self.frame_dados_cliente, text="Mesa:", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_mesa.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_mesa = tk.Entry(self.frame_dados_cliente, font=("Arial", 12), bg="#ffffff", bd=0)
        self.entry_mesa.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_quantidade = tk.Label(self.frame_dados_cliente, text="Quantidade de itens:", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_quantidade.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.entry_quantidade = tk.Entry(self.frame_dados_cliente, font=("Arial", 12), bg="#ffffff", bd=0)
        self.entry_quantidade.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    def menu(self,dados_cliente):
        self.dados_cliente (self.entry_nome.get()=)
        lbl_cardapio = tk.Label(self.frame_menu, text="Olá,"nome_cliente, font=("Arial", 16, "bold"), bg="#1b98e0")
        lbl_cardapio.pack(padx=20, pady=(19, 9))

        lbl_cardapio = tk.Label(self.frame_menu, text="Cardápio", font=("Arial", 14, "bold"), bg="#1b98e0")
        lbl_cardapio.pack(padx=20, pady=(20, 10))

        lbl_aviso = tk.Label(self.frame_menu, text="Por Favor,insira os dados da sua mesa para adicionar os pedidos!", font=("Arial", 10), bg="#1b98e0")
        lbl_aviso.pack(padx=21, pady=(21, 11))

        self.lista_pedidos = tk.Listbox(self.frame_menu, font=("Arial", 12), bg="#006494", bd=0, highlightthickness=0)
        self.lista_pedidos.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.frame_cardapio = tk.Frame(self.frame_menu, bg="#006494")
        self.frame_cardapio.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Definição do cardápio
        self.itens_cardapio = [
            {'nome': 'Bebidas', 'imagem': 'bebidas.jpg'},
            {'nome': 'Cachorro Quente', 'imagem': 'catioro-quente.jpg'},
            {'nome': 'Pastel Duvidoso', 'imagem': 'pastelzin.jpg'},
            {'nome': 'Cachorrao Caramelo (sim é comestivel)', 'imagem': 'cachorro-caramelo.jpg'},
            {'nome': 'A boa ne pae 🤭😎', 'imagem': 'a-boa.jpg'},
        ]
        
        for item in self.itens_cardapio:
            frame_item = tk.Frame(self.frame_cardapio, bg="#006494")
            frame_item.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

            caminho_imagem = os.path.join("Imagens", item["imagem"])
            if not os.path.isfile(caminho_imagem):
                print(f"Imagem não encontrada: {caminho_imagem}")
                continue
            
            imagem = Image.open(caminho_imagem)
            imagem = imagem.resize((50, 50))
            foto = ImageTk.PhotoImage(imagem)
            label = tk.Label(frame_item, text=item["nome"], font=("Arial", 12), bg="#006494")
            label.pack(side=tk.LEFT)

            label_imagem = tk.Label(frame_item, image=foto, bg="#006494")
            label_imagem.image = foto
            label_imagem.pack(side=tk.LEFT, padx=10)

            botao_adicionar = ttk.Button(frame_item, text="Adicionar ao Pedido", style="Highlighted.TButton", command=lambda item=item["nome"]: self.fazer_pedido(item))
            botao_adicionar.pack(side=tk.RIGHT, padx=10)

    def pedidos_pendentes(self):
        lbl_pedidos_pendentes = tk.Label(self.frame_finalizar_pedido, text="Pedidos Pendentes", font=("Arial", 14, "bold"), bg="#1b98e0")
        lbl_pedidos_pendentes.pack(padx=20, pady=(20, 10))
        
        lbl_aviso = tk.Label(self.frame_finalizar_pedido, text="Clique no seu pedido para seleciona-lo!", font=("Arial", 10 ), bg="#1b98e0")
        lbl_aviso.pack(padx=21, pady=(21, 11))

        self.lista_pedidos_pendentes = tk.Listbox(self.frame_finalizar_pedido, font=("Arial", 12), bg="#006494", bd=0, highlightthickness=0)
        self.lista_pedidos_pendentes.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        frame_botoes = tk.Frame(self.frame_finalizar_pedido, bg="#13293D")
        frame_botoes.pack(pady=(10, 20))

        self.botao_remover_pedido = ttk.Button(frame_botoes, text="Retirar Pedido", style="Highlighted.TButton", command=self.remover_pedido)
        self.botao_remover_pedido.grid(row=0, column=0, padx=10)

        self.botao_finalizar_pedido = ttk.Button(frame_botoes, text="Finalizar Pedido", style="Highlighted.TButton", command=self.finalizar_pedido)
        self.botao_finalizar_pedido.grid(row=0, column=1, padx=10)

    def fazer_pedido(self, nome_item):
        nome_cliente = self.entry_nome.get().strip()
        numero_mesa = self.entry_mesa.get().strip()
        quantidade = self.entry_quantidade.get().strip()

        if nome_cliente and numero_mesa:
            if not quantidade.isdigit():
                quantidade = "1"
            else:
                quantidade = int(quantidade)
            
            if nome_item in self.pedidos:
                self.pedidos[nome_item] += quantidade
            else:
                self.pedidos[nome_item] = quantidade
            
            self.atualizar_lista_pedidos()
            self.mostrar_mensagem("Sucesso", "Item adicionado ao pedido com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha o nome do cliente e o número da mesa.")

    def atualizar_lista_pedidos(self):
        self.lista_pedidos.delete(0, tk.END)
        for item, quantidade in self.pedidos.items():
            texto_pedido = f"{item} - Quantidade: {quantidade}"
            self.lista_pedidos.insert(tk.END, texto_pedido)

    def remover_pedido(self):
        indices_selecionados = self.lista_pedidos_pendentes.curselection()
        if not indices_selecionados:
            messagebox.showwarning("Aviso", "Nenhum pedido selecionado para retirar.")
            return
        for index in indices_selecionados:
            texto_pedido = self.lista_pedidos_pendentes.get(index)
            item = texto_pedido.split(" - ")[0]
            quantidade = int(texto_pedido.split("Quantidade: ")[1])
            
            if item in self.pedidos:
                if self.pedidos[item] <= quantidade:
                    del self.pedidos[item]
                else:
                    self.pedidos[item] -= quantidade
            
            self.lista_pedidos_pendentes.delete(index)
            self.atualizar_lista_pedidos()
        self.mostrar_mensagem("Sucesso", "Pedido retirado com sucesso!")
        

    def finalizar_pedido(self):
        indices_selecionados = self.lista_pedidos.curselection()
        if not indices_selecionados:
            messagebox.showwarning("Aviso", "Nenhum pedido selecionado para finalizar.")
            return
        for index in indices_selecionados:
            texto_pedido = self.lista_pedidos.get(index)
            self.lista_pedidos_pendentes.insert(tk.END, texto_pedido)
            self.lista_pedidos.delete(index)
        self.mostrar_mensagem("Sucesso", "Pedido finalizado com sucesso!")
        time.sleep (3)
        root.quit()
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

root = tk.Tk()
app = AplicativoRestaurante(root)
root.mainloop()
