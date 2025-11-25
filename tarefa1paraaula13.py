import random
numero_secreto = random.randint(1, 10)
 
acertou = False
 
tentativas = 0
 
print("Bem-vindo ao jogo de adivinhar o número!")
print("Tente adivinhar o número que estou pensando (entre 1 e 10).")
 
while not acertou:
    palpite = int(input("\nDigite seu palpite: "))
 
    tentativas += 1
 
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        acertou = True  
    elif palpite > numero_secreto:
        print("Seu palpite foi muito alto. Tente um número menor!")
    else:
        print("Seu palpite foi muito baixo. Tente um número maior!")
 
print(f"\n🏁 Fim do jogo! O número secreto era {numero_secreto}.")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")