soma_pares = 0
soma_impares = 0
 
numero_digitado = 1
 
print("Digite números inteiros (0 para encerrar):")
 
while numero_digitado != 0:
    numero_digitado = int(input("\nDigite um número: "))
 
    if numero_digitado == 0:
        print("Encerrando o programa... ")
    elif numero_digitado % 2 == 0:
        soma_pares += numero_digitado
        print(f"{numero_digitado} é par! Somado aos pares (total: {soma_pares})")
    else:
        soma_impares += numero_digitado
        print(f"{numero_digitado} é ímpar! Somado aos ímpares (total: {soma_impares})")
 
print("\n Resultado final:")
print(f"Soma total dos números pares: {soma_pares}")
print(f"Soma total dos números ímpares: {soma_impares}")