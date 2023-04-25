def contador():
    for i in range(inicio, fim, passo):
        print(i, end=' ')


inicio = int(input("Início: "))
passo = int(input("Passo: "))
fim = int(input("Fim: "))
contador()
