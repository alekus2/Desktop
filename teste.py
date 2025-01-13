def comparador(parcela):
    resultados = {}
    parcela=int(parcela)
    if parcela % 2 == 0 and parcela > 3:
            return resultados[parcela] == 1
    if parcela % 2 !=0 and parcela > 3:
            return resultados[parcela] == 0
    else: 
            return resultados[parcela] == 1
