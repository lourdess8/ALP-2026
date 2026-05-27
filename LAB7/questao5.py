import random
numsecreto = random.randint(1, 10)
chances = 5
while chances > 0:
    num = int (input(f"Qual o número secreto? Você tem {chances} chances:"))
    if num != numsecreto:
        chances -= 1
        if num > numsecreto:
            print(" O número é menor que o digitado")
        if num < numsecreto:
            print(" O número é maior que o digitado")
    if num == numsecreto:
            print ("parabéns, vc acertou o número!! ")
print (random.randint(1, 10), "😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍💕💕😁")