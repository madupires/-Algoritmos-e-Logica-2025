soma_pares = 0
 
numero_digitado = 1
 
print("Digite números inteiros (0 para encerrar):")
 
while numero_digitado != 0:
    
    numero_digitado = int(input("\nDigite um número: "))
 
    if numero_digitado == 0:
        print("Encerrando o programa... ")
    elif numero_digitado % 2 == 0:
       
        soma_pares += numero_digitado
        print(f"{numero_digitado} é par! Adicionado à soma.")
    else:
       
        print(f"{numero_digitado} é ímpar e foi ignorado.")
 
print(f"\nA soma total dos números pares digitados é: {soma_pares}")