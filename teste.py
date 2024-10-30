import csv

num = 0

def inc():
    global num
    num += 1
    return num

def carregar_talhoes(arquivo):
    talhoes = {}
    try:
        with open(arquivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                talhao = int(row[0])
                parcelas_talho = int(row[1])
                talhoes[talhao] = parcelas_talho
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome do arquivo.")
    except ValueError:
        print("Erro ao converter dados do CSV. Verifique o formato.")
    return talhoes

def contagem(talhoes):
    global parcela_nova
    for talhao, parcelas_talho in talhoes.items():
        if parcelas_talho < 3:
            parcela_nova = parcelas_talho
        else:
            if parcelas_talho % 2 == 0:
                parcela_nova = parcelas_talho // 2
            else:
                parcela_nova = (parcelas_talho + 1) // 2
        talhoes[talhao] = parcela_nova
    print("Talhões e suas parcelas:", talhoes)

def main():
    arquivo = 'talhoes.csv' 
    talhoes = carregar_talhoes(arquivo)
    if talhoes:
        contagem(talhoes)
    else:
        print("Nenhum talhão carregado.")

main()
