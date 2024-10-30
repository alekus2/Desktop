
num=0
def inc():
    global num
    num += 1
    return num

def lista_de_talhoes(parcela_nova):
    talhoes={talhao : parcela_nova}
    x = int(input("Insira a quantidade de talhões que deseja alterar: "))
    for _ in range(x):
        talhao = inc()  
        if talhao not in talhoes:
            talhoes[talhao] = 1
        else:
            talhoes[talhao] += 1
   
   
    print(talhoes)

def contagem():
    parcela = int(input("Insira a quantidade de parcelas: "))
    global parcela_nova
    if parcela < 3 or parcela == 2:
        return parcela
    else:
        try:
            if parcela % 2 == 0:
                parcela_nova=parcela/2
            else:
                parcela_nova=(parcela+1)/2
        except ValueError:
            print("Entrada inválida.")
            return 0
parcela_nova = contagem()
lista_de_talhoes(parcela_nova)