contador_pares = 0
contador_impares = 0
 
numero_digitado = 1
 
print("Digite números inteiros (0 para encerrar):")
 
while numero_digitado != 0:
    numero_digitado = int(input("\nDigite um número: "))
 
    if numero_digitado == 0:
        print("Programa encerrado.")
    elif numero_digitado % 2 == 0:
        contador_pares += 1
        print(f"{numero_digitado} é par! Contagem de pares atual: {contador_pares}")
    else:
        contador_impares += 1
        print(f"{numero_digitado} é ímpar! Contagem de ímpares atual: {contador_impares}")
 
print("\n Resultado final:")
print(f"Total de números pares digitados: {contador_pares}")
print(f"Total de números ímpares digitados: {contador_impares}")