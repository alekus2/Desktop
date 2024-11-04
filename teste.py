# import random
# import os

# numero_aleatorio=random.randint(1,10)
# chute=input ("Tente adivinhar o numero entre 1 e 10. \n")
# chute=int(chute)
# while True:
#     if chute == numero_aleatorio:
#         print ("Voce ganhou :D")
#         break
#     else:
#         print ("vc errou ,o numero era ",numero_aleatorio)


# import csv

# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# from pptx import Presentation

# apresentacao = Presentation()

# # editar o ppt 
# slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[0]) # slide com titulo e subtitulo
# # slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[6]) # slide em branco

# titulo = slide1.shapes.title 
# subtitulo = slide1.placeholders[1]

# titulo.text = "1º Slide do Lira"
# subtitulo.text = "Tamo criando ppt com Python"

# # salvar esse ppt
# apresentacao.save("MeuPPT.pptx")



# import csv

# def contagem(talhoes):
#     novos_talhoes = {}
    
#     for talhao, parcelas_talho in talhoes.items():
#         if parcelas_talho < 3:
#             parcela_nova = parcelas_talho
#         else:
#             if parcelas_talho % 2 == 0:
#                 parcela_nova = parcelas_talho // 2
#             else:
#                 parcela_nova = (parcelas_talho + 1) // 2
#         novos_talhoes[talhao] = parcela_nova

#     # Escreve os dados no arquivo CSV fora do loop
#     with open('Talhão_atualizado.csv', 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(['Talhão', 'Parcelas Atualizadas'])  # Cabeçalho
#         for talhao, parcelas in novos_talhoes.items():
#             spamwriter.writerow([talhao, parcelas])  # Escreve cada talhão com suas parcelas atualizadas

# # Exemplo de uso
# talhoes = {
#     'Talhão 1': 10,
#     'Talhão 2': 12,
#     'Talhão 3': 16
# }
# contagem(talhoes)

# import csv

# def contagem(talhoes):
#     novos_talhoes = {}

#     for talhao, parcelas_talho in talhoes.items():
#         if talhao % 2 == 0:  # Apenas para talhões pares
#             if parcelas_talho < 3:
#                 parcela_nova = parcelas_talho
#             elif parcelas_talho % 2 == 0:
#                 parcela_nova = parcelas_talho // 2
#             else:
#                 parcela_nova = (parcelas_talho + 1) // 2
            
#             novos_talhoes[talhao] = parcela_nova

#     # Escrevendo os resultados em um arquivo CSV
#     with open('Talhão_atualizado.csv', 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(['Talhão', 'Parcelas Atualizadas'])
#         for talhao, parcelas in novos_talhoes.items():
#             spamwriter.writerow([talhao, parcelas]) 
# contagem(talhoes)

# import csv

# def carregar_talhoes(arquivo):
#     talhoes = {}
#     try:
#         with open(arquivo, mode='r') as file:
#             reader = csv.reader(file)
#             header = next(reader, None)
#             if header is None:
#                 print("O arquivo CSV está vazio.")
#                 return talhoes
#             for row in reader:
#                 if len(row) < 2:
#                     continue  
#                 try:
#                     talhao = int(row[0]) 
#                     parcelas_talho = int(row[1]) 
#                     talhoes[talhao] = parcelas_talho
#                 except ValueError:
#                     print(f"Erro ao converter dados na linha: {row}.")
#     except FileNotFoundError:
#         print("Arquivo não encontrado. Verifique o nome do arquivo.")
#     except Exception as e:
#         print(f"Ocorreu um erro: {e}")    
#     return talhoes

# def contagem(talhoes):
#     novos_talhoes = {} 
#     for talhao, parcelas_talho in talhoes.items():
#         if talhao % 2 == 0:
#             if parcelas_talho < 3:
#                 parcela_nova = parcelas_talho
#             elif parcelas_talho % 2 == 0:
#                 parcela_nova = parcelas_talho // 2
#             else:
#                 parcela_nova = (parcelas_talho + 1) // 2
            
#             novos_talhoes[talhao] = parcela_nova

#     with open('Talhão_atualizado.csv', 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(['Talhão', 'Parcelas Atualizadas'])
#         for talhao, parcelas in novos_talhoes.items():
#             spamwriter.writerow([talhao, parcelas]) 

# def main():
#     arquivo = r'G:\Alex Qualidade\Atividades-SENAC-AGOST\MS florestal\tls.csv'  
#     talhoes = carregar_talhoes(arquivo)
#     if talhoes:
#         contagem(talhoes)
#     else:
#         print("Nenhum talhão carregado.")

# main()

# from tkinter import *
# from tkinter import ttk
# import csv

# def carregar_talhoes(arquivo):
#     talhoes = {}
#     try:
#         with open(arquivo, mode='r') as file:
#             reader = csv.reader(file)
#             header = next(reader, None)
#             if header is None:
#                 print("O arquivo CSV está vazio.")
#                 return talhoes
#             for row in reader:
#                 if len(row) < 2:
#                     continue  
#                 try:
#                     talhao = int(row[0]) 
#                     parcelas_talho = int(row[1]) 
#                     talhoes[talhao] = parcelas_talho
#                 except ValueError:
#                     print(f"Erro ao converter dados na linha: {row}.")
#     except FileNotFoundError:
#         print("Arquivo não encontrado. Verifique o nome do arquivo.")
#     except Exception as e:
#         print(f"Ocorreu um erro: {e}")    
#     return talhoes

# def contagem(talhoes):
#     novos_talhoes = {} 
#     for talhao, parcelas_talho in talhoes.items():
#         if talhao % 2 == 0:
#             if parcelas_talho < 3:
#                 parcela_nova = parcelas_talho
#             elif parcelas_talho % 2 == 0:
#                 parcela_nova = parcelas_talho // 2
#             else:
#                 parcela_nova = (parcelas_talho + 1) // 2
            
#             novos_talhoes[talhao] = parcela_nova

#     with open('Talhão_atualizado.csv', 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(['Talhao', 'Parcelas Atualizadas'])
#         for talhao, parcelas in novos_talhoes.items():
#             spamwriter.writerow([talhao, parcelas]) 

# def apagar_talhoes(talhoes):
#     apagador_talhoes = {}
#     for talhao, parcelas_talho in talhoes.items():
#         if talhao % 2 >= 1:
#             if parcelas_talho < 3:
#                 parcelas_novas = parcelas_talho
#             elif parcelas_talho % 2 == 0:
#                 parcelas_novas = parcelas_talho // 2
#             else:
#                 parcelas_novas = (parcelas_talho + 1) // 2
#             apagador_talhoes[talhao] = parcelas_novas
#     return apagador_talhoes 

# def main_salvar():
#     caminho = caminho_relativo.get().strip()
#     if caminho == "":
#         resultado_label.config(text="Campo não preenchido!", foreground="red")
#         return
#     talhoes = carregar_talhoes(caminho)
#     if talhoes:
#         contagem(talhoes)
#         resultado_label.config(text="Contagem realizada com sucesso!", foreground="green")
#         resultado_label2.config(text="Verifique seus arquivos na barra de arquivos :)", foreground='#e0e0e0')
#     else:
#         resultado_label.config(text="Arquivo não encontrado.", foreground="red")

# def main_apagar():
#     caminho = caminho_relativo.get().strip()
#     if caminho == "":
#         resultado_label.config(text="Campo não preenchido!", foreground="red")
#         return
#     talhoes = carregar_talhoes(caminho)  # Carregue os talhões primeiro
#     if talhoes:
#         apagados = apagar_talhoes(talhoes)  # Chame a função e capture o resultado
#         if apagados:
#             contagem(apagados)  # Contagem com os talhões apagados
#             resultado_label.config(text="Talhões apagados com sucesso!", foreground="green")
#             resultado_label2.config(text="Verifique seus arquivos na barra de arquivos :)", foreground='#e0e0e0')
#         else:
#             resultado_label.config(text="Nenhum talhão apagado.", foreground="orange")
#     else:
#         resultado_label.config(text="Arquivo não encontrado.", foreground="red")

# root = Tk()
# root.title("Contador Rural")
# root.geometry("850x550")  # Ajuste o tamanho da janela conforme necessário

# frm = Frame(root, padx=200, pady=200, background="#66cc00", width=800, height=500)
# frm.grid(row=0, column=1, sticky=(N, S, E, W))

# # Mensagem inicio
# label_msg = ttk.Label(frm, text="Olá, Bem-vindo ao CONTADOR RURAL", font=("Cambria", 16), background="#66cc00", foreground='#e0e0e0')
# label_msg.grid(column=0, row=1, padx=10, pady=5, sticky=W)

# # Label e entry para caminho relativo
# label_msg2 = ttk.Label(frm, text="Preencha o campo abaixo com o caminho relativo do arquivo que deseja contar.", font=("Cambria", 10), background="#66cc00", foreground='#e0e0e0')
# label_msg2.grid(column=0, row=3, padx=10, pady=5, sticky=W)
# caminho_relativo = Entry(frm, font=("Arial", 10))
# caminho_relativo.place(x=130, y=75)

# # Resultado da validação
# resultado_label = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
# resultado_label.grid(column=0, row=8, padx=10, pady=10)

# resultado_label2 = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
# resultado_label2.grid(column=0, row=9, padx=10, pady=10)

# # Botão apagar
# botao_apagar = ttk.Button(frm, text="Apagar", command=main_apagar)
# botao_apagar.place(x=215, y=110)

# # Botão salvar
# botao_salvar = ttk.Button(frm, text="Salvar", command=main_salvar)
# botao_salvar.place(x=115, y=110)

# # Inicia o loop principal da interface gráfica
# root.mainloop()

from tkinter import *
from tkinter import ttk
import csv

def carregar_talhoes(arquivo):
    # Sua função para carregar talhões
    pass

def contagem(talhoes):
    # Sua função para contagem
    pass

def apagar_talhoes(talhoes):
    # Sua função para apagar talhões
    pass

def main_salvar():
    # Sua função para salvar
    pass

def main_apagar():
    # Sua função para apagar
    pass

root = Tk()
root.title("Contador Rural")
root.geometry("600x450")

# Frame principal
frm = Frame(root, padx=100, pady=200, background="#66cc00")
frm.grid(row=0, column=0, sticky=(N, S, E, W))

# Carregando a imagem e posicionando-a dentro do frame
imagem = PhotoImage(file="logo.png")
label_imagem = Label(frm, image=imagem, background="#66cc00")
label_imagem.grid(row=0, column=0, padx=10, pady=10)

# Mensagem de início
label_msg = ttk.Label(frm, text="Olá, Bem-vindo ao CONTADOR RURAL", font=("Cambria", 16), background="#66cc00", foreground='#e0e0e0')
label_msg.grid(column=0, row=1, padx=10, pady=5, sticky=W)

# Outros widgets...
label_msg2 = ttk.Label(frm, text="Preencha o campo abaixo com o caminho relativo do arquivo que deseja contar.", font=("Cambria", 10), background="#66cc00", foreground='#e0e0e0')
label_msg2.grid(column=0, row=3, padx=10, pady=5, sticky=W)

caminho_relativo = Entry(frm, font=("Arial", 10))
caminho_relativo.grid(column=0, row=4, padx=10, pady=5, sticky=W)

# Resultado da validação
resultado_label = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label.grid(column=0, row=5, padx=10, pady=5, sticky=W)

resultado_label2 = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label2.grid(column=0, row=6, padx=10, pady=5, sticky=W)

# Botões
botao_apagar = ttk.Button(frm, text="Apagar", command=main_apagar)
botao_apagar.grid(column=0, row=7, padx=10, pady=5, sticky=W)

botao_salvar = ttk.Button(frm, text="Salvar", command=main_salvar)
botao_salvar.grid(column=0, row=8, padx=10, pady=5, sticky=W)

# Inicia o loop principal da interface gráfica
root.mainloop()


# Carregando a imagem e posicionando-a dentro do frame
imagem = PhotoImage(file="logo.png")
label_imagem = Label(frm, image=imagem, background="#66cc00")
label_imagem.place(x=0, y=0)

# Ajuste a posição do texto para que ele fique sobre a imagem
label_msg = ttk.Label(frm, text="Olá, Bem-vindo ao CONTADOR RURAL", font=("Cambria", 16), background="#66cc00", foreground='#e0e0e0')
label_msg.place(x=50, y=30)  # Ajuste as coordenadas conforme necessário

label_msg2 = ttk.Label(frm, text="Preencha o campo abaixo com o caminho relativo do arquivo que deseja contar.", font=("Cambria", 10), background="#66cc00", foreground='#e0e0e0')
label_msg2.place(x=50, y=70)  # Ajuste as coordenadas conforme necessário
