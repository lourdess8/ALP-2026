maior = float('-inf') #o número nunca vai ser maior que infinito, logo -infinito 
contador = 1
#tinha que ter um contador no início
while contador <= 10: #ao invés de "soma", tinha que ser contador
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num 
    contador += 1 
    #cada vez que esse while roda, o contador aumenta, uma hora irá chegar a 10 e vai terminar. 
print('O maior número é', maior)
