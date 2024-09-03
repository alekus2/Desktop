import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os


class AplicativoRestaurante:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante do Ederson")
        self.root.configure(background="#ffff66")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('Highlighted.TButton', background='#4caf50', foreground='#ffffff')

        self.pedidos = {}
        self.tela_login()

    def tela_login(self):
        self.frame_login = tk.Frame(self.root, padx=20, pady=20, background="#ffff66", width=800, height=700)
        self.frame_login.pack(fill=tk.BOTH, expand=True)

        self.logo_frame = tk.Frame(self.frame_login, background="#ffff66", width=400, height=600)
        self.logo_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.label_imagem = tk.Label(self.logo_frame, background="#ffff66")
        self.label_imagem.pack(fill=tk.BOTH, expand=True)

        self.imagens = [
            'Imagens/Logo pizzaria.png',
            'Imagens/Logo-tipo-sem-fundo.png'
        ]
        self.img_index = 0
        self.logo_pizzaria()

        self.frm = tk.Frame(self.frame_login, padx=20, pady=20, background="#ffff66", width=400, height=600)
        self.frm.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.logo_pequena_frame = tk.Frame(self.frm, background="#ffff66")
        self.logo_pequena_frame.grid(row=0, column=0, padx=1, pady=1, sticky=tk.W)

        self.label_logo_pequena = tk.Label(self.logo_pequena_frame, background="#ffff66")
        self.label_logo_pequena.pack()

        self.logo_pequena()

        tk.Label(self.frm, text="Digite seu usuário:", font=("Constantia", 20), background="#ffff66", foreground='#ff9933').grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.usuario = tk.Entry(self.frm, font=("Arial", 16))
        self.usuario.grid(column=0, row=2, padx=10, pady=5)

        tk.Label(self.frm, text="Digite sua senha:", font=("Constantia", 20), background="#ffff66", foreground='#ff9933').grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
        self.senha = tk.Entry(self.frm, font=("Arial", 16), show="*")
        self.senha.grid(column=0, row=4, padx=10, pady=5)

        tk.Label(self.frm, text="Confirme sua senha:", font=("Constantia", 20), background="#ffff66", foreground='#ff9933').grid(column=0, row=5, padx=10, pady=5, sticky=tk.W)
        self.confirmar_senha = tk.Entry(self.frm, font=("Arial", 16), show="*")
        self.confirmar_senha.grid(column=0, row=6, padx=10, pady=5)

        self.resultado_label = tk.Label(self.frm, text="", font=("Constantia", 16), background="#ffff66", foreground='#ff9933')
        self.resultado_label.grid(column=0, row=8, padx=10, pady=10)

        tk.Button(self.frm, text="LOGIN", command=self.cadastro_realizado).grid(column=0, row=7, padx=10, pady=10)

    def logo_pizzaria(self):
        image_path = self.imagens[self.img_index]
        img = Image.open(image_path)
        img = img.resize((400, 700))  # Ajuste para cobrir toda a área
        img_tk = ImageTk.PhotoImage(img)
        self.label_imagem.config(image=img_tk)
        self.label_imagem.image = img_tk

    def logo_pequena(self):
        image_path = 'Imagens/Logo-tipo-sem-fundo.png'
        img = Image.open(image_path)
        img = img.resize((250, 250))  # Ajuste o tamanho da imagem pequena conforme necessário
        img_tk = ImageTk.PhotoImage(img)
        self.label_logo_pequena.config(image=img_tk)
        self.label_logo_pequena.image = img_tk

    def cadastro_realizado(self):
        usuario_texto = self.usuario.get().strip()
        senha_texto = self.senha.get().strip()
        confirmar_senha_texto = self.confirmar_senha.get().strip()
        
        if not usuario_texto or not senha_texto or not confirmar_senha_texto:
            self.resultado_label.config(text="Campo não preenchido, confira os campos de cadastro e tente novamente.", foreground="red")
        elif senha_texto != confirmar_senha_texto:
            self.resultado_label.config(text="Senhas não coincidem!!", foreground="red")
        elif usuario_texto == senha_texto:
            self.resultado_label.config(text="Usuário e senha não podem coincidir!", foreground="red")
        else:
            self.resultado_label.config(text="Cadastro realizado com sucesso!", foreground="green")
            self.frame_login.pack_forget()
            self.pagina_logada(usuario_texto)

    def pagina_logada(self, usuario_nome):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.frame_menu = tk.Frame(self.notebook, bg="#ff9933")
        self.notebook.add(self.frame_menu, text="Cardápio")

        self.frame_finalizar_pedido = tk.Frame(self.notebook, bg="#ff9933")
        self.notebook.add(self.frame_finalizar_pedido, text="Finalizar Pedido")

        self.frame_dados_cliente = tk.Frame(self.notebook, bg="#ff9933")
        self.notebook.add(self.frame_dados_cliente, text="Dados do Cliente")

        self.dados_cliente()
        self.menu(usuario_nome)
        self.pedidos_pendentes()

    def dados_cliente(self):
        tk.Label(self.frame_dados_cliente, text="Nome:", font=("Constantia", 14, "bold"), bg="#f0f0f0").grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_nome = tk.Entry(self.frame_dados_cliente, font=("Constantia", 12), bg="#ffffff", bd=0)
        self.entry_nome.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        tk.Label(self.frame_dados_cliente, text="Mesa:", font=("Constantia", 14, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_mesa = tk.Entry(self.frame_dados_cliente, font=("Constantia", 12), bg="#ffffff", bd=0)
        self.entry_mesa.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self.frame_dados_cliente, text="Quantidade de itens:", font=("Constantia", 14, "bold"), bg="#f0f0f0").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.entry_quantidade = tk.Entry(self.frame_dados_cliente, font=("Constantia", 12), bg="#ffffff", bd=0)
        self.entry_quantidade.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    def menu(self, usuario_nome):
        tk.Label(self.frame_menu, text=f"Olá, {usuario_nome}", font=("Gil Sans", 16, "bold"), bg="#ff9933").pack(padx=20, pady=(19, 9))
        tk.Label(self.frame_menu, text="Cardápio", font=("Gil Sans", 14, "bold"), bg="#ff9933").pack(padx=20, pady=(20, 10))
        tk.Label(self.frame_menu, text="Por Favor, insira os dados da sua mesa para adicionar os pedidos!", font=("Constantia", 10), bg="#ff9933").pack(padx=21, pady=(21, 11))
        
        self.lista_pedidos = tk.Listbox(self.frame_menu, font=("Constantia", 12), bg="#ffff66", bd=0, highlightthickness=0, selectmode=tk.MULTIPLE)
        self.lista_pedidos.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.frame_cardapio = tk.Frame(self.frame_menu, bg="#ffff66")
        self.frame_cardapio.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.itens_cardapio = [
            {'nome': 'Bebidas', 'imagem': 'bebidas.jpg'},
            {'nome': 'Cachorro Quente', 'imagem': 'catioro-quente.jpg'},
            {'nome': 'Pastel Duvidoso', 'imagem': 'pastelzin.jpg'},
            {'nome': 'Cachorrao Caramelo (sim é comestivel)', 'imagem': 'cachorro-caramelo.jpg'},
            {'nome': 'A boa ne pae 🤭😎', 'imagem': 'a-boa.jpg'},
        ]
        
        for item in self.itens_cardapio:
            frame_item = tk.Frame(self.frame_cardapio, bg="#ffff66")
            frame_item.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

            caminho_imagem = os.path.join("Imagens", item["imagem"])
            if not os.path.isfile(caminho_imagem):
                print(f"Imagem não encontrada: {caminho_imagem}")
                continue
            
            imagem = Image.open(caminho_imagem)
            imagem = imagem.resize((50, 50))
            foto = ImageTk.PhotoImage(imagem)
            tk.Label(frame_item, text=item["nome"], font=("Gil Sans", 12), bg="#ffff66").pack(side=tk.LEFT)

            label_imagem = tk.Label(frame_item, image=foto, bg="#ffff66")
            label_imagem.image = foto
            label_imagem.pack(side=tk.LEFT, padx=10)

            botao_adicionar = ttk.Button(frame_item, text="Adicionar ao Pedido", style="Highlighted.TButton", command=lambda item=item["nome"]: self.fazer_pedido(item))
            botao_adicionar.pack(side=tk.RIGHT, padx=10)

        # Botão para adicionar todos os pedidos
        self.botao_adicionar_todos = ttk.Button(self.frame_menu, text="Adicionar Todos os Pedidos", style="Highlighted.TButton", command=self.adicionar_todos_pedidos)
        self.botao_adicionar_todos.pack(pady=10)

    def pedidos_pendentes(self):
        tk.Label(self.frame_finalizar_pedido, text="Pedidos Pendentes", font=("Gil Sans", 14, "bold"), bg="#ff9933").pack(padx=20, pady=(20, 10))
        
        tk.Label(self.frame_finalizar_pedido, text="Clique no seu pedido para seleciona-lo!", font=("Constantia", 10), bg="#ff9933").pack(padx=21, pady=(21, 11))

        self.lista_pedidos_pendentes = tk.Listbox(self.frame_finalizar_pedido, font=("Constantia", 12), bg="#ffff66", bd=0, highlightthickness=0, selectmode=tk.MULTIPLE)
        self.lista_pedidos_pendentes.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        frame_botoes = tk.Frame(self.frame_finalizar_pedido, bg="#ffff66")
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

    def adicionar_todos_pedidos(self):
        selecionados = self.lista_pedidos.curselection()
        if not selecionados:
            messagebox.showwarning("Aviso", "Nenhum pedido selecionado para adicionar.")
            return
        
        for index in selecionados:
            texto_pedido = self.lista_pedidos.get(index)
            item = texto_pedido.split(" - ")[0]
            quantidade = int(texto_pedido.split("Quantidade: ")[1])
            
            if item in self.pedidos:
                self.pedidos[item] += quantidade
            else:
                self.pedidos[item] = quantidade
        
        self.atualizar_lista_pedidos()
        self.mostrar_mensagem("Sucesso", "Todos os pedidos selecionados foram adicionados com sucesso!")

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
        self.root.quit()

    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoRestaurante(root)
    root.mainloop()
