#Comparando variaveis

numero_secreto = 40

#Forma do usuario incluir um valor
chute_do_numero = input("Digite um numero: ") 

print(f"Numero digitado é: {chute_do_numero}")

chute_do_numero = int(chute_do_numero)

if numero_secreto == chute_do_numero:
    print("Você acertou o número")
else:
    print("Você errou o número")