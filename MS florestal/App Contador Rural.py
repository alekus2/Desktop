from tkinter import *
from tkinter import ttk
import pandas as pd
import os

def carregar_talhoes(arquivo):
    talhoes = []
    try:
        df = pd.read_csv(arquivo, delimiter=";", encoding="utf-8")  # Adicione o delimitador correto
        print(f"Colunas no arquivo CSV: {df.columns.tolist()}")
        if df.empty:
            print("O arquivo CSV está vazio.")
            return talhoes
        if 'CD_TALHAO' not in df.columns or 'nm_parcela' not in df.columns:
            print("As colunas 'CD_TALHAO' e 'nm_parcela' não estão presentes.")
            return talhoes
        df['nm_parcela'] = pd.to_numeric(df['nm_parcela'], errors='coerce')
        df = df.dropna(subset=['nm_parcela'])
        df.columns = df.columns.str.strip() 
        df['CD_TALHAO'] = df['CD_TALHAO'].astype(str)
        talhoes = df[['CD_TALHAO', 'nm_parcela']].drop_duplicates().to_dict(orient='records')
        print(df.head()) 
        return talhoes
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")    
    return []


def contagem(talhoes, arquivo_original):
    df = pd.read_csv(arquivo_original, delimiter=";", encoding="utf-8")  
    for talhao_dict in talhoes:
        talhao = talhao_dict['CD_TALHAO']
        nm_parcela = talhao_dict['nm_parcela']
        if nm_parcela < 3:
            parcela_nova = nm_parcela 
        elif nm_parcela % 2 == 0:
            parcela_nova = nm_parcela // 2
        else:
            parcela_nova = (nm_parcela + 1) // 2
        df.loc[df['CD_TALHAO'] == talhao, 'nm_parcela'] = parcela_nova
        print(f"Talhão {talhao} | Parcela original: {nm_parcela} | Nova parcela: {parcela_nova}")

    nome_arquivo = os.path.splitext(arquivo_original)[0]
    novo_arquivo = f"{nome_arquivo}_atualizado.xlsx"
    try:
        df.to_excel(novo_arquivo, index=False, engine='openpyxl')
        print(f"Arquivo salvo como: {novo_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
    return novo_arquivo

def apagar_parcelas(talhoes, arquivo_original):
    df = pd.read_csv(arquivo_original, delimiter=";", encoding="utf-8")

    for talhao_dict in talhoes:
        talhao = talhao_dict['CD_TALHAO']
        nm_parcela = talhao_dict['nm_parcela']
        if nm_parcela <= 3:
            parcela_nova = nm_parcela  
        elif nm_parcela % 2 == 0 and nm_parcela > 3:
            parcela_nova = nm_parcela // 2 
        else:
            continue  
        df.loc[df['CD_TALHAO'] == talhao, 'nm_parcela'] = parcela_nova
        print(f"Talhão {talhao} | Parcela original: {nm_parcela} | Parcela modificada para: {parcela_nova}")

    nome_arquivo = os.path.splitext(arquivo_original)[0]
    novo_arquivo = f"{nome_arquivo}_atualizado.xlsx"
    try:
        df.to_excel(novo_arquivo, index=False, engine='openpyxl')
        print(f"Arquivo salvo com sucesso como: {novo_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
    
    return novo_arquivo


def main_salvar():
    caminho = caminho_relativo.get().strip()
    if caminho == "":
        resultado_label.config(text="Campo não preenchido!", foreground="red")
        return
    talhoes = carregar_talhoes(caminho)
    if talhoes:
        novo_arquivo = contagem(talhoes, caminho)
        resultado_label.config(text="Contagem realizada com sucesso!", foreground="green")
        resultado_label2.config(text=f"Arquivo salvo como: {novo_arquivo}", foreground='#e0e0e0')
    else:
        resultado_label.config(text="Arquivo não encontrado.", foreground="red")

def main_apagar():
    caminho = caminho_relativo.get().strip()
    if caminho == "":
        resultado_label.config(text="Campo não preenchido!", foreground="red")
        return
    talhoes = carregar_talhoes(caminho) 
    if talhoes:
        novo_arquivo = apagar_parcelas(talhoes, caminho)
        resultado_label.config(text="Talhões apagados com sucesso!", foreground="green")
        resultado_label2.config(text=f"Arquivo salvo como: {novo_arquivo}", foreground='#e0e0e0')
    else:
        resultado_label.config(text="Nenhum talhão apagado.", foreground="orange")

root = Tk()
root.title("Contador Rural")
root.geometry("650x450") 

frm = Frame(root, padx=0, pady=100, background="#66cc00", width=200, height=500)
frm.grid(row=1, column=0, sticky=(N, S, E, W))

frm_img = Frame(root, padx=100, pady=7, background="#ffffff", width=500, height=150)
frm_img.grid(row=0, column=0, sticky=(W))

imagem = PhotoImage(file="logo.png")
label_imagem = Label(frm_img, image=imagem, background="#ffffff")
label_imagem.grid(row=1, column=0)

label_msg = ttk.Label(frm, text="Olá, Bem-vindo ao CONTADOR RURAL", font=("Cambria", 16), background="#66cc00", foreground='#e0e0e0')
label_msg.place(x=140, y=0) 

label_msg2 = ttk.Label(frm, text="Preencha o campo abaixo com o caminho relativo do arquivo que deseja contar.", font=("Cambria", 10), background="#66cc00", foreground='#e0e0e0')
label_msg2.place(x=110, y=40)  

caminho_relativo = Entry(frm, font=("Arial", 10))
caminho_relativo.place(x=240, y=80)

resultado_label = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label.place(x=220, y=150)

resultado_label2 = ttk.Label(frm, text="", font=("Agrandir", 16), background="#66cc00", foreground='#e0e0e0')
resultado_label2.place(x=130, y=200)

# Botão apagar
botao_apagar = ttk.Button(frm, text="Apagar", command=main_apagar)
botao_apagar.place(x=325, y=110)

# Botão salvar
botao_salvar = ttk.Button(frm, text="Salvar", command=main_salvar)
botao_salvar.place(x=225, y=110)

root.mainloop()

