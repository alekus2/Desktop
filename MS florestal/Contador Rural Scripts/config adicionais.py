import pandas as pd
import os

def carregar_talhoes(arquivo):
    talhoes = []
    try:
        df = pd.read_csv(arquivo, delimiter=";", encoding="utf-8")
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

def apagar_parcelas(talhoes, arquivo_original):
    df = pd.read_csv(arquivo_original, delimiter=";")
    df['CD_TALHAO'] = df['CD_TALHAO'].astype(str)  
    df['nm_parcela'] = pd.to_numeric(df['nm_parcela'], errors='coerce')  
    if 'nm_parcela_atualizada' not in df.columns:
        df['nm_parcela_atualizada'] = None 
    for talhao_dict in talhoes:
        talhao = talhao_dict['CD_TALHAO']
        nm_parcela = talhao_dict['nm_parcela']
        print(f"Processando talhão: {talhao}, parcela: {nm_parcela}")
        if nm_parcela <= 3:
            parcela_nova = nm_parcela
        elif nm_parcela % 2 == 0 and nm_parcela > 3:
            parcela_nova = nm_parcela
        else:
            continue
        print(f"Atualizando talhão {talhao} para parcela {nm_parcela} com nova parcela {parcela_nova}") 
        df.loc[(df['CD_TALHAO'] == talhao) & (df['nm_parcela'] == nm_parcela), 'nm_parcela_atualizada'] = parcela_nova
    print("DataFrame após as modificações:")
    print(df[['CD_TALHAO', 'nm_parcela', 'nm_parcela_atualizada']].head(10))
    nome_arquivo = os.path.splitext(arquivo_original)[0]
    novo_arquivo = f"{nome_arquivo}_atualizado.xlsx"
    try:
        df.to_excel(novo_arquivo, index=False)
        print(f"Arquivo salvo com sucesso como: {novo_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
    return novo_arquivo


def main_apagar(caminho):
    if caminho == "":
        print("Campo não preenchido!")
        return
    talhoes = carregar_talhoes(caminho) 
    if talhoes:
        novo_arquivo = apagar_parcelas(talhoes, caminho)
        print("Talhões apagados com sucesso!")
        print(f"Arquivo salvo como: {novo_arquivo}")
    else:
        print("Nenhum talhão apagado.")

caminho = input("Digite o caminho do arquivo: ")
if caminho:
    main_apagar(caminho)  