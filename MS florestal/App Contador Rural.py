from tkinter import *
from tkinter import ttk
import csv
import pandas as pd

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
    novos_talhoes = pd.DataFrame ({})

    for talhao, parcelas in talhoes.items():
        if parcelas < 3:
            parcela_nova = parcelas
        elif parcelas % 2 == 0:
            parcela_nova = parcelas // 2
        else:
            parcela_nova = (parcelas + 1) // 2

        novos_talhoes[talhao] = [parcela_nova] 
    novos_talhoes = novos_talhoes.T  
    novos_talhoes.columns = ['Parcelas Atualizadas']  
    novos_talhoes.to_excel('Talhão_atualizado.xlsx', index_label='Talhão') 

def apagar_parcelas(talhoes):
    apagador_parcelas = {}
    for talhao, parcelas in talhoes.items():
        if parcelas <= 3:
            parcela_nova = parcelas
        elif parcelas % 2 == 0 and parcelas > 3:
            parcela_nova = parcelas // 2
        else:
            continue
        apagador_parcelas[talhao] = parcela_nova

    apagador_parcelas_df = pd.DataFrame(list(apagador_parcelas.items()), columns=['Talhão', 'Parcelas Atualizadas'])
    apagador_parcelas_df.to_excel('Talhão_atualizado.xlsx', index=False)
    return apagador_parcelas


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
    talhoes = carregar_talhoes(caminho) 
    if talhoes:
        apagados = apagar_parcelas(talhoes)
        if apagados:
            resultado_label.config(text="Talhões apagados com sucesso!", foreground="green")
            resultado_label2.config(text="Verifique seus arquivos na barra de arquivos :)", foreground='#e0e0e0')
        else:
            resultado_label.config(text="Nenhum talhão apagado.", foreground="orange")
    else:
        resultado_label.config(text="Arquivo não encontrado.", foreground="red")

root = Tk()
root.title("Contador Rural")
root.geometry("650x450") 


frm = Frame(root, padx=0, pady=100, background="#66cc00", width=200, height=500)
frm.grid(row=1, column=0, sticky=(N, S, E, W))

frm_img =Frame(root,padx=100,pady=7,background="#ffffff",width=500,height=150)
frm_img.grid(row=0, column=0,sticky=(W))

imagem = PhotoImage(file="logo.png")
label_imagem = Label(frm_img, image=imagem, background="#ffffff")
label_imagem.grid (row=1,column=0)


label_msg = ttk.Label(frm, text="Olá, Bem-vindo ao CONTADOR RURAL", font=("Cambria", 16), background="#66cc00", foreground='#e0e0e0')
label_msg.place(x=140,y=0) 

label_msg2 = ttk.Label(frm, text="Preencha o campo abaixo com o caminho relativo do arquivo que deseja contar.", font=("Cambria", 10), background="#66cc00", foreground='#e0e0e0')
label_msg2.place(x=110,y=40)  

caminho_relativo = Entry(frm, font=("Arial", 10))
caminho_relativo.place(x=240, y=80)


resultado_label = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label.place(x=220,y=150)

resultado_label2 = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label2.place(x=130,y=200)

# Botão apagar
botao_apagar = ttk.Button(frm, text="Apagar", command=main_apagar)
botao_apagar.place(x=325, y=110)

# Botão salvar
botao_salvar = ttk.Button(frm, text="Salvar", command=main_salvar)
botao_salvar.place(x=225, y=110)

root.mainloop()

