qntd = int(input("Digite a quantidade que você quer: "))
pi = input("Você quer par ou ímpar? ").strip().lower()

contador = 0
numero = 0   

while contador < qntd:
    if pi == "par" and numero % 2 == 0:
        print(numero)
        contador += 1
    elif pi == "ímpar" and numero % 2 != 0:
        print(numero)
        contador += 1
    
    numero += 1 