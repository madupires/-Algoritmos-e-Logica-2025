# Jogo de Dados com WHILE

# O programa sorteia um número aleatório entre 1 e 6 (como se fosse um dado), e o usuário deve tentar adivinhar qual número foi sorteado.
# O laço while continua repetindo até que o usuário acerte o número. Ao final, o programa mostra quantas tentativas foram necessárias.

 
import random
 
numero_secreto = random.randint(1, 6)  
tentativas = 0
acertou = False
palpite_usuario = 0 
 
print("\n--- Jogo de Adivinhar o Dado ---")
print("Tente adivinhar o número que o dado sorteou (entre 1 e 6).")

while not acertou:

    palpite_usuario = int(input("\nSeu palpite: "))
 
    if palpite_usuario < 1 or palpite_usuario > 6:
        print("Palpite fora do intervalo. Tente um número entre 1 e 6.")
        continue  
 
    tentativas += 1

    if palpite_usuario == numero_secreto:
        acertou = True  
        print("\n*** Parabéns! Você acertou! ***")
    else:
        print("Errado. Tente novamente!")
 
print(f"\nO número sorteado era: {numero_secreto}!")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")