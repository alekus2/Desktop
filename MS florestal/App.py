from tkinter import *
from tkinter import ttk
import csv
import tkinter as tk

def carregar_talhoes(arquivo):
    talhoes = {}
    try:
        with open(arquivo, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header is None:
                print("O arquivo CSV está vazio.")
                return talhoes
            for row in reader:
                if len(row) < 2:
                    continue  
                try:
                    talhao = int(row[0]) 
                    parcelas_talho = int(row[1]) 
                    talhoes[talhao] = parcelas_talho
                except ValueError:
                    print(f"Erro ao converter dados na linha: {row}.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")    
    return talhoes

def contagem(talhoes):
    novos_talhoes = {} 
    for talhao, parcelas_talho in talhoes.items():
        if talhao % 2 == 0:
            if parcelas_talho < 3:
                parcela_nova = parcelas_talho
            elif parcelas_talho % 2 == 0:
                parcela_nova = parcelas_talho // 2
            else:
                parcela_nova = (parcelas_talho + 1) // 2
            
            novos_talhoes[talhao] = parcela_nova

    with open('Talhão_atualizado.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Talhao', 'Parcelas Atualizadas'])
        for talhao, parcelas in novos_talhoes.items():
            spamwriter.writerow([talhao, parcelas]) 

def apagar_talhoes(talhoes):
    apagador_talhoes = {}
    for talhao, parcelas_talho in talhoes.items():
        if talhao % 2 >= 1:
            if parcelas_talho < 3:
                parcelas_novas = parcelas_talho
            elif parcelas_talho % 2 == 0:
                parcelas_novas = parcelas_talho // 2
            else:
                parcelas_novas = (parcelas_talho + 1) // 2
            apagador_talhoes[talhao] = parcelas_novas
    return apagador_talhoes 

def main_salvar():
    caminho = caminho_relativo.get().strip()
    if caminho == "":
        resultado_label.config(text="Campo não preenchido!", foreground="red")
        return
    talhoes = carregar_talhoes(caminho)
    if talhoes:
        contagem(talhoes)
        resultado_label.config(text="Contagem realizada com sucesso!", foreground="green")
        resultado_label2.config(text="Verifique seus arquivos na barra de arquivos :)", foreground='#e0e0e0')
    else:
        resultado_label.config(text="Arquivo não encontrado.", foreground="red")

def main_apagar():
    caminho = caminho_relativo.get().strip()
    if caminho == "":
        resultado_label.config(text="Campo não preenchido!", foreground="red")
        return
    talhoes = carregar_talhoes(caminho)  # Carregue os talhões primeiro
    if talhoes:
        apagados = apagar_talhoes(talhoes)  # Chame a função e capture o resultado
        if apagados:
            contagem(apagados)  # Contagem com os talhões apagados
            resultado_label.config(text="Talhões apagados com sucesso!", foreground="green")
            resultado_label2.config(text="Verifique seus arquivos na barra de arquivos :)", foreground='#e0e0e0')
        else:
            resultado_label.config(text="Nenhum talhão apagado.", foreground="orange")
    else:
        resultado_label.config(text="Arquivo não encontrado.", foreground="red")

root = Tk()
root.title("Contador Rural")
root.geometry("600x450")  # Ajuste o tamanho da janela conforme necessário


frm = Frame(root, padx=150, pady=250, background="#66cc00", width=800, height=500)
frm.grid(row=1, column=1, sticky=(N, S, E, W))

# Carregando a imagem e posicionando-a dentro do frame
imagem = PhotoImage(file="logo.png")
label_imagem = Label(frm, image=imagem, background="#66cc00")
label_imagem.place(x=0,y=0)

# Mensagem inicio
label_msg = ttk.Label(frm, text="Olá, Bem-vindo ao CONTADOR RURAL", font=("Cambria", 16), background="#66cc00", foreground='#e0e0e0')
label_msg.place(x=130,y=10)
# Label e entry para caminho relativo
label_msg2 = ttk.Label(frm, text="Preencha o campo abaixo com o caminho relativo do arquivo que deseja contar.", font=("Cambria", 10), background="#66cc00", foreground='#e0e0e0')
label_msg2.place(x=130,y=40)
caminho_relativo = Entry(frm, font=("Arial", 10))
caminho_relativo.place(x=130, y=75)

# Resultado da validação
resultado_label = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label.place(x=20,y=150)

resultado_label2 = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label2.place(x=0,y=200)

# Botão apagar
botao_apagar = ttk.Button(frm, text="Apagar", command=main_apagar)
botao_apagar.place(x=215, y=110)

# Botão salvar
botao_salvar = ttk.Button(frm, text="Salvar", command=main_salvar)
botao_salvar.place(x=115, y=110)

# Inicia o loop principal da interface gráfica
root.mainloop()

