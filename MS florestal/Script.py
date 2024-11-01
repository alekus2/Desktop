import csv

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

def main():
    arquivo = r'G:\Alex Qualidade\Atividades-SENAC-AGOST\MS florestal\tls.csv'  
    talhoes = carregar_talhoes(arquivo)
    if talhoes:
        contagem(talhoes)
    else:
        print("Nenhum talhão carregado.")

main()
