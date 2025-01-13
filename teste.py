def comparador(parcela):
    parcela = int(parcela)
    
    if parcela > 3:
        if parcela % 2 == 0:  # Par
            return 0
        else:  # Ímpar
            return 1
    else:  # Menor ou igual a 3
        return 0

# Exemplo de uso
resultado = comparador(4)  # Chame a função com uma parcela de exemplo
print(resultado)  # Deve imprimir 0= 1
