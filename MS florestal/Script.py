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
            header = next(reader, None)  # Pula o cabeçalho, mas não levanta StopIteration
            if header is None:
                print("O arquivo CSV está vazio.")
                return talhoes
            for row in reader:
                if len(row) < 2:
                    continue  # Ignora linhas com menos de duas colunas
                try:
                    talhao = int(row[0])  # Converte o talhão para inteiro
                    parcelas_talho = int(row[1])  # Converte a quantidade de parcelas para inteiro
                    talhoes[talhao] = parcelas_talho
                except ValueError:
                    print(f"Erro ao converter dados na linha: {row}.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
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
    arquivo = r'G:\Nova pasta\Atividades-SENAC-AGOST\MS florestal\tls.csv'  
    talhoes = carregar_talhoes(arquivo)
    if talhoes:
        contagem(talhoes)
    else:
        print("Nenhum talhão carregado.")

main()
