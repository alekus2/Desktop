def comparador(parcelas):
    resultados = {}
    for parcela in parcelas:
        if parcela > 3:
            if parcela % 2 == 0:  # Par
                resultados[parcela] = 0
            else:  # Ímpar
                resultados[parcela] = 1
        else:  # Menor ou igual a 3
            resultados[parcela] = 0
    return resultados

# Exemplo de uso
parcelas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados_comparador = comparador(parcelas)
print(resultados_comparador)