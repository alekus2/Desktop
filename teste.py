def excluir (parcela):
    parcela=int(parcela)
    if parcela % 2 == 0 and parcela > 3:
        return parcela/2
    elif parcela % 2 != 0 and parcela > 3:
        return (parcela+1)/2
    else:
        return parcela
#Parcelador de talhoes.
#Com base no nm_parcela dos talhoes.






import random

talhoes = {}
max_talhoes = 220

def autoIncrement(talhao):
    talhao = int(talhao)
    num_zeros = sum(1 for v in talhoes.values() if v == 0)
    num_uns = sum(1 for v in talhoes.values() if v == 1)
    if num_zeros > num_uns:
        talhoes[talhao] = 1
    elif num_uns > num_zeros:
        talhoes[talhao] = 0
    elif num_zeros == num_uns and (num_zeros + num_uns) < max_talhoes:
        talhoes[talhao] = random.choice([0, 1])
    else:
        if num_zeros > num_uns:
            talhoes[talhao] = 1
        else:
            talhoes[talhao] = 0

    return talhoes[talhao]
#Numerador de Talhoes
#Com base no index do talhao.