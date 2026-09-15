quantidade = int( input("Digite a quantidade que você deseja:"))
parouimpar = int( input("Você deseja par ou impar? "))

contador = 0
numero = 0

while contador < quantidade:
    if parouimpar == "par" and numero % 2 == 0:
        print(numero)
        contador += 1
    elif parouimpar == "Impar" and numero % 2 != 0:
        print(numero)
        contador +=1

    numero += 1