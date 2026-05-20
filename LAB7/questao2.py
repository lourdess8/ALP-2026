N = int(input("Quantos números quer digitar?"))
contador = 1 
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
#cada vez que esse while roda, o contador tem q aumentar
print(f"Quantidade de ímpares: {impares}")





