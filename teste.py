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
        spamwriter.writerow(['Talhão', 'Parcelas Atualizadas'])
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
